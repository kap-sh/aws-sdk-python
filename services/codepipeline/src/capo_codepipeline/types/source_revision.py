"""Generated from Smithy shape ``com.amazonaws.codepipeline#SourceRevision``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codepipeline.types.action_name
    import capo_codepipeline.types.revision
    import capo_codepipeline.types.revision_summary
    import capo_codepipeline.types.url


class SourceRevision(TypedDict, closed=True):
    action_name: "capo_codepipeline.types.action_name.ActionName"
    """<p>The name of the action that processed the revision to the source artifact.</p>"""
    revision_id: NotRequired["capo_codepipeline.types.revision.Revision"]
    """<p>The system-generated unique ID that identifies the revision number of the artifact.</p>"""
    revision_summary: NotRequired[
        "capo_codepipeline.types.revision_summary.RevisionSummary"
    ]
    """<p>Summary information about the most recent revision of the artifact. For GitHub and CodeCommit repositories, the commit message. For Amazon S3 buckets or actions, the user-provided content of a <code>codepipeline-artifact-revision-summary</code> key specified in the object metadata.</p>"""
    revision_url: NotRequired["capo_codepipeline.types.url.Url"]
    """<p>The commit ID for the artifact revision. For artifacts stored in GitHub or CodeCommit repositories, the commit ID is linked to a commit details page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceRevision) -> dict:
    out: dict = {}
    out["actionName"] = value["action_name"]
    if "revision_id" in value:
        out["revisionId"] = value["revision_id"]
    if "revision_summary" in value:
        out["revisionSummary"] = value["revision_summary"]
    if "revision_url" in value:
        out["revisionUrl"] = value["revision_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceRevision:
    out: SourceRevision = {}  # type: ignore[typeddict-item]
    if "actionName" in data:
        out["action_name"] = data["actionName"]
    else:
        raise DeserializationError("SourceRevision.action_name required")
    if "revisionId" in data:
        out["revision_id"] = data["revisionId"]
    if "revisionSummary" in data:
        out["revision_summary"] = data["revisionSummary"]
    if "revisionUrl" in data:
        out["revision_url"] = data["revisionUrl"]
    return out
