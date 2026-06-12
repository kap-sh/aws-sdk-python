"""Generated from Smithy shape ``com.amazonaws.fis#GetTargetAccountConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_template_id
    import aws_sdk_fis.types.target_account_id


class GetTargetAccountConfigurationRequest(TypedDict):
    experiment_template_id: (
        "aws_sdk_fis.types.experiment_template_id.ExperimentTemplateId"
    )
    """<p>The ID of the experiment template.</p>"""
    account_id: "aws_sdk_fis.types.target_account_id.TargetAccountId"
    """<p>The Amazon Web Services account ID of the target account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTargetAccountConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTargetAccountConfigurationRequest:
    out: GetTargetAccountConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
