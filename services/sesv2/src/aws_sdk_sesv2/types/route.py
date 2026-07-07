"""Generated from Smithy shape ``com.amazonaws.sesv2#Route``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.region


class Route(TypedDict, closed=True):
    region: "aws_sdk_sesv2.types.region.Region"
    """<p>The name of an AWS-Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Route) -> dict:
    out: dict = {}
    out["Region"] = value["region"]
    return out


def deserialize_json(data: dict) -> Route:
    out: Route = {}  # type: ignore[typeddict-item]
    if "Region" in data:
        out["region"] = data["Region"]
    else:
        raise DeserializationError("Route.region required")
    return out
