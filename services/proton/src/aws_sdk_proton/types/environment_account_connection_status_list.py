"""Generated from Smithy shape ``com.amazonaws.proton#EnvironmentAccountConnectionStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_proton.types.environment_account_connection_status

EnvironmentAccountConnectionStatusList: TypeAlias = list[
    "aws_sdk_proton.types.environment_account_connection_status.EnvironmentAccountConnectionStatus"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnvironmentAccountConnectionStatusList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> EnvironmentAccountConnectionStatusList:
    return list(data)
