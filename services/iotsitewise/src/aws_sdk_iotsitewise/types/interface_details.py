"""Generated from Smithy shape ``com.amazonaws.iotsitewise#InterfaceDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.interface_relationship

InterfaceDetails: TypeAlias = list[
    "aws_sdk_iotsitewise.types.interface_relationship.InterfaceRelationship"
]


# --- restJson1 ser/de ---
def serialize_json(value: InterfaceDetails) -> list:
    import aws_sdk_iotsitewise.types.interface_relationship

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotsitewise.types.interface_relationship.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> InterfaceDetails:
    import aws_sdk_iotsitewise.types.interface_relationship

    out: InterfaceDetails = []
    for item in data:
        out.append(
            aws_sdk_iotsitewise.types.interface_relationship.deserialize_json(item)
        )
    return out
