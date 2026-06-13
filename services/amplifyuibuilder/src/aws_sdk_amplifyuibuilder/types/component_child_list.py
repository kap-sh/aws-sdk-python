"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ComponentChildList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.component_child

ComponentChildList: TypeAlias = list[
    "aws_sdk_amplifyuibuilder.types.component_child.ComponentChild"
]


# --- restJson1 ser/de ---
def serialize_json(value: ComponentChildList) -> list:
    import aws_sdk_amplifyuibuilder.types.component_child

    out: list = []
    for item in value:
        out.append(aws_sdk_amplifyuibuilder.types.component_child.serialize_json(item))
    return out


def deserialize_json(data: list) -> ComponentChildList:
    import aws_sdk_amplifyuibuilder.types.component_child

    out: ComponentChildList = []
    for item in data:
        out.append(
            aws_sdk_amplifyuibuilder.types.component_child.deserialize_json(item)
        )
    return out
