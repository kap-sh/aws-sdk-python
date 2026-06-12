"""Generated from Smithy shape ``com.amazonaws.fis#GetExperimentTargetAccountConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_target_account_configuration


class GetExperimentTargetAccountConfigurationResponse(TypedDict):
    target_account_configuration: NotRequired[
        "aws_sdk_fis.types.experiment_target_account_configuration.ExperimentTargetAccountConfiguration"
    ]
    """<p>Information about the target account configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetExperimentTargetAccountConfigurationResponse) -> dict:
    out: dict = {}
    if "target_account_configuration" in value:
        import aws_sdk_fis.types.experiment_target_account_configuration

        out["targetAccountConfiguration"] = (
            aws_sdk_fis.types.experiment_target_account_configuration.serialize_json(
                value["target_account_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetExperimentTargetAccountConfigurationResponse:
    out: GetExperimentTargetAccountConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "targetAccountConfiguration" in data:
        import aws_sdk_fis.types.experiment_target_account_configuration

        out["target_account_configuration"] = (
            aws_sdk_fis.types.experiment_target_account_configuration.deserialize_json(
                data["targetAccountConfiguration"]
            )
        )
    return out
