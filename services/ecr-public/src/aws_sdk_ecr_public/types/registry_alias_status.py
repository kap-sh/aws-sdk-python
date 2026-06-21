"""Generated from Smithy shape ``com.amazonaws.ecrpublic#RegistryAliasStatus``."""

from typing import Literal, TypeAlias, cast

RegistryAliasStatus: TypeAlias = Literal[
    "ACTIVE",
    "PENDING",
    "REJECTED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegistryAliasStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RegistryAliasStatus:
    return cast(RegistryAliasStatus, data)
