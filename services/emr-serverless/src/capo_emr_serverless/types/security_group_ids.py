"""Generated from Smithy shape ``com.amazonaws.emrserverless#SecurityGroupIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr_serverless.types.security_group_string

SecurityGroupIds: TypeAlias = list[
    "capo_emr_serverless.types.security_group_string.SecurityGroupString"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityGroupIds) -> list:
    return list(value)


def deserialize_json(data: list) -> SecurityGroupIds:
    return list(data)
