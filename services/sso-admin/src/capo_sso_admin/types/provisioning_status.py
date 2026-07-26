"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ProvisioningStatus``."""

from typing import Literal, TypeAlias, cast

ProvisioningStatus: TypeAlias = Literal[
    "LATEST_PERMISSION_SET_PROVISIONED",
    "LATEST_PERMISSION_SET_NOT_PROVISIONED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisioningStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProvisioningStatus:
    return cast(ProvisioningStatus, data)
