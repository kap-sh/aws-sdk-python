"""Generated from Smithy shape ``com.amazonaws.fms#FailedItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fms.types.failed_item_reason
    import aws_sdk_fms.types.identifier


class FailedItem(TypedDict):
    uri: NotRequired["aws_sdk_fms.types.identifier.Identifier"]
    """<p>The univeral resource indicator (URI) of the resource that failed.</p>"""
    reason: NotRequired["aws_sdk_fms.types.failed_item_reason.FailedItemReason"]
    """<p>The reason the resource's association could not be updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailedItem) -> dict:
    out: dict = {}
    if "uri" in value:
        out["URI"] = value["uri"]
    if "reason" in value:
        import aws_sdk_fms.types.failed_item_reason

        out["Reason"] = aws_sdk_fms.types.failed_item_reason.serialize_aws_json_1_1(
            value["reason"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FailedItem:
    out: FailedItem = {}  # type: ignore[typeddict-item]
    if "URI" in data:
        out["uri"] = data["URI"]
    if "Reason" in data:
        import aws_sdk_fms.types.failed_item_reason

        out["reason"] = aws_sdk_fms.types.failed_item_reason.deserialize_aws_json_1_1(
            data["Reason"]
        )
    return out
