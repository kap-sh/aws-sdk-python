"""Generated from Smithy shape ``com.amazonaws.mediatailor#ResponseOutputs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.response_output_item

ResponseOutputs: TypeAlias = list[
    "aws_sdk_mediatailor.types.response_output_item.ResponseOutputItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResponseOutputs) -> list:
    import aws_sdk_mediatailor.types.response_output_item

    out: list = []
    for item in value:
        out.append(aws_sdk_mediatailor.types.response_output_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResponseOutputs:
    import aws_sdk_mediatailor.types.response_output_item

    out: ResponseOutputs = []
    for item in data:
        out.append(
            aws_sdk_mediatailor.types.response_output_item.deserialize_json(item)
        )
    return out
