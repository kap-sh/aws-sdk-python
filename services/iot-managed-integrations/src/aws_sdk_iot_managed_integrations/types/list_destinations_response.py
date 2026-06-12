"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ListDestinationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_managed_integrations.types.destination_list_definition
    import aws_sdk_iot_managed_integrations.types.next_token


class ListDestinationsResponse(TypedDict):
    destination_list: NotRequired[
        "aws_sdk_iot_managed_integrations.types.destination_list_definition.DestinationListDefinition"
    ]
    """<p>The list of destinations.</p>"""
    next_token: NotRequired[
        "aws_sdk_iot_managed_integrations.types.next_token.NextToken"
    ]
    """<p>A token that can be used to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDestinationsResponse) -> dict:
    out: dict = {}
    if "destination_list" in value:
        import aws_sdk_iot_managed_integrations.types.destination_list_definition

        out["DestinationList"] = (
            aws_sdk_iot_managed_integrations.types.destination_list_definition.serialize_json(
                value["destination_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDestinationsResponse:
    out: ListDestinationsResponse = {}  # type: ignore[typeddict-item]
    if "DestinationList" in data:
        import aws_sdk_iot_managed_integrations.types.destination_list_definition

        out["destination_list"] = (
            aws_sdk_iot_managed_integrations.types.destination_list_definition.deserialize_json(
                data["DestinationList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
