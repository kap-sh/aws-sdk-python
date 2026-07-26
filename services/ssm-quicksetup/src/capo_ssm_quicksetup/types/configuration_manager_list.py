"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#ConfigurationManagerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm_quicksetup.types.configuration_manager_summary

ConfigurationManagerList: TypeAlias = list[
    "capo_ssm_quicksetup.types.configuration_manager_summary.ConfigurationManagerSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationManagerList) -> list:
    import capo_ssm_quicksetup.types.configuration_manager_summary

    out: list = []
    for item in value:
        out.append(
            capo_ssm_quicksetup.types.configuration_manager_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ConfigurationManagerList:
    import capo_ssm_quicksetup.types.configuration_manager_summary

    out: ConfigurationManagerList = []
    for item in data:
        out.append(
            capo_ssm_quicksetup.types.configuration_manager_summary.deserialize_json(
                item
            )
        )
    return out
