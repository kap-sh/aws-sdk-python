"""Generated from Smithy shape ``com.amazonaws.kendra#GitHubDocumentCrawlProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.boolean


class GitHubDocumentCrawlProperties(TypedDict, closed=True):
    crawl_repository_documents: "capo_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> to index all files with a repository.</p>"""
    crawl_issue: "capo_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> to index all issues within a repository.</p>"""
    crawl_issue_comment: "capo_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> to index all comments on issues.</p>"""
    crawl_issue_comment_attachment: "capo_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> to include all comment attachments for issues.</p>"""
    crawl_pull_request: "capo_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> to index all pull requests within a repository.</p>"""
    crawl_pull_request_comment: "capo_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> to index all comments on pull requests.</p>"""
    crawl_pull_request_comment_attachment: "capo_kendra.types.boolean.Boolean"
    """<p> <code>TRUE</code> to include all comment attachments for pull requests.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GitHubDocumentCrawlProperties) -> dict:
    out: dict = {}
    out["CrawlRepositoryDocuments"] = value.get("crawl_repository_documents", False)
    out["CrawlIssue"] = value.get("crawl_issue", False)
    out["CrawlIssueComment"] = value.get("crawl_issue_comment", False)
    out["CrawlIssueCommentAttachment"] = value.get(
        "crawl_issue_comment_attachment", False
    )
    out["CrawlPullRequest"] = value.get("crawl_pull_request", False)
    out["CrawlPullRequestComment"] = value.get("crawl_pull_request_comment", False)
    out["CrawlPullRequestCommentAttachment"] = value.get(
        "crawl_pull_request_comment_attachment", False
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GitHubDocumentCrawlProperties:
    out: GitHubDocumentCrawlProperties = {}  # type: ignore[typeddict-item]
    if "CrawlRepositoryDocuments" in data:
        out["crawl_repository_documents"] = data["CrawlRepositoryDocuments"]
    else:
        out["crawl_repository_documents"] = False
    if "CrawlIssue" in data:
        out["crawl_issue"] = data["CrawlIssue"]
    else:
        out["crawl_issue"] = False
    if "CrawlIssueComment" in data:
        out["crawl_issue_comment"] = data["CrawlIssueComment"]
    else:
        out["crawl_issue_comment"] = False
    if "CrawlIssueCommentAttachment" in data:
        out["crawl_issue_comment_attachment"] = data["CrawlIssueCommentAttachment"]
    else:
        out["crawl_issue_comment_attachment"] = False
    if "CrawlPullRequest" in data:
        out["crawl_pull_request"] = data["CrawlPullRequest"]
    else:
        out["crawl_pull_request"] = False
    if "CrawlPullRequestComment" in data:
        out["crawl_pull_request_comment"] = data["CrawlPullRequestComment"]
    else:
        out["crawl_pull_request_comment"] = False
    if "CrawlPullRequestCommentAttachment" in data:
        out["crawl_pull_request_comment_attachment"] = data[
            "CrawlPullRequestCommentAttachment"
        ]
    else:
        out["crawl_pull_request_comment_attachment"] = False
    return out
