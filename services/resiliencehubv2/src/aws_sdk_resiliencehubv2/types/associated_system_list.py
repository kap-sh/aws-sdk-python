"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#AssociatedSystemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.associated_system

AssociatedSystemList: TypeAlias = list[
    "aws_sdk_resiliencehubv2.types.associated_system.AssociatedSystem"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedSystemList) -> list:
    import aws_sdk_resiliencehubv2.types.associated_system

    out: list = []
    for item in value:
        out.append(aws_sdk_resiliencehubv2.types.associated_system.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssociatedSystemList:
    import aws_sdk_resiliencehubv2.types.associated_system

    out: AssociatedSystemList = []
    for item in data:
        out.append(
            aws_sdk_resiliencehubv2.types.associated_system.deserialize_json(item)
        )
    return out
