"""Generated from Smithy shape ``com.amazonaws.proton#ComponentDeploymentIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_proton.types.deployment_id

ComponentDeploymentIdList: TypeAlias = list[
    "capo_proton.types.deployment_id.DeploymentId"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ComponentDeploymentIdList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> ComponentDeploymentIdList:
    return list(data)
