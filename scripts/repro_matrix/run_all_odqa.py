import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate regression matrix for MS MARCO corpora.')
    parser.add_argument('--topics', type=str, help='Topic to run [tqa, nq].', choices=['tqa', 'nq'], required=True)
    parser.add_argument('--dry-run', action='store_true', default=False, help='Print out commands but do not execute.')
    parser.add_argument('--skip-eval', action='store_true', default=False, help='Skip running trec_eval.')
    parser.add_argument('--display-commands', action='store_true', default=False, help='Display command.')
    parser.add_argument('--full-topk', action='store_true', default=False, help='Run topk 5-1000, default is topk 5-100')
    args = parser.parse_args()
    
    cmd = f'python -m pyserini.2cr.odqa ' + \
                f'--topic {args.topics} ' + \
                f'--all '
    
    if args.dry_run:
        cmd += f'--dry-run '
    if args.display_commands:
        cmd += f'--display-commands '
    if args.full_topk:
        cmd += f'--full-topk '
    if args.skip_eval:
        cmd += f'--skip-eval '
    
    os.system(cmd)