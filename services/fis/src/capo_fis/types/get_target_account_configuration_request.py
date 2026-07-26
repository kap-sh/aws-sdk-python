"""Generated from Smithy shape ``com.amazonaws.fis#GetTargetAccountConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_fis.types.experiment_template_id
    import capo_fis.types.target_account_id


class GetTargetAccountConfigurationRequest(TypedDict, closed=True):
    experiment_template_id: "capo_fis.types.experiment_template_id.ExperimentTemplateId"
    """<p>The ID of the experiment template.</p>"""
    account_id: "capo_fis.types.target_account_id.TargetAccountId"
    """<p>The Amazon Web Services account ID of the target account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTargetAccountConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetTargetAccountConfigurationRequest:
    out: GetTargetAccountConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
