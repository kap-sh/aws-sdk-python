"""Generated from Smithy shape ``com.amazonaws.elementalinference#UpdateOutputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_elementalinference.types.update_output

UpdateOutputList: TypeAlias = list[
    "aws_sdk_elementalinference.types.update_output.UpdateOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOutputList) -> list:
    import aws_sdk_elementalinference.types.update_output

    out: list = []
    for item in value:
        out.append(aws_sdk_elementalinference.types.update_output.serialize_json(item))
    return out


def deserialize_json(data: list) -> UpdateOutputList:
    import aws_sdk_elementalinference.types.update_output

    out: UpdateOutputList = []
    for item in data:
        out.append(
            aws_sdk_elementalinference.types.update_output.deserialize_json(item)
        )
    return out
