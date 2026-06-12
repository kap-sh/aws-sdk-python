"""Generated from Smithy shape ``com.amazonaws.ssm#Runbooks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.runbook

Runbooks: TypeAlias = list["aws_sdk_ssm.types.runbook.Runbook"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Runbooks) -> list:
    import aws_sdk_ssm.types.runbook

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.runbook.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Runbooks:
    import aws_sdk_ssm.types.runbook

    out: Runbooks = []
    for item in data:
        out.append(aws_sdk_ssm.types.runbook.deserialize_aws_json_1_1(item))
    return out
