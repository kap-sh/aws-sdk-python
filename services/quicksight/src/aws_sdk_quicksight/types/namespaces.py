"""Generated from Smithy shape ``com.amazonaws.quicksight#Namespaces``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.namespace_info_v2

Namespaces: TypeAlias = list[
    "aws_sdk_quicksight.types.namespace_info_v2.NamespaceInfoV2"
]


# --- restJson1 ser/de ---
def serialize_json(value: Namespaces) -> list:
    import aws_sdk_quicksight.types.namespace_info_v2

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.namespace_info_v2.serialize_json(item))
    return out


def deserialize_json(data: list) -> Namespaces:
    import aws_sdk_quicksight.types.namespace_info_v2

    out: Namespaces = []
    for item in data:
        out.append(aws_sdk_quicksight.types.namespace_info_v2.deserialize_json(item))
    return out
