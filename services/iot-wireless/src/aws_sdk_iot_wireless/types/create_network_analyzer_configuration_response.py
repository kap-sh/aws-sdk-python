"""Generated from Smithy shape ``com.amazonaws.iotwireless#CreateNetworkAnalyzerConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.network_analyzer_configuration_arn
    import aws_sdk_iot_wireless.types.network_analyzer_configuration_name


class CreateNetworkAnalyzerConfigurationResponse(TypedDict, closed=True):
    arn: NotRequired[
        "aws_sdk_iot_wireless.types.network_analyzer_configuration_arn.NetworkAnalyzerConfigurationArn"
    ]
    """<p>The Amazon Resource Name of the new resource.</p>"""
    name: NotRequired[
        "aws_sdk_iot_wireless.types.network_analyzer_configuration_name.NetworkAnalyzerConfigurationName"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CreateNetworkAnalyzerConfigurationResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> CreateNetworkAnalyzerConfigurationResponse:
    out: CreateNetworkAnalyzerConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
