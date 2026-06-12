"""Generated from Smithy shape ``com.amazonaws.sesv2#RoutesDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.route_details

RoutesDetails: TypeAlias = list["aws_sdk_sesv2.types.route_details.RouteDetails"]


# --- restJson1 ser/de ---
def serialize_json(value: RoutesDetails) -> list:
    import aws_sdk_sesv2.types.route_details

    out: list = []
    for item in value:
        out.append(aws_sdk_sesv2.types.route_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> RoutesDetails:
    import aws_sdk_sesv2.types.route_details

    out: RoutesDetails = []
    for item in data:
        out.append(aws_sdk_sesv2.types.route_details.deserialize_json(item))
    return out
