"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#FlowTemplateSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotthingsgraph.types.arn
    import aws_sdk_iotthingsgraph.types.timestamp
    import aws_sdk_iotthingsgraph.types.urn
    import aws_sdk_iotthingsgraph.types.version


class FlowTemplateSummary(TypedDict, closed=True):
    id: NotRequired["aws_sdk_iotthingsgraph.types.urn.Urn"]
    """<p>The ID of the workflow.</p>"""
    arn: NotRequired["aws_sdk_iotthingsgraph.types.arn.Arn"]
    """<p>The ARN of the workflow.</p>"""
    revision_number: NotRequired["aws_sdk_iotthingsgraph.types.version.Version"]
    """<p>The revision number of the workflow.</p>"""
    created_at: NotRequired["aws_sdk_iotthingsgraph.types.timestamp.Timestamp"]
    """<p>The date when the workflow was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlowTemplateSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "revision_number" in value:
        out["revisionNumber"] = value["revision_number"]
    if "created_at" in value:
        import aws_sdk_iotthingsgraph.types.timestamp

        out["createdAt"] = (
            aws_sdk_iotthingsgraph.types.timestamp.serialize_aws_json_1_1(
                value["created_at"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FlowTemplateSummary:
    out: FlowTemplateSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "revisionNumber" in data:
        out["revision_number"] = data["revisionNumber"]
    if "createdAt" in data:
        import aws_sdk_iotthingsgraph.types.timestamp

        out["created_at"] = (
            aws_sdk_iotthingsgraph.types.timestamp.deserialize_aws_json_1_1(
                data["createdAt"]
            )
        )
    return out
