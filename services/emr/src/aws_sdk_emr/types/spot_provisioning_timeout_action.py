"""Generated from Smithy shape ``com.amazonaws.emr#SpotProvisioningTimeoutAction``."""

from typing import Literal, TypeAlias, cast

SpotProvisioningTimeoutAction: TypeAlias = Literal[
    "SWITCH_TO_ON_DEMAND",
    "TERMINATE_CLUSTER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SpotProvisioningTimeoutAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SpotProvisioningTimeoutAction:
    return cast(SpotProvisioningTimeoutAction, data)
