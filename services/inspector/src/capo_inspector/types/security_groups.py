"""Generated from Smithy shape ``com.amazonaws.inspector#SecurityGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector.types.security_group

SecurityGroups: TypeAlias = list["capo_inspector.types.security_group.SecurityGroup"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecurityGroups) -> list:
    import capo_inspector.types.security_group

    out: list = []
    for item in value:
        out.append(capo_inspector.types.security_group.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SecurityGroups:
    import capo_inspector.types.security_group

    out: SecurityGroups = []
    for item in data:
        out.append(capo_inspector.types.security_group.deserialize_aws_json_1_1(item))
    return out
