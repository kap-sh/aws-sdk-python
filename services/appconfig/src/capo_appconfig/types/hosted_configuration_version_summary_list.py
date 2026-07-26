"""Generated from Smithy shape ``com.amazonaws.appconfig#HostedConfigurationVersionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appconfig.types.hosted_configuration_version_summary

HostedConfigurationVersionSummaryList: TypeAlias = list[
    "capo_appconfig.types.hosted_configuration_version_summary.HostedConfigurationVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: HostedConfigurationVersionSummaryList) -> list:
    import capo_appconfig.types.hosted_configuration_version_summary

    out: list = []
    for item in value:
        out.append(
            capo_appconfig.types.hosted_configuration_version_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> HostedConfigurationVersionSummaryList:
    import capo_appconfig.types.hosted_configuration_version_summary

    out: HostedConfigurationVersionSummaryList = []
    for item in data:
        out.append(
            capo_appconfig.types.hosted_configuration_version_summary.deserialize_json(
                item
            )
        )
    return out
