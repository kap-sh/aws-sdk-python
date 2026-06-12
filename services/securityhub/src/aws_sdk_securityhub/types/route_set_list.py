"""Generated from Smithy shape ``com.amazonaws.securityhub#RouteSetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.route_set_details

RouteSetList: TypeAlias = list[
    "aws_sdk_securityhub.types.route_set_details.RouteSetDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteSetList) -> list:
    import aws_sdk_securityhub.types.route_set_details

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.route_set_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteSetList:
    import aws_sdk_securityhub.types.route_set_details

    out: RouteSetList = []
    for item in data:
        out.append(aws_sdk_securityhub.types.route_set_details.deserialize_json(item))
    return out
