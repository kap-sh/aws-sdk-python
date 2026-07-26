"""Generated from Smithy shape ``com.amazonaws.greengrassv2#EffectiveDeploymentErrorTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_greengrassv2.types.effective_deployment_error_type

EffectiveDeploymentErrorTypeList: TypeAlias = list[
    "capo_greengrassv2.types.effective_deployment_error_type.EffectiveDeploymentErrorType"
]


# --- restJson1 ser/de ---
def serialize_json(value: EffectiveDeploymentErrorTypeList) -> list:
    return list(value)


def deserialize_json(data: list) -> EffectiveDeploymentErrorTypeList:
    return list(data)
