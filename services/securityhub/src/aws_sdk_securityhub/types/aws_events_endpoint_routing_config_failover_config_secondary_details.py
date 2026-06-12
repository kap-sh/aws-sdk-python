"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEventsEndpointRoutingConfigFailoverConfigSecondaryDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEventsEndpointRoutingConfigFailoverConfigSecondaryDetails(TypedDict):
    route: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> Defines the secondary Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEventsEndpointRoutingConfigFailoverConfigSecondaryDetails,
) -> dict:
    out: dict = {}
    if "route" in value:
        out["Route"] = value["route"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEventsEndpointRoutingConfigFailoverConfigSecondaryDetails:
    out: AwsEventsEndpointRoutingConfigFailoverConfigSecondaryDetails = {}  # type: ignore[typeddict-item]
    if "Route" in data:
        out["route"] = data["Route"]
    return out
