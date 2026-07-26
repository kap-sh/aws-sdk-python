"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentTargetAccountConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fis.types.experiment_target_account_configuration_summary

ExperimentTargetAccountConfigurationList: TypeAlias = list[
    "capo_fis.types.experiment_target_account_configuration_summary.ExperimentTargetAccountConfigurationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentTargetAccountConfigurationList) -> list:
    import capo_fis.types.experiment_target_account_configuration_summary

    out: list = []
    for item in value:
        out.append(
            capo_fis.types.experiment_target_account_configuration_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ExperimentTargetAccountConfigurationList:
    import capo_fis.types.experiment_target_account_configuration_summary

    out: ExperimentTargetAccountConfigurationList = []
    for item in data:
        out.append(
            capo_fis.types.experiment_target_account_configuration_summary.deserialize_json(
                item
            )
        )
    return out
