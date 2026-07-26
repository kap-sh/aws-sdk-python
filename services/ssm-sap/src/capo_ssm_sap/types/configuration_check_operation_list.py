"""Generated from Smithy shape ``com.amazonaws.ssmsap#ConfigurationCheckOperationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm_sap.types.configuration_check_operation

ConfigurationCheckOperationList: TypeAlias = list[
    "capo_ssm_sap.types.configuration_check_operation.ConfigurationCheckOperation"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationCheckOperationList) -> list:
    import capo_ssm_sap.types.configuration_check_operation

    out: list = []
    for item in value:
        out.append(
            capo_ssm_sap.types.configuration_check_operation.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ConfigurationCheckOperationList:
    import capo_ssm_sap.types.configuration_check_operation

    out: ConfigurationCheckOperationList = []
    for item in data:
        out.append(
            capo_ssm_sap.types.configuration_check_operation.deserialize_json(item)
        )
    return out
