"""Generated from Smithy shape ``com.amazonaws.medialive#InputDestinationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_input_request_destination_route
    import aws_sdk_medialive.types.__string


class InputDestinationRequest(TypedDict):
    stream_name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """A unique name for the location the RTMP stream is being pushed to."""
    network: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """If the push input has an input location of ON-PREM, ID the ID of the attached network."""
    network_routes: NotRequired[
        "aws_sdk_medialive.types.__list_of_input_request_destination_route.__listOfInputRequestDestinationRoute"
    ]
    """If the push input has an input location of ON-PREM it's a requirement to specify what the route of the input is going to be on the customer local network."""
    static_ip_address: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """If the push input has an input location of ON-PREM it's optional to specify what the ip address of the input is going to be on the customer local network."""


# --- restJson1 ser/de ---
def serialize_json(value: InputDestinationRequest) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["streamName"] = value["stream_name"]
    if "network" in value:
        out["network"] = value["network"]
    if "network_routes" in value:
        import aws_sdk_medialive.types.__list_of_input_request_destination_route

        out["networkRoutes"] = (
            aws_sdk_medialive.types.__list_of_input_request_destination_route.serialize_json(
                value["network_routes"]
            )
        )
    if "static_ip_address" in value:
        out["staticIpAddress"] = value["static_ip_address"]
    return out


def deserialize_json(data: dict) -> InputDestinationRequest:
    out: InputDestinationRequest = {}  # type: ignore[typeddict-item]
    if "streamName" in data:
        out["stream_name"] = data["streamName"]
    if "network" in data:
        out["network"] = data["network"]
    if "networkRoutes" in data:
        import aws_sdk_medialive.types.__list_of_input_request_destination_route

        out["network_routes"] = (
            aws_sdk_medialive.types.__list_of_input_request_destination_route.deserialize_json(
                data["networkRoutes"]
            )
        )
    if "staticIpAddress" in data:
        out["static_ip_address"] = data["staticIpAddress"]
    return out
