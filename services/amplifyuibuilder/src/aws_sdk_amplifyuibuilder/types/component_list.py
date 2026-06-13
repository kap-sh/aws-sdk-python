"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ComponentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.component

ComponentList: TypeAlias = list["aws_sdk_amplifyuibuilder.types.component.Component"]


# --- restJson1 ser/de ---
def serialize_json(value: ComponentList) -> list:
    import aws_sdk_amplifyuibuilder.types.component

    out: list = []
    for item in value:
        out.append(aws_sdk_amplifyuibuilder.types.component.serialize_json(item))
    return out


def deserialize_json(data: list) -> ComponentList:
    import aws_sdk_amplifyuibuilder.types.component

    out: ComponentList = []
    for item in data:
        out.append(aws_sdk_amplifyuibuilder.types.component.deserialize_json(item))
    return out
