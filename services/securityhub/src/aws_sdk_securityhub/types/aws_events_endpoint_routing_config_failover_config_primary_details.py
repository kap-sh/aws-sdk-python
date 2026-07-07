"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEventsEndpointRoutingConfigFailoverConfigPrimaryDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEventsEndpointRoutingConfigFailoverConfigPrimaryDetails(
    TypedDict, closed=True
):
    health_check: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The Amazon Resource Name (ARN) of the health check used by the endpoint to determine whether failover is triggered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEventsEndpointRoutingConfigFailoverConfigPrimaryDetails,
) -> dict:
    out: dict = {}
    if "health_check" in value:
        out["HealthCheck"] = value["health_check"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEventsEndpointRoutingConfigFailoverConfigPrimaryDetails:
    out: AwsEventsEndpointRoutingConfigFailoverConfigPrimaryDetails = {}  # type: ignore[typeddict-item]
    if "HealthCheck" in data:
        out["health_check"] = data["HealthCheck"]
    return out
