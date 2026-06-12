"""Generated from Smithy shape ``com.amazonaws.opensearch#CancelledChangePropertyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.cancelled_change_property

CancelledChangePropertyList: TypeAlias = list[
    "aws_sdk_opensearch.types.cancelled_change_property.CancelledChangeProperty"
]


# --- restJson1 ser/de ---
def serialize_json(value: CancelledChangePropertyList) -> list:
    import aws_sdk_opensearch.types.cancelled_change_property

    out: list = []
    for item in value:
        out.append(
            aws_sdk_opensearch.types.cancelled_change_property.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CancelledChangePropertyList:
    import aws_sdk_opensearch.types.cancelled_change_property

    out: CancelledChangePropertyList = []
    for item in data:
        out.append(
            aws_sdk_opensearch.types.cancelled_change_property.deserialize_json(item)
        )
    return out
