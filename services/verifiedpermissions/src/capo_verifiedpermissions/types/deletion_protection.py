"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#DeletionProtection``."""

from typing import Literal, TypeAlias, cast

DeletionProtection: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeletionProtection) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DeletionProtection:
    return cast(DeletionProtection, data)
