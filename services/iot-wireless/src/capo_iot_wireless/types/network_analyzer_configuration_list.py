"""Generated from Smithy shape ``com.amazonaws.iotwireless#NetworkAnalyzerConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.network_analyzer_configurations

NetworkAnalyzerConfigurationList: TypeAlias = list[
    "capo_iot_wireless.types.network_analyzer_configurations.NetworkAnalyzerConfigurations"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkAnalyzerConfigurationList) -> list:
    import capo_iot_wireless.types.network_analyzer_configurations

    out: list = []
    for item in value:
        out.append(
            capo_iot_wireless.types.network_analyzer_configurations.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> NetworkAnalyzerConfigurationList:
    import capo_iot_wireless.types.network_analyzer_configurations

    out: NetworkAnalyzerConfigurationList = []
    for item in data:
        out.append(
            capo_iot_wireless.types.network_analyzer_configurations.deserialize_json(
                item
            )
        )
    return out
