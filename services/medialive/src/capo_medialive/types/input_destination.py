"""Generated from Smithy shape ``com.amazonaws.medialive#InputDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of_input_destination_route
    import capo_medialive.types.__string
    import capo_medialive.types.input_destination_vpc


class InputDestination(TypedDict, closed=True):
    ip: NotRequired["capo_medialive.types.__string.__string"]
    """The system-generated static IP address of endpoint. It remains fixed for the lifetime of the input."""
    port: NotRequired["capo_medialive.types.__string.__string"]
    """The port number for the input."""
    url: NotRequired["capo_medialive.types.__string.__string"]
    """This represents the endpoint that the customer stream will be pushed to."""
    vpc: NotRequired["capo_medialive.types.input_destination_vpc.InputDestinationVpc"]
    network: NotRequired["capo_medialive.types.__string.__string"]
    """The ID of the attached network."""
    network_routes: NotRequired[
        "capo_medialive.types.__list_of_input_destination_route.__listOfInputDestinationRoute"
    ]
    """If the push input has an input location of ON-PREM it's a requirement to specify what the route of the input is going to be on the customer local network."""


# --- restJson1 ser/de ---
def serialize_json(value: InputDestination) -> dict:
    out: dict = {}
    if "ip" in value:
        out["ip"] = value["ip"]
    if "port" in value:
        out["port"] = value["port"]
    if "url" in value:
        out["url"] = value["url"]
    if "vpc" in value:
        import capo_medialive.types.input_destination_vpc

        out["vpc"] = capo_medialive.types.input_destination_vpc.serialize_json(
            value["vpc"]
        )
    if "network" in value:
        out["network"] = value["network"]
    if "network_routes" in value:
        import capo_medialive.types.__list_of_input_destination_route

        out["networkRoutes"] = (
            capo_medialive.types.__list_of_input_destination_route.serialize_json(
                value["network_routes"]
            )
        )
    return out


def deserialize_json(data: dict) -> InputDestination:
    out: InputDestination = {}  # type: ignore[typeddict-item]
    if "ip" in data:
        out["ip"] = data["ip"]
    if "port" in data:
        out["port"] = data["port"]
    if "url" in data:
        out["url"] = data["url"]
    if "vpc" in data:
        import capo_medialive.types.input_destination_vpc

        out["vpc"] = capo_medialive.types.input_destination_vpc.deserialize_json(
            data["vpc"]
        )
    if "network" in data:
        out["network"] = data["network"]
    if "networkRoutes" in data:
        import capo_medialive.types.__list_of_input_destination_route

        out["network_routes"] = (
            capo_medialive.types.__list_of_input_destination_route.deserialize_json(
                data["networkRoutes"]
            )
        )
    return out
