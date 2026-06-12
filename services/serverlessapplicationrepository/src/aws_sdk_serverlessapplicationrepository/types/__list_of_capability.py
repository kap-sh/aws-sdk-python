"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#__listOfCapability``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_serverlessapplicationrepository.types.capability

__listOfCapability: TypeAlias = list[
    "aws_sdk_serverlessapplicationrepository.types.capability.Capability"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfCapability) -> list:
    import aws_sdk_serverlessapplicationrepository.types.capability

    out: list = []
    for item in value:
        out.append(
            aws_sdk_serverlessapplicationrepository.types.capability.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfCapability:
    import aws_sdk_serverlessapplicationrepository.types.capability

    out: __listOfCapability = []
    for item in data:
        out.append(
            aws_sdk_serverlessapplicationrepository.types.capability.deserialize_json(
                item
            )
        )
    return out
