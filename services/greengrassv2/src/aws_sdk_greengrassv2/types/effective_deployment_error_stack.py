"""Generated from Smithy shape ``com.amazonaws.greengrassv2#EffectiveDeploymentErrorStack``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.effective_deployment_error_code

EffectiveDeploymentErrorStack: TypeAlias = list[
    "aws_sdk_greengrassv2.types.effective_deployment_error_code.EffectiveDeploymentErrorCode"
]


# --- restJson1 ser/de ---
def serialize_json(value: EffectiveDeploymentErrorStack) -> list:
    return list(value)


def deserialize_json(data: list) -> EffectiveDeploymentErrorStack:
    return list(data)
