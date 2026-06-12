"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#CancelChangeSetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.arn
    import aws_sdk_marketplace_catalog.types.resource_id


class CancelChangeSetResponse(TypedDict):
    change_set_id: NotRequired[
        "aws_sdk_marketplace_catalog.types.resource_id.ResourceId"
    ]
    """<p>The unique identifier for the change set referenced in this request.</p>"""
    change_set_arn: NotRequired["aws_sdk_marketplace_catalog.types.arn.ARN"]
    """<p>The ARN associated with the change set referenced in this request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelChangeSetResponse) -> dict:
    out: dict = {}
    if "change_set_id" in value:
        out["ChangeSetId"] = value["change_set_id"]
    if "change_set_arn" in value:
        out["ChangeSetArn"] = value["change_set_arn"]
    return out


def deserialize_json(data: dict) -> CancelChangeSetResponse:
    out: CancelChangeSetResponse = {}  # type: ignore[typeddict-item]
    if "ChangeSetId" in data:
        out["change_set_id"] = data["ChangeSetId"]
    if "ChangeSetArn" in data:
        out["change_set_arn"] = data["ChangeSetArn"]
    return out
