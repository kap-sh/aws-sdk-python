"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#TargetHealthDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.administrative_override
    import capo_elastic_load_balancing_v2.types.anomaly_detection
    import capo_elastic_load_balancing_v2.types.health_check_port
    import capo_elastic_load_balancing_v2.types.target_description
    import capo_elastic_load_balancing_v2.types.target_health


class TargetHealthDescription(TypedDict, closed=True):
    target: NotRequired[
        "capo_elastic_load_balancing_v2.types.target_description.TargetDescription"
    ]
    """<p>The description of the target.</p>"""
    health_check_port: NotRequired[
        "capo_elastic_load_balancing_v2.types.health_check_port.HealthCheckPort"
    ]
    """<p>The port to use to connect with the target.</p>"""
    target_health: NotRequired[
        "capo_elastic_load_balancing_v2.types.target_health.TargetHealth"
    ]
    """<p>The health information for the target.</p>"""
    anomaly_detection: NotRequired[
        "capo_elastic_load_balancing_v2.types.anomaly_detection.AnomalyDetection"
    ]
    """<p>The anomaly detection result for the target.</p> <p>If no anomalies were detected, the result is <code>normal</code>.</p> <p>If anomalies were detected, the result is <code>anomalous</code>.</p>"""
    administrative_override: NotRequired[
        "capo_elastic_load_balancing_v2.types.administrative_override.AdministrativeOverride"
    ]
    """<p>The administrative override information for the target.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TargetHealthDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "target" in value:
        import capo_elastic_load_balancing_v2.types.target_description

        capo_elastic_load_balancing_v2.types.target_description.serialize_query(
            value["target"], pairs, f"{key_prefix}Target"
        )
    if "health_check_port" in value:
        pairs.append((f"{key_prefix}HealthCheckPort", str(value["health_check_port"])))
    if "target_health" in value:
        import capo_elastic_load_balancing_v2.types.target_health

        capo_elastic_load_balancing_v2.types.target_health.serialize_query(
            value["target_health"], pairs, f"{key_prefix}TargetHealth"
        )
    if "anomaly_detection" in value:
        import capo_elastic_load_balancing_v2.types.anomaly_detection

        capo_elastic_load_balancing_v2.types.anomaly_detection.serialize_query(
            value["anomaly_detection"], pairs, f"{key_prefix}AnomalyDetection"
        )
    if "administrative_override" in value:
        import capo_elastic_load_balancing_v2.types.administrative_override

        capo_elastic_load_balancing_v2.types.administrative_override.serialize_query(
            value["administrative_override"],
            pairs,
            f"{key_prefix}AdministrativeOverride",
        )


def deserialize_query(el: Element) -> TargetHealthDescription:
    out: TargetHealthDescription = {}  # type: ignore[typeddict-item]
    child_target = el.find("Target")
    if child_target is not None:
        import capo_elastic_load_balancing_v2.types.target_description

        out["target"] = (
            capo_elastic_load_balancing_v2.types.target_description.deserialize_query(
                child_target
            )
        )
    child_health_check_port = el.find("HealthCheckPort")
    if child_health_check_port is not None:
        out["health_check_port"] = str(child_health_check_port.text or "")
    child_target_health = el.find("TargetHealth")
    if child_target_health is not None:
        import capo_elastic_load_balancing_v2.types.target_health

        out["target_health"] = (
            capo_elastic_load_balancing_v2.types.target_health.deserialize_query(
                child_target_health
            )
        )
    child_anomaly_detection = el.find("AnomalyDetection")
    if child_anomaly_detection is not None:
        import capo_elastic_load_balancing_v2.types.anomaly_detection

        out["anomaly_detection"] = (
            capo_elastic_load_balancing_v2.types.anomaly_detection.deserialize_query(
                child_anomaly_detection
            )
        )
    child_administrative_override = el.find("AdministrativeOverride")
    if child_administrative_override is not None:
        import capo_elastic_load_balancing_v2.types.administrative_override

        out["administrative_override"] = (
            capo_elastic_load_balancing_v2.types.administrative_override.deserialize_query(
                child_administrative_override
            )
        )
    return out
