"""Generated from Smithy shape ``com.amazonaws.greengrass#Deployments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.deployment

Deployments: TypeAlias = list["aws_sdk_greengrass.types.deployment.Deployment"]


# --- restJson1 ser/de ---
def serialize_json(value: Deployments) -> list:
    import aws_sdk_greengrass.types.deployment

    out: list = []
    for item in value:
        out.append(aws_sdk_greengrass.types.deployment.serialize_json(item))
    return out


def deserialize_json(data: list) -> Deployments:
    import aws_sdk_greengrass.types.deployment

    out: Deployments = []
    for item in data:
        out.append(aws_sdk_greengrass.types.deployment.deserialize_json(item))
    return out
