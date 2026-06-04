"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceConnectTestTrafficHeaderRules``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service_connect_test_traffic_header_match_rules
    import aws_sdk_ecs.types.string


class ServiceConnectTestTrafficHeaderRules(TypedDict):
    name: "aws_sdk_ecs.types.string.String"
    """<p>The name of the HTTP header to examine for test traffic routing. Common examples include custom headers like <code>X-Test-Version</code> or <code>X-Canary-Request</code> that can be used to identify test traffic.</p>"""
    value: NotRequired[
        "aws_sdk_ecs.types.service_connect_test_traffic_header_match_rules.ServiceConnectTestTrafficHeaderMatchRules"
    ]
    """<p>The header value matching configuration that determines how the HTTP header value is evaluated for test traffic routing decisions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceConnectTestTrafficHeaderRules) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "value" in value:
        import aws_sdk_ecs.types.service_connect_test_traffic_header_match_rules

        out["value"] = (
            aws_sdk_ecs.types.service_connect_test_traffic_header_match_rules.serialize_aws_json_1_1(
                value["value"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceConnectTestTrafficHeaderRules:
    out: ServiceConnectTestTrafficHeaderRules = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ServiceConnectTestTrafficHeaderRules.name required")
    if "value" in data:
        import aws_sdk_ecs.types.service_connect_test_traffic_header_match_rules

        out["value"] = (
            aws_sdk_ecs.types.service_connect_test_traffic_header_match_rules.deserialize_aws_json_1_1(
                data["value"]
            )
        )
    return out
