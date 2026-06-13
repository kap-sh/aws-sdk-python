"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#StreamingAccessDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resource_explorer_2.types.streaming_access_details

StreamingAccessDetailsList: TypeAlias = list[
    "aws_sdk_resource_explorer_2.types.streaming_access_details.StreamingAccessDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: StreamingAccessDetailsList) -> list:
    import aws_sdk_resource_explorer_2.types.streaming_access_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_resource_explorer_2.types.streaming_access_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> StreamingAccessDetailsList:
    import aws_sdk_resource_explorer_2.types.streaming_access_details

    out: StreamingAccessDetailsList = []
    for item in data:
        out.append(
            aws_sdk_resource_explorer_2.types.streaming_access_details.deserialize_json(
                item
            )
        )
    return out
