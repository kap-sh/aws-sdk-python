"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#PathElementList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.path_element

PathElementList: TypeAlias = list[
    "aws_sdk_accessanalyzer.types.path_element.PathElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: PathElementList) -> list:
    import aws_sdk_accessanalyzer.types.path_element

    out: list = []
    for item in value:
        out.append(aws_sdk_accessanalyzer.types.path_element.serialize_json(item))
    return out


def deserialize_json(data: list) -> PathElementList:
    import aws_sdk_accessanalyzer.types.path_element

    out: PathElementList = []
    for item in data:
        out.append(aws_sdk_accessanalyzer.types.path_element.deserialize_json(item))
    return out
