"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#TargetHealthDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.administrative_override
    import aws_sdk_elastic_load_balancing_v2.types.anomaly_detection
    import aws_sdk_elastic_load_balancing_v2.types.health_check_port
    import aws_sdk_elastic_load_balancing_v2.types.target_description
    import aws_sdk_elastic_load_balancing_v2.types.target_health


class TargetHealthDescription(TypedDict, closed=True):
    target: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.target_description.TargetDescription"
    ]
    """<p>The description of the target.</p>"""
    health_check_port: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.health_check_port.HealthCheckPort"
    ]
    """<p>The port to use to connect with the target.</p>"""
    target_health: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.target_health.TargetHealth"
    ]
    """<p>The health information for the target.</p>"""
    anomaly_detection: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.anomaly_detection.AnomalyDetection"
    ]
    """<p>The anomaly detection result for the target.</p> <p>If no anomalies were detected, the result is <code>normal</code>.</p> <p>If anomalies were detected, the result is <code>anomalous</code>.</p>"""
    administrative_override: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.administrative_override.AdministrativeOverride"
    ]
    """<p>The administrative override information for the target.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TargetHealthDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "target" in value:
        import aws_sdk_elastic_load_balancing_v2.types.target_description

        aws_sdk_elastic_load_balancing_v2.types.target_description.serialize_query(
            value["target"], pairs, f"{prefix}.Target"
        )
    if "health_check_port" in value:
        pairs.append((f"{prefix}.HealthCheckPort", str(value["health_check_port"])))
    if "target_health" in value:
        import aws_sdk_elastic_load_balancing_v2.types.target_health

        aws_sdk_elastic_load_balancing_v2.types.target_health.serialize_query(
            value["target_health"], pairs, f"{prefix}.TargetHealth"
        )
    if "anomaly_detection" in value:
        import aws_sdk_elastic_load_balancing_v2.types.anomaly_detection

        aws_sdk_elastic_load_balancing_v2.types.anomaly_detection.serialize_query(
            value["anomaly_detection"], pairs, f"{prefix}.AnomalyDetection"
        )
    if "administrative_override" in value:
        import aws_sdk_elastic_load_balancing_v2.types.administrative_override

        aws_sdk_elastic_load_balancing_v2.types.administrative_override.serialize_query(
            value["administrative_override"], pairs, f"{prefix}.AdministrativeOverride"
        )


def deserialize_query(el: Element) -> TargetHealthDescription:
    out: TargetHealthDescription = {}  # type: ignore[typeddict-item]
    child_target = el.find("Target")
    if child_target is not None:
        import aws_sdk_elastic_load_balancing_v2.types.target_description

        out["target"] = (
            aws_sdk_elastic_load_balancing_v2.types.target_description.deserialize_query(
                child_target
            )
        )
    child_health_check_port = el.find("HealthCheckPort")
    if child_health_check_port is not None:
        out["health_check_port"] = str(child_health_check_port.text or "")
    child_target_health = el.find("TargetHealth")
    if child_target_health is not None:
        import aws_sdk_elastic_load_balancing_v2.types.target_health

        out["target_health"] = (
            aws_sdk_elastic_load_balancing_v2.types.target_health.deserialize_query(
                child_target_health
            )
        )
    child_anomaly_detection = el.find("AnomalyDetection")
    if child_anomaly_detection is not None:
        import aws_sdk_elastic_load_balancing_v2.types.anomaly_detection

        out["anomaly_detection"] = (
            aws_sdk_elastic_load_balancing_v2.types.anomaly_detection.deserialize_query(
                child_anomaly_detection
            )
        )
    child_administrative_override = el.find("AdministrativeOverride")
    if child_administrative_override is not None:
        import aws_sdk_elastic_load_balancing_v2.types.administrative_override

        out["administrative_override"] = (
            aws_sdk_elastic_load_balancing_v2.types.administrative_override.deserialize_query(
                child_administrative_override
            )
        )
    return out
