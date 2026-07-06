"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetNetworkAnalyzerConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.network_analyzer_configuration_name


class GetNetworkAnalyzerConfigurationRequest(TypedDict, closed=True):
    configuration_name: "aws_sdk_iot_wireless.types.network_analyzer_configuration_name.NetworkAnalyzerConfigurationName"


# --- restJson1 ser/de ---
def serialize_json(value: GetNetworkAnalyzerConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetNetworkAnalyzerConfigurationRequest:
    out: GetNetworkAnalyzerConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
