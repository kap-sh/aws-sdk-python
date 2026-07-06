"""Generated from Smithy shape ``com.amazonaws.devopsagent#AWSConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.monitor_account_type
    import aws_sdk_devops_agent.types.role_arn


class AWSConfiguration(TypedDict, closed=True):
    assumable_role_arn: "aws_sdk_devops_agent.types.role_arn.RoleArn"
    """<p>Role ARN to be assumed by AIDevOps to operate on behalf of customer.</p>"""
    account_id: "str"
    """<p>AWS Account Id corresponding to provided resources.</p>"""
    account_type: "aws_sdk_devops_agent.types.monitor_account_type.MonitorAccountType"
    """<p>Account Type 'monitor' for AIDevOps monitoring.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AWSConfiguration) -> dict:
    out: dict = {}
    out["assumableRoleArn"] = value["assumable_role_arn"]
    out["accountId"] = value["account_id"]
    import aws_sdk_devops_agent.types.monitor_account_type

    out["accountType"] = aws_sdk_devops_agent.types.monitor_account_type.serialize_json(
        value["account_type"]
    )
    return out


def deserialize_json(data: dict) -> AWSConfiguration:
    out: AWSConfiguration = {}  # type: ignore[typeddict-item]
    if "assumableRoleArn" in data:
        out["assumable_role_arn"] = data["assumableRoleArn"]
    else:
        raise DeserializationError("AWSConfiguration.assumable_role_arn required")
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError("AWSConfiguration.account_id required")
    if "accountType" in data:
        import aws_sdk_devops_agent.types.monitor_account_type

        out["account_type"] = (
            aws_sdk_devops_agent.types.monitor_account_type.deserialize_json(
                data["accountType"]
            )
        )
    else:
        raise DeserializationError("AWSConfiguration.account_type required")
    return out
