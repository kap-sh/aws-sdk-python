"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionRevision``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.revision
    import aws_sdk_codepipeline.types.revision_change_identifier
    import aws_sdk_codepipeline.types.timestamp


class ActionRevision(TypedDict, closed=True):
    revision_id: "aws_sdk_codepipeline.types.revision.Revision"
    """<p>The system-generated unique ID that identifies the revision number of the action.</p>"""
    revision_change_id: (
        "aws_sdk_codepipeline.types.revision_change_identifier.RevisionChangeIdentifier"
    )
    """<p>The unique identifier of the change that set the state to this revision (for example, a deployment ID or timestamp).</p>"""
    created: "aws_sdk_codepipeline.types.timestamp.Timestamp"
    """<p>The date and time when the most recent version of the action was created, in timestamp format.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionRevision) -> dict:
    out: dict = {}
    out["revisionId"] = value["revision_id"]
    out["revisionChangeId"] = value["revision_change_id"]
    import aws_sdk_codepipeline.types.timestamp

    out["created"] = aws_sdk_codepipeline.types.timestamp.serialize_aws_json_1_1(
        value["created"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ActionRevision:
    out: ActionRevision = {}  # type: ignore[typeddict-item]
    if "revisionId" in data:
        out["revision_id"] = data["revisionId"]
    else:
        raise DeserializationError("ActionRevision.revision_id required")
    if "revisionChangeId" in data:
        out["revision_change_id"] = data["revisionChangeId"]
    else:
        raise DeserializationError("ActionRevision.revision_change_id required")
    if "created" in data:
        import aws_sdk_codepipeline.types.timestamp

        out["created"] = aws_sdk_codepipeline.types.timestamp.deserialize_aws_json_1_1(
            data["created"]
        )
    else:
        raise DeserializationError("ActionRevision.created required")
    return out
