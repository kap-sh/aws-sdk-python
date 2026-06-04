"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceConnectTestTrafficHeaderMatchRules``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class ServiceConnectTestTrafficHeaderMatchRules(TypedDict):
    exact: "aws_sdk_ecs.types.string.String"
    """<p>The exact value that the HTTP header must match for the test traffic routing rule to apply. This provides precise control over which requests are routed to the new service revision during blue/green deployments.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceConnectTestTrafficHeaderMatchRules) -> dict:
    out: dict = {}
    out["exact"] = value["exact"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceConnectTestTrafficHeaderMatchRules:
    out: ServiceConnectTestTrafficHeaderMatchRules = {}  # type: ignore[typeddict-item]
    if "exact" in data:
        out["exact"] = data["exact"]
    else:
        raise DeserializationError(
            "ServiceConnectTestTrafficHeaderMatchRules.exact required"
        )
    return out
