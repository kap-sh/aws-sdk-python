"""Generated from Smithy shape ``com.amazonaws.appstream#StackList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.stack

StackList: TypeAlias = list["capo_appstream.types.stack.Stack"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StackList) -> list:
    import capo_appstream.types.stack

    out: list = []
    for item in value:
        out.append(capo_appstream.types.stack.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> StackList:
    import capo_appstream.types.stack

    out: StackList = []
    for item in data:
        out.append(capo_appstream.types.stack.deserialize_aws_json_1_1(item))
    return out
