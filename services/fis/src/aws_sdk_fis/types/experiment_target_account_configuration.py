"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentTargetAccountConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fis.types.role_arn
    import aws_sdk_fis.types.target_account_configuration_description
    import aws_sdk_fis.types.target_account_id


class ExperimentTargetAccountConfiguration(TypedDict, closed=True):
    role_arn: NotRequired["aws_sdk_fis.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role for the target account.</p>"""
    account_id: NotRequired["aws_sdk_fis.types.target_account_id.TargetAccountId"]
    """<p>The Amazon Web Services account ID of the target account.</p>"""
    description: NotRequired[
        "aws_sdk_fis.types.target_account_configuration_description.TargetAccountConfigurationDescription"
    ]
    """<p>The description of the target account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentTargetAccountConfiguration) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> ExperimentTargetAccountConfiguration:
    out: ExperimentTargetAccountConfiguration = {}  # type: ignore[typeddict-item]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "description" in data:
        out["description"] = data["description"]
    return out
