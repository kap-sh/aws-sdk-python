"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#AnomalyDetection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.anomaly_result_enum
    import capo_elastic_load_balancing_v2.types.mitigation_in_effect_enum


class AnomalyDetection(TypedDict, closed=True):
    result: NotRequired[
        "capo_elastic_load_balancing_v2.types.anomaly_result_enum.AnomalyResultEnum"
    ]
    """<p>The latest anomaly detection result.</p>"""
    mitigation_in_effect: NotRequired[
        "capo_elastic_load_balancing_v2.types.mitigation_in_effect_enum.MitigationInEffectEnum"
    ]
    """<p>Indicates whether anomaly mitigation is in progress.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AnomalyDetection, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "result" in value:
        import capo_elastic_load_balancing_v2.types.anomaly_result_enum

        capo_elastic_load_balancing_v2.types.anomaly_result_enum.serialize_query(
            value["result"], pairs, f"{prefix}.Result"
        )
    if "mitigation_in_effect" in value:
        import capo_elastic_load_balancing_v2.types.mitigation_in_effect_enum

        capo_elastic_load_balancing_v2.types.mitigation_in_effect_enum.serialize_query(
            value["mitigation_in_effect"], pairs, f"{prefix}.MitigationInEffect"
        )


def deserialize_query(el: Element) -> AnomalyDetection:
    out: AnomalyDetection = {}  # type: ignore[typeddict-item]
    child_result = el.find("Result")
    if child_result is not None:
        import capo_elastic_load_balancing_v2.types.anomaly_result_enum

        out["result"] = (
            capo_elastic_load_balancing_v2.types.anomaly_result_enum.deserialize_query(
                child_result
            )
        )
    child_mitigation_in_effect = el.find("MitigationInEffect")
    if child_mitigation_in_effect is not None:
        import capo_elastic_load_balancing_v2.types.mitigation_in_effect_enum

        out["mitigation_in_effect"] = (
            capo_elastic_load_balancing_v2.types.mitigation_in_effect_enum.deserialize_query(
                child_mitigation_in_effect
            )
        )
    return out
