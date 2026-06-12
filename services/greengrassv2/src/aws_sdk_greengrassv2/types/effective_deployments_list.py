"""Generated from Smithy shape ``com.amazonaws.greengrassv2#EffectiveDeploymentsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.effective_deployment

EffectiveDeploymentsList: TypeAlias = list[
    "aws_sdk_greengrassv2.types.effective_deployment.EffectiveDeployment"
]


# --- restJson1 ser/de ---
def serialize_json(value: EffectiveDeploymentsList) -> list:
    import aws_sdk_greengrassv2.types.effective_deployment

    out: list = []
    for item in value:
        out.append(aws_sdk_greengrassv2.types.effective_deployment.serialize_json(item))
    return out


def deserialize_json(data: list) -> EffectiveDeploymentsList:
    import aws_sdk_greengrassv2.types.effective_deployment

    out: EffectiveDeploymentsList = []
    for item in data:
        out.append(
            aws_sdk_greengrassv2.types.effective_deployment.deserialize_json(item)
        )
    return out
