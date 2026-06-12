"""Generated from Smithy shape ``com.amazonaws.efs#DestinationsToCreate``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_efs.types.destination_to_create

DestinationsToCreate: TypeAlias = list[
    "aws_sdk_efs.types.destination_to_create.DestinationToCreate"
]


# --- restJson1 ser/de ---
def serialize_json(value: DestinationsToCreate) -> list:
    import aws_sdk_efs.types.destination_to_create

    out: list = []
    for item in value:
        out.append(aws_sdk_efs.types.destination_to_create.serialize_json(item))
    return out


def deserialize_json(data: list) -> DestinationsToCreate:
    import aws_sdk_efs.types.destination_to_create

    out: DestinationsToCreate = []
    for item in data:
        out.append(aws_sdk_efs.types.destination_to_create.deserialize_json(item))
    return out
