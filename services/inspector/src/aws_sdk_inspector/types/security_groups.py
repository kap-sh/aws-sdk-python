"""Generated from Smithy shape ``com.amazonaws.inspector#SecurityGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector.types.security_group

SecurityGroups: TypeAlias = list["aws_sdk_inspector.types.security_group.SecurityGroup"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecurityGroups) -> list:
    import aws_sdk_inspector.types.security_group

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector.types.security_group.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SecurityGroups:
    import aws_sdk_inspector.types.security_group

    out: SecurityGroups = []
    for item in data:
        out.append(
            aws_sdk_inspector.types.security_group.deserialize_aws_json_1_1(item)
        )
    return out
