"""Generated from Smithy shape ``com.amazonaws.fis#UpdateTargetAccountConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.experiment_template_id
    import capo_fis.types.role_arn
    import capo_fis.types.target_account_configuration_description
    import capo_fis.types.target_account_id


class UpdateTargetAccountConfigurationRequest(TypedDict, closed=True):
    experiment_template_id: "capo_fis.types.experiment_template_id.ExperimentTemplateId"
    """<p>The ID of the experiment template.</p>"""
    account_id: "capo_fis.types.target_account_id.TargetAccountId"
    """<p>The Amazon Web Services account ID of the target account.</p>"""
    role_arn: NotRequired["capo_fis.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role for the target account.</p>"""
    description: NotRequired[
        "capo_fis.types.target_account_configuration_description.TargetAccountConfigurationDescription"
    ]
    """<p>The description of the target account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTargetAccountConfigurationRequest) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateTargetAccountConfigurationRequest:
    out: UpdateTargetAccountConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "description" in data:
        out["description"] = data["description"]
    return out
