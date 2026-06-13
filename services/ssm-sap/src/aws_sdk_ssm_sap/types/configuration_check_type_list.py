"""Generated from Smithy shape ``com.amazonaws.ssmsap#ConfigurationCheckTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.configuration_check_type

ConfigurationCheckTypeList: TypeAlias = list[
    "aws_sdk_ssm_sap.types.configuration_check_type.ConfigurationCheckType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationCheckTypeList) -> list:
    import aws_sdk_ssm_sap.types.configuration_check_type

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm_sap.types.configuration_check_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConfigurationCheckTypeList:
    import aws_sdk_ssm_sap.types.configuration_check_type

    out: ConfigurationCheckTypeList = []
    for item in data:
        out.append(
            aws_sdk_ssm_sap.types.configuration_check_type.deserialize_json(item)
        )
    return out
