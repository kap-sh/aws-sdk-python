"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#ConfigurationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_quicksetup.types.configuration_summary

ConfigurationsList: TypeAlias = list[
    "aws_sdk_ssm_quicksetup.types.configuration_summary.ConfigurationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationsList) -> list:
    import aws_sdk_ssm_quicksetup.types.configuration_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm_quicksetup.types.configuration_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ConfigurationsList:
    import aws_sdk_ssm_quicksetup.types.configuration_summary

    out: ConfigurationsList = []
    for item in data:
        out.append(
            aws_sdk_ssm_quicksetup.types.configuration_summary.deserialize_json(item)
        )
    return out
