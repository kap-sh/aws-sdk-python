"""Generated from Smithy shape ``com.amazonaws.evs#SecurityGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_evs.types.security_group_id

SecurityGroups: TypeAlias = list["capo_evs.types.security_group_id.SecurityGroupId"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SecurityGroups) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> SecurityGroups:
    return list(data)
