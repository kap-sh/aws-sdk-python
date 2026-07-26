"""Generated from Smithy shape ``com.amazonaws.greengrassv2#EffectiveDeploymentsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_greengrassv2.types.effective_deployment

EffectiveDeploymentsList: TypeAlias = list[
    "capo_greengrassv2.types.effective_deployment.EffectiveDeployment"
]


# --- restJson1 ser/de ---
def serialize_json(value: EffectiveDeploymentsList) -> list:
    import capo_greengrassv2.types.effective_deployment

    out: list = []
    for item in value:
        out.append(capo_greengrassv2.types.effective_deployment.serialize_json(item))
    return out


def deserialize_json(data: list) -> EffectiveDeploymentsList:
    import capo_greengrassv2.types.effective_deployment

    out: EffectiveDeploymentsList = []
    for item in data:
        out.append(capo_greengrassv2.types.effective_deployment.deserialize_json(item))
    return out
