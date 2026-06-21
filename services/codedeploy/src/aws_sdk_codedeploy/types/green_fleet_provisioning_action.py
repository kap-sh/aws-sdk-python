"""Generated from Smithy shape ``com.amazonaws.codedeploy#GreenFleetProvisioningAction``."""

from typing import Literal, TypeAlias, cast

GreenFleetProvisioningAction: TypeAlias = Literal[
    "DISCOVER_EXISTING",
    "COPY_AUTO_SCALING_GROUP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GreenFleetProvisioningAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GreenFleetProvisioningAction:
    return cast(GreenFleetProvisioningAction, data)
