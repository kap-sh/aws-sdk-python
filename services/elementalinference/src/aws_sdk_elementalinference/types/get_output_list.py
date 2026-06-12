"""Generated from Smithy shape ``com.amazonaws.elementalinference#GetOutputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_elementalinference.types.get_output

GetOutputList: TypeAlias = list["aws_sdk_elementalinference.types.get_output.GetOutput"]


# --- restJson1 ser/de ---
def serialize_json(value: GetOutputList) -> list:
    import aws_sdk_elementalinference.types.get_output

    out: list = []
    for item in value:
        out.append(aws_sdk_elementalinference.types.get_output.serialize_json(item))
    return out


def deserialize_json(data: list) -> GetOutputList:
    import aws_sdk_elementalinference.types.get_output

    out: GetOutputList = []
    for item in data:
        out.append(aws_sdk_elementalinference.types.get_output.deserialize_json(item))
    return out
