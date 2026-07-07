"""Generated from Smithy shape ``com.amazonaws.sesv2#Details``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.routes_details


class Details(TypedDict, closed=True):
    routes_details: "aws_sdk_sesv2.types.routes_details.RoutesDetails"
    """<p>A list of route configuration details. Must contain exactly one route configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Details) -> dict:
    out: dict = {}
    import aws_sdk_sesv2.types.routes_details

    out["RoutesDetails"] = aws_sdk_sesv2.types.routes_details.serialize_json(
        value["routes_details"]
    )
    return out


def deserialize_json(data: dict) -> Details:
    out: Details = {}  # type: ignore[typeddict-item]
    if "RoutesDetails" in data:
        import aws_sdk_sesv2.types.routes_details

        out["routes_details"] = aws_sdk_sesv2.types.routes_details.deserialize_json(
            data["RoutesDetails"]
        )
    else:
        raise DeserializationError("Details.routes_details required")
    return out
