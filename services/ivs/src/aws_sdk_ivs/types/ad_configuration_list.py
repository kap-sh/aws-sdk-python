"""Generated from Smithy shape ``com.amazonaws.ivs#AdConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivs.types.ad_configuration_summary

AdConfigurationList: TypeAlias = list[
    "aws_sdk_ivs.types.ad_configuration_summary.AdConfigurationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AdConfigurationList) -> list:
    import aws_sdk_ivs.types.ad_configuration_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_ivs.types.ad_configuration_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AdConfigurationList:
    import aws_sdk_ivs.types.ad_configuration_summary

    out: AdConfigurationList = []
    for item in data:
        out.append(aws_sdk_ivs.types.ad_configuration_summary.deserialize_json(item))
    return out
