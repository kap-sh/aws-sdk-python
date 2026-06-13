"""Generated from Smithy shape ``com.amazonaws.mailmanager#Rules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.rule

Rules: TypeAlias = list["aws_sdk_mailmanager.types.rule.Rule"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Rules) -> list:
    import aws_sdk_mailmanager.types.rule

    out: list = []
    for item in value:
        out.append(aws_sdk_mailmanager.types.rule.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Rules:
    import aws_sdk_mailmanager.types.rule

    out: Rules = []
    for item in data:
        out.append(aws_sdk_mailmanager.types.rule.deserialize_aws_json_1_0(item))
    return out
