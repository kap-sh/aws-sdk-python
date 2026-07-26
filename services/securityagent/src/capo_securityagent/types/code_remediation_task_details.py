"""Generated from Smithy shape ``com.amazonaws.securityagent#CodeRemediationTaskDetails``."""

from typing_extensions import NotRequired, TypedDict


class CodeRemediationTaskDetails(TypedDict, closed=True):
    repo_name: NotRequired["str"]
    """<p>The name of the repository where the remediation was applied.</p>"""
    code_diff_link: NotRequired["str"]
    """<p>The link to the code diff for the remediation.</p>"""
    pull_request_link: NotRequired["str"]
    """<p>The link to the pull request created for the remediation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeRemediationTaskDetails) -> dict:
    out: dict = {}
    if "repo_name" in value:
        out["repoName"] = value["repo_name"]
    if "code_diff_link" in value:
        out["codeDiffLink"] = value["code_diff_link"]
    if "pull_request_link" in value:
        out["pullRequestLink"] = value["pull_request_link"]
    return out


def deserialize_json(data: dict) -> CodeRemediationTaskDetails:
    out: CodeRemediationTaskDetails = {}  # type: ignore[typeddict-item]
    if "repoName" in data:
        out["repo_name"] = data["repoName"]
    if "codeDiffLink" in data:
        out["code_diff_link"] = data["codeDiffLink"]
    if "pullRequestLink" in data:
        out["pull_request_link"] = data["pullRequestLink"]
    return out
