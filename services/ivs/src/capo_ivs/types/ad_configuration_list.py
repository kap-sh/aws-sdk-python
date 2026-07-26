"""Generated from Smithy shape ``com.amazonaws.ivs#AdConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ivs.types.ad_configuration_summary

AdConfigurationList: TypeAlias = list[
    "capo_ivs.types.ad_configuration_summary.AdConfigurationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AdConfigurationList) -> list:
    import capo_ivs.types.ad_configuration_summary

    out: list = []
    for item in value:
        out.append(capo_ivs.types.ad_configuration_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AdConfigurationList:
    import capo_ivs.types.ad_configuration_summary

    out: AdConfigurationList = []
    for item in data:
        out.append(capo_ivs.types.ad_configuration_summary.deserialize_json(item))
    return out
