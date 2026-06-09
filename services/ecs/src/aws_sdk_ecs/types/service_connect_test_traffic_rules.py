"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceConnectTestTrafficRules``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service_connect_test_traffic_header_rules


class ServiceConnectTestTrafficRules(TypedDict):
    header: "aws_sdk_ecs.types.service_connect_test_traffic_header_rules.ServiceConnectTestTrafficHeaderRules"
    """<p>The HTTP header-based routing rules that determine which requests should be routed to the new service version during blue/green deployment testing. These rules provide fine-grained control over test traffic routing based on request headers.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceConnectTestTrafficRules) -> dict:
    out: dict = {}
    import aws_sdk_ecs.types.service_connect_test_traffic_header_rules

    out["header"] = (
        aws_sdk_ecs.types.service_connect_test_traffic_header_rules.serialize_aws_json_1_1(
            value["header"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceConnectTestTrafficRules:
    out: ServiceConnectTestTrafficRules = {}  # type: ignore[typeddict-item]
    if "header" in data:
        import aws_sdk_ecs.types.service_connect_test_traffic_header_rules

        out["header"] = (
            aws_sdk_ecs.types.service_connect_test_traffic_header_rules.deserialize_aws_json_1_1(
                data["header"]
            )
        )
    else:
        raise DeserializationError("ServiceConnectTestTrafficRules.header required")
    return out
