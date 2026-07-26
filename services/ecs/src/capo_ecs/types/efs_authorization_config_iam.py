"""Generated from Smithy shape ``com.amazonaws.ecs#EFSAuthorizationConfigIAM``."""

from typing import Literal, TypeAlias, cast

EFSAuthorizationConfigIAM: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EFSAuthorizationConfigIAM) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EFSAuthorizationConfigIAM:
    return cast(EFSAuthorizationConfigIAM, data)
