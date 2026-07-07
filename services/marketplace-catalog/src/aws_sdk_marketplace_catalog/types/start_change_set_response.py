"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#StartChangeSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.arn
    import aws_sdk_marketplace_catalog.types.resource_id


class StartChangeSetResponse(TypedDict, closed=True):
    change_set_id: NotRequired[
        "aws_sdk_marketplace_catalog.types.resource_id.ResourceId"
    ]
    """<p>Unique identifier generated for the request.</p>"""
    change_set_arn: NotRequired["aws_sdk_marketplace_catalog.types.arn.ARN"]
    """<p>The ARN associated to the unique identifier generated for the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartChangeSetResponse) -> dict:
    out: dict = {}
    if "change_set_id" in value:
        out["ChangeSetId"] = value["change_set_id"]
    if "change_set_arn" in value:
        out["ChangeSetArn"] = value["change_set_arn"]
    return out


def deserialize_json(data: dict) -> StartChangeSetResponse:
    out: StartChangeSetResponse = {}  # type: ignore[typeddict-item]
    if "ChangeSetId" in data:
        out["change_set_id"] = data["ChangeSetId"]
    if "ChangeSetArn" in data:
        out["change_set_arn"] = data["ChangeSetArn"]
    return out
