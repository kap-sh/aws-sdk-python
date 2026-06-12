"""Generated from Smithy shape ``com.amazonaws.greengrass#__listOfResourceAccessPolicy``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.resource_access_policy

__listOfResourceAccessPolicy: TypeAlias = list[
    "aws_sdk_greengrass.types.resource_access_policy.ResourceAccessPolicy"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfResourceAccessPolicy) -> list:
    import aws_sdk_greengrass.types.resource_access_policy

    out: list = []
    for item in value:
        out.append(aws_sdk_greengrass.types.resource_access_policy.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfResourceAccessPolicy:
    import aws_sdk_greengrass.types.resource_access_policy

    out: __listOfResourceAccessPolicy = []
    for item in data:
        out.append(
            aws_sdk_greengrass.types.resource_access_policy.deserialize_json(item)
        )
    return out
