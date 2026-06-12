"""Generated from Smithy shape ``com.amazonaws.iotwireless#DeleteNetworkAnalyzerConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.network_analyzer_configuration_name


class DeleteNetworkAnalyzerConfigurationRequest(TypedDict):
    configuration_name: "aws_sdk_iot_wireless.types.network_analyzer_configuration_name.NetworkAnalyzerConfigurationName"


# --- restJson1 ser/de ---
def serialize_json(value: DeleteNetworkAnalyzerConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteNetworkAnalyzerConfigurationRequest:
    out: DeleteNetworkAnalyzerConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
