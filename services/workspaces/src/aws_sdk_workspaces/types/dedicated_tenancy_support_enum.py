"""Generated from Smithy shape ``com.amazonaws.workspaces#DedicatedTenancySupportEnum``."""

from typing import Literal, TypeAlias, cast

DedicatedTenancySupportEnum: TypeAlias = Literal["ENABLED",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DedicatedTenancySupportEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DedicatedTenancySupportEnum:
    return cast(DedicatedTenancySupportEnum, data)
