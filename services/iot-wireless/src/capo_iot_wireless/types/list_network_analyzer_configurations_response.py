"""Generated from Smithy shape ``com.amazonaws.iotwireless#ListNetworkAnalyzerConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.network_analyzer_configuration_list
    import capo_iot_wireless.types.next_token


class ListNetworkAnalyzerConfigurationsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_iot_wireless.types.next_token.NextToken"]
    """<p>The token to use to get the next set of results, or <b>null</b> if there are no additional results.</p>"""
    network_analyzer_configuration_list: NotRequired[
        "capo_iot_wireless.types.network_analyzer_configuration_list.NetworkAnalyzerConfigurationList"
    ]
    """<p>The list of network analyzer configurations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworkAnalyzerConfigurationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "network_analyzer_configuration_list" in value:
        import capo_iot_wireless.types.network_analyzer_configuration_list

        out["NetworkAnalyzerConfigurationList"] = (
            capo_iot_wireless.types.network_analyzer_configuration_list.serialize_json(
                value["network_analyzer_configuration_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListNetworkAnalyzerConfigurationsResponse:
    out: ListNetworkAnalyzerConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "NetworkAnalyzerConfigurationList" in data:
        import capo_iot_wireless.types.network_analyzer_configuration_list

        out["network_analyzer_configuration_list"] = (
            capo_iot_wireless.types.network_analyzer_configuration_list.deserialize_json(
                data["NetworkAnalyzerConfigurationList"]
            )
        )
    return out
