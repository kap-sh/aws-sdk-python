"""Generated from Smithy shape ``com.amazonaws.devopsagent#SourceAwsConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.role_arn
    import aws_sdk_devops_agent.types.source_account_type


class SourceAwsConfiguration(TypedDict):
    account_id: "str"
    """<p>AWS Account Id corresponding to provided resources.</p>"""
    account_type: "aws_sdk_devops_agent.types.source_account_type.SourceAccountType"
    """<p>Account Type 'source' for AIDevOps monitoring.</p>"""
    assumable_role_arn: "aws_sdk_devops_agent.types.role_arn.RoleArn"
    """<p>Role ARN to be assumed by AIDevOps to operate on behalf of customer.</p>"""
    external_id: NotRequired["str"]
    """<p>External ID for additional security when assuming the role. Used to prevent the confused deputy problem.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceAwsConfiguration) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    import aws_sdk_devops_agent.types.source_account_type

    out["accountType"] = aws_sdk_devops_agent.types.source_account_type.serialize_json(
        value["account_type"]
    )
    out["assumableRoleArn"] = value["assumable_role_arn"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    return out


def deserialize_json(data: dict) -> SourceAwsConfiguration:
    out: SourceAwsConfiguration = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError("SourceAwsConfiguration.account_id required")
    if "accountType" in data:
        import aws_sdk_devops_agent.types.source_account_type

        out["account_type"] = (
            aws_sdk_devops_agent.types.source_account_type.deserialize_json(
                data["accountType"]
            )
        )
    else:
        raise DeserializationError("SourceAwsConfiguration.account_type required")
    if "assumableRoleArn" in data:
        out["assumable_role_arn"] = data["assumableRoleArn"]
    else:
        raise DeserializationError("SourceAwsConfiguration.assumable_role_arn required")
    if "externalId" in data:
        out["external_id"] = data["externalId"]
    return out
