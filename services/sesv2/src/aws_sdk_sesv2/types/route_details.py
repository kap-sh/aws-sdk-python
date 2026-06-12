"""Generated from Smithy shape ``com.amazonaws.sesv2#RouteDetails``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.region


class RouteDetails(TypedDict):
    region: "aws_sdk_sesv2.types.region.Region"
    """<p>The name of an AWS-Region to be a secondary region for the multi-region endpoint (global-endpoint).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteDetails) -> dict:
    out: dict = {}
    out["Region"] = value["region"]
    return out


def deserialize_json(data: dict) -> RouteDetails:
    out: RouteDetails = {}  # type: ignore[typeddict-item]
    if "Region" in data:
        out["region"] = data["Region"]
    else:
        raise DeserializationError("RouteDetails.region required")
    return out
