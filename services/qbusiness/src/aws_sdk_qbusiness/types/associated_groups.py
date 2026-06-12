"""Generated from Smithy shape ``com.amazonaws.qbusiness#AssociatedGroups``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.associated_group

AssociatedGroups: TypeAlias = list["aws_sdk_qbusiness.types.associated_group.AssociatedGroup"]


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedGroups) -> list:
    import aws_sdk_qbusiness.types.associated_group
    out: list = []
    for item in value:
        out.append(aws_sdk_qbusiness.types.associated_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssociatedGroups:
    import aws_sdk_qbusiness.types.associated_group
    out: AssociatedGroups = []
    for item in data:
        out.append(aws_sdk_qbusiness.types.associated_group.deserialize_json(item))
    return out