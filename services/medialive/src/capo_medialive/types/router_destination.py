"""Generated from Smithy shape ``com.amazonaws.medialive#RouterDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class RouterDestination(TypedDict, closed=True):
    availability_zone_name: NotRequired["capo_medialive.types.__string.__string"]
    """The Availability Zone (AZ) names of the AZs this destination is created in."""
    router_output_arn: NotRequired["capo_medialive.types.__string.__string"]
    """ARN of the output from MediaConnect Router currently connected to this input."""


# --- restJson1 ser/de ---
def serialize_json(value: RouterDestination) -> dict:
    out: dict = {}
    if "availability_zone_name" in value:
        out["availabilityZoneName"] = value["availability_zone_name"]
    if "router_output_arn" in value:
        out["routerOutputArn"] = value["router_output_arn"]
    return out


def deserialize_json(data: dict) -> RouterDestination:
    out: RouterDestination = {}  # type: ignore[typeddict-item]
    if "availabilityZoneName" in data:
        out["availability_zone_name"] = data["availabilityZoneName"]
    if "routerOutputArn" in data:
        out["router_output_arn"] = data["routerOutputArn"]
    return out
