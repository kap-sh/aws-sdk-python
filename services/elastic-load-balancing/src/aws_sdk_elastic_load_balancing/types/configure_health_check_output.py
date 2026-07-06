"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#ConfigureHealthCheckOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing.types.health_check


class ConfigureHealthCheckOutput(TypedDict, closed=True):
    health_check: NotRequired[
        "aws_sdk_elastic_load_balancing.types.health_check.HealthCheck"
    ]
    """<p>The updated health check.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ConfigureHealthCheckOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "health_check" in value:
        import aws_sdk_elastic_load_balancing.types.health_check

        aws_sdk_elastic_load_balancing.types.health_check.serialize_query(
            value["health_check"], pairs, f"{prefix}.HealthCheck"
        )


def deserialize_query(el: Element) -> ConfigureHealthCheckOutput:
    out: ConfigureHealthCheckOutput = {}  # type: ignore[typeddict-item]
    child_health_check = el.find("HealthCheck")
    if child_health_check is not None:
        import aws_sdk_elastic_load_balancing.types.health_check

        out["health_check"] = (
            aws_sdk_elastic_load_balancing.types.health_check.deserialize_query(
                child_health_check
            )
        )
    return out
