"""Generated from Smithy shape ``com.amazonaws.greengrassv2#DeploymentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.deployment

DeploymentList: TypeAlias = list["aws_sdk_greengrassv2.types.deployment.Deployment"]


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentList) -> list:
    import aws_sdk_greengrassv2.types.deployment

    out: list = []
    for item in value:
        out.append(aws_sdk_greengrassv2.types.deployment.serialize_json(item))
    return out


def deserialize_json(data: list) -> DeploymentList:
    import aws_sdk_greengrassv2.types.deployment

    out: DeploymentList = []
    for item in data:
        out.append(aws_sdk_greengrassv2.types.deployment.deserialize_json(item))
    return out
