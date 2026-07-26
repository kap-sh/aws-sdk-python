"""Generated from Smithy shape ``com.amazonaws.fis#TargetAccountConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fis.types.target_account_configuration_summary

TargetAccountConfigurationList: TypeAlias = list[
    "capo_fis.types.target_account_configuration_summary.TargetAccountConfigurationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetAccountConfigurationList) -> list:
    import capo_fis.types.target_account_configuration_summary

    out: list = []
    for item in value:
        out.append(
            capo_fis.types.target_account_configuration_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TargetAccountConfigurationList:
    import capo_fis.types.target_account_configuration_summary

    out: TargetAccountConfigurationList = []
    for item in data:
        out.append(
            capo_fis.types.target_account_configuration_summary.deserialize_json(item)
        )
    return out
