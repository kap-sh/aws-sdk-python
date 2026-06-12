"""Generated from Smithy shape ``com.amazonaws.iotwireless#ListPositionConfigurationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_wireless.types.next_token
    import aws_sdk_iot_wireless.types.position_configuration_list


class ListPositionConfigurationsResponse(TypedDict):
    position_configuration_list: NotRequired[
        "aws_sdk_iot_wireless.types.position_configuration_list.PositionConfigurationList"
    ]
    """<p>A list of position configurations.</p>"""
    next_token: NotRequired["aws_sdk_iot_wireless.types.next_token.NextToken"]
    """<p>The token to use to get the next set of results, or <b>null</b> if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPositionConfigurationsResponse) -> dict:
    out: dict = {}
    if "position_configuration_list" in value:
        import aws_sdk_iot_wireless.types.position_configuration_list

        out["PositionConfigurationList"] = (
            aws_sdk_iot_wireless.types.position_configuration_list.serialize_json(
                value["position_configuration_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPositionConfigurationsResponse:
    out: ListPositionConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if "PositionConfigurationList" in data:
        import aws_sdk_iot_wireless.types.position_configuration_list

        out["position_configuration_list"] = (
            aws_sdk_iot_wireless.types.position_configuration_list.deserialize_json(
                data["PositionConfigurationList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
