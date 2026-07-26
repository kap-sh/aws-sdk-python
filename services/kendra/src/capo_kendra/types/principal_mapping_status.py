"""Generated from Smithy shape ``com.amazonaws.kendra#PrincipalMappingStatus``."""

from typing import Literal, TypeAlias, cast

PrincipalMappingStatus: TypeAlias = Literal[
    "FAILED",
    "SUCCEEDED",
    "PROCESSING",
    "DELETING",
    "DELETED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PrincipalMappingStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PrincipalMappingStatus:
    return cast(PrincipalMappingStatus, data)
