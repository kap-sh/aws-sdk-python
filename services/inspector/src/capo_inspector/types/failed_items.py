"""Generated from Smithy shape ``com.amazonaws.inspector#FailedItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector.types.arn
    import capo_inspector.types.failed_item_details

FailedItems: TypeAlias = dict[
    "capo_inspector.types.arn.Arn",
    "capo_inspector.types.failed_item_details.FailedItemDetails",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: FailedItems) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_inspector.types.failed_item_details

        out[key] = capo_inspector.types.failed_item_details.serialize_aws_json_1_1(
            value
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FailedItems:
    out: FailedItems = {}
    for key, value in data.items():
        import capo_inspector.types.failed_item_details

        out[key] = capo_inspector.types.failed_item_details.deserialize_aws_json_1_1(
            value
        )
    return out
