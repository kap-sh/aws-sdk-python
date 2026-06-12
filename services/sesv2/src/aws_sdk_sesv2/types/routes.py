"""Generated from Smithy shape ``com.amazonaws.sesv2#Routes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.route

Routes: TypeAlias = list["aws_sdk_sesv2.types.route.Route"]


# --- restJson1 ser/de ---
def serialize_json(value: Routes) -> list:
    import aws_sdk_sesv2.types.route

    out: list = []
    for item in value:
        out.append(aws_sdk_sesv2.types.route.serialize_json(item))
    return out


def deserialize_json(data: list) -> Routes:
    import aws_sdk_sesv2.types.route

    out: Routes = []
    for item in data:
        out.append(aws_sdk_sesv2.types.route.deserialize_json(item))
    return out
