"""Generated from Smithy shape ``com.amazonaws.connectcases#CreateRelatedItemResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcases.types.related_item_arn
    import capo_connectcases.types.related_item_id


class CreateRelatedItemResponse(TypedDict, closed=True):
    related_item_id: "capo_connectcases.types.related_item_id.RelatedItemId"
    """<p>The unique identifier of the related item.</p>"""
    related_item_arn: "capo_connectcases.types.related_item_arn.RelatedItemArn"
    """<p>The Amazon Resource Name (ARN) of the related item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRelatedItemResponse) -> dict:
    out: dict = {}
    out["relatedItemId"] = value["related_item_id"]
    out["relatedItemArn"] = value["related_item_arn"]
    return out


def deserialize_json(data: dict) -> CreateRelatedItemResponse:
    out: CreateRelatedItemResponse = {}  # type: ignore[typeddict-item]
    if "relatedItemId" in data:
        out["related_item_id"] = data["relatedItemId"]
    else:
        raise DeserializationError("CreateRelatedItemResponse.related_item_id required")
    if "relatedItemArn" in data:
        out["related_item_arn"] = data["relatedItemArn"]
    else:
        raise DeserializationError(
            "CreateRelatedItemResponse.related_item_arn required"
        )
    return out
