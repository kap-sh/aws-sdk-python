"""Generated from Smithy shape ``com.amazonaws.iotwireless#DeleteNetworkAnalyzerConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.network_analyzer_configuration_name


class DeleteNetworkAnalyzerConfigurationRequest(TypedDict, closed=True):
    configuration_name: "capo_iot_wireless.types.network_analyzer_configuration_name.NetworkAnalyzerConfigurationName"


# --- restJson1 ser/de ---
def serialize_json(value: DeleteNetworkAnalyzerConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteNetworkAnalyzerConfigurationRequest:
    out: DeleteNetworkAnalyzerConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
