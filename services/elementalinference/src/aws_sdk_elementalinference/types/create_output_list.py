"""Generated from Smithy shape ``com.amazonaws.elementalinference#CreateOutputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_elementalinference.types.create_output

CreateOutputList: TypeAlias = list[
    "aws_sdk_elementalinference.types.create_output.CreateOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: CreateOutputList) -> list:
    import aws_sdk_elementalinference.types.create_output

    out: list = []
    for item in value:
        out.append(aws_sdk_elementalinference.types.create_output.serialize_json(item))
    return out


def deserialize_json(data: list) -> CreateOutputList:
    import aws_sdk_elementalinference.types.create_output

    out: CreateOutputList = []
    for item in data:
        out.append(
            aws_sdk_elementalinference.types.create_output.deserialize_json(item)
        )
    return out
