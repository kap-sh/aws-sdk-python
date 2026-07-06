"""Generated from Smithy shape ``com.amazonaws.fis#GetExperimentTargetAccountConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_id
    import aws_sdk_fis.types.target_account_id


class GetExperimentTargetAccountConfigurationRequest(TypedDict, closed=True):
    experiment_id: "aws_sdk_fis.types.experiment_id.ExperimentId"
    """<p>The ID of the experiment.</p>"""
    account_id: "aws_sdk_fis.types.target_account_id.TargetAccountId"
    """<p>The Amazon Web Services account ID of the target account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetExperimentTargetAccountConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetExperimentTargetAccountConfigurationRequest:
    out: GetExperimentTargetAccountConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
