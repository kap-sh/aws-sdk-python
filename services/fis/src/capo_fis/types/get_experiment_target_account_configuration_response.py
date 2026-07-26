"""Generated from Smithy shape ``com.amazonaws.fis#GetExperimentTargetAccountConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.experiment_target_account_configuration


class GetExperimentTargetAccountConfigurationResponse(TypedDict, closed=True):
    target_account_configuration: NotRequired[
        "capo_fis.types.experiment_target_account_configuration.ExperimentTargetAccountConfiguration"
    ]
    """<p>Information about the target account configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetExperimentTargetAccountConfigurationResponse) -> dict:
    out: dict = {}
    if "target_account_configuration" in value:
        import capo_fis.types.experiment_target_account_configuration

        out["targetAccountConfiguration"] = (
            capo_fis.types.experiment_target_account_configuration.serialize_json(
                value["target_account_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetExperimentTargetAccountConfigurationResponse:
    out: GetExperimentTargetAccountConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "targetAccountConfiguration" in data:
        import capo_fis.types.experiment_target_account_configuration

        out["target_account_configuration"] = (
            capo_fis.types.experiment_target_account_configuration.deserialize_json(
                data["targetAccountConfiguration"]
            )
        )
    return out
