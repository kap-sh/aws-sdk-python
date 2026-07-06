"""Generated from Smithy shape ``com.amazonaws.personalizeevents#PutItemsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_personalize_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_personalize_events.types.arn
    import aws_sdk_personalize_events.types.item_list


class PutItemsRequest(TypedDict, closed=True):
    dataset_arn: "aws_sdk_personalize_events.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Items dataset you are adding the item or items to.</p>"""
    items: "aws_sdk_personalize_events.types.item_list.ItemList"
    """<p>A list of item data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutItemsRequest) -> dict:
    out: dict = {}
    out["datasetArn"] = value["dataset_arn"]
    import aws_sdk_personalize_events.types.item_list

    out["items"] = aws_sdk_personalize_events.types.item_list.serialize_json(
        value["items"]
    )
    return out


def deserialize_json(data: dict) -> PutItemsRequest:
    out: PutItemsRequest = {}  # type: ignore[typeddict-item]
    if "datasetArn" in data:
        out["dataset_arn"] = data["datasetArn"]
    else:
        raise DeserializationError("PutItemsRequest.dataset_arn required")
    if "items" in data:
        import aws_sdk_personalize_events.types.item_list

        out["items"] = aws_sdk_personalize_events.types.item_list.deserialize_json(
            data["items"]
        )
    else:
        raise DeserializationError("PutItemsRequest.items required")
    return out
