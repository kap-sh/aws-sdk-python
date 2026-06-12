"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#ConfigurationManagerList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_ssm_quicksetup.types.configuration_manager_summary

ConfigurationManagerList: TypeAlias = list["aws_sdk_ssm_quicksetup.types.configuration_manager_summary.ConfigurationManagerSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationManagerList) -> list:
    import aws_sdk_ssm_quicksetup.types.configuration_manager_summary
    out: list = []
    for item in value:
        out.append(aws_sdk_ssm_quicksetup.types.configuration_manager_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConfigurationManagerList:
    import aws_sdk_ssm_quicksetup.types.configuration_manager_summary
    out: ConfigurationManagerList = []
    for item in data:
        out.append(aws_sdk_ssm_quicksetup.types.configuration_manager_summary.deserialize_json(item))
    return out