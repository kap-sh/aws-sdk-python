"""Generated from Smithy shape ``com.amazonaws.ssmsap#ConfigurationCheckTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm_sap.types.configuration_check_type

ConfigurationCheckTypeList: TypeAlias = list[
    "capo_ssm_sap.types.configuration_check_type.ConfigurationCheckType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationCheckTypeList) -> list:
    import capo_ssm_sap.types.configuration_check_type

    out: list = []
    for item in value:
        out.append(capo_ssm_sap.types.configuration_check_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConfigurationCheckTypeList:
    import capo_ssm_sap.types.configuration_check_type

    out: ConfigurationCheckTypeList = []
    for item in data:
        out.append(capo_ssm_sap.types.configuration_check_type.deserialize_json(item))
    return out
