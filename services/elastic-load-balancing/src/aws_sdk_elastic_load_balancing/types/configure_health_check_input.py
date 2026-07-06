"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#ConfigureHealthCheckInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_elastic_load_balancing._protocol.xml import Element
from aws_sdk_elastic_load_balancing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.access_point_name
    import aws_sdk_elastic_load_balancing.types.health_check


class ConfigureHealthCheckInput(TypedDict, closed=True):
    load_balancer_name: (
        "aws_sdk_elastic_load_balancing.types.access_point_name.AccessPointName"
    )
    """<p>The name of the load balancer.</p>"""
    health_check: "aws_sdk_elastic_load_balancing.types.health_check.HealthCheck"
    """<p>The configuration information.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ConfigureHealthCheckInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.LoadBalancerName", str(value["load_balancer_name"])))
    import aws_sdk_elastic_load_balancing.types.health_check

    aws_sdk_elastic_load_balancing.types.health_check.serialize_query(
        value["health_check"], pairs, f"{prefix}.HealthCheck"
    )


def deserialize_query(el: Element) -> ConfigureHealthCheckInput:
    out: ConfigureHealthCheckInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_name = el.find("LoadBalancerName")
    if child_load_balancer_name is not None:
        out["load_balancer_name"] = str(child_load_balancer_name.text or "")
    else:
        raise DeserializationError(
            "ConfigureHealthCheckInput.load_balancer_name required"
        )
    child_health_check = el.find("HealthCheck")
    if child_health_check is not None:
        import aws_sdk_elastic_load_balancing.types.health_check

        out["health_check"] = (
            aws_sdk_elastic_load_balancing.types.health_check.deserialize_query(
                child_health_check
            )
        )
    else:
        raise DeserializationError("ConfigureHealthCheckInput.health_check required")
    return out
