"""Generated from Smithy shape ``com.amazonaws.appconfig#ConfigurationProfileSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.configuration_profile_summary

ConfigurationProfileSummaryList: TypeAlias = list[
    "aws_sdk_appconfig.types.configuration_profile_summary.ConfigurationProfileSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationProfileSummaryList) -> list:
    import aws_sdk_appconfig.types.configuration_profile_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_appconfig.types.configuration_profile_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ConfigurationProfileSummaryList:
    import aws_sdk_appconfig.types.configuration_profile_summary

    out: ConfigurationProfileSummaryList = []
    for item in data:
        out.append(
            aws_sdk_appconfig.types.configuration_profile_summary.deserialize_json(item)
        )
    return out
