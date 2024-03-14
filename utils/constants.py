# Regex
GITHUB_REGEX = r'(?:https?://(?:www\.)?)?github\.com\s*/\s*[a-zA-Z0-9_. -]+\s*/\s*[a-zA-Z0-9_.-]+'
CODE_GOOGLE_REGEX = r'(?:https?://(?:www\.)?)?code\.google\.com/[a-zA-Z0-9_.-]+/[a-zA-Z0-9_.-]+'
GITLAB_REGEX = r'(?:https?://(?:www\.)?)?gitlab\.com/[a-zA-Z0-9_.-]+/[a-zA-Z0-9_.-]+'
REPO_REGEXES = [GITHUB_REGEX, GITLAB_REGEX]

# Paths
CORPUS_PATH = '../../Corpus/Test/'
MODEL_PATH = 'oeg/RoBERTa-Repository-Proposal'
TOKENIZER_PATH = 'roberta-base'

# Limits
FOOTNOTE_NUM_LIMIT = 30  # Numbers higher than this are not considered as footnotes
