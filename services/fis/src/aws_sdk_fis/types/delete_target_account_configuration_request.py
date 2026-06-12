"""Generated from Smithy shape ``com.amazonaws.fis#DeleteTargetAccountConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_template_id
    import aws_sdk_fis.types.target_account_id


class DeleteTargetAccountConfigurationRequest(TypedDict):
    experiment_template_id: (
        "aws_sdk_fis.types.experiment_template_id.ExperimentTemplateId"
    )
    """<p>The ID of the experiment template.</p>"""
    account_id: "aws_sdk_fis.types.target_account_id.TargetAccountId"
    """<p>The Amazon Web Services account ID of the target account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTargetAccountConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTargetAccountConfigurationRequest:
    out: DeleteTargetAccountConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
