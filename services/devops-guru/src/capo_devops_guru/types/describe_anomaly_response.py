"""Generated from Smithy shape ``com.amazonaws.devopsguru#DescribeAnomalyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.proactive_anomaly
    import capo_devops_guru.types.reactive_anomaly


class DescribeAnomalyResponse(TypedDict, closed=True):
    proactive_anomaly: NotRequired[
        "capo_devops_guru.types.proactive_anomaly.ProactiveAnomaly"
    ]
    """<p> A <code>ProactiveAnomaly</code> object that represents the requested anomaly. </p>"""
    reactive_anomaly: NotRequired[
        "capo_devops_guru.types.reactive_anomaly.ReactiveAnomaly"
    ]
    """<p> A <code>ReactiveAnomaly</code> object that represents the requested anomaly. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAnomalyResponse) -> dict:
    out: dict = {}
    if "proactive_anomaly" in value:
        import capo_devops_guru.types.proactive_anomaly

        out["ProactiveAnomaly"] = (
            capo_devops_guru.types.proactive_anomaly.serialize_json(
                value["proactive_anomaly"]
            )
        )
    if "reactive_anomaly" in value:
        import capo_devops_guru.types.reactive_anomaly

        out["ReactiveAnomaly"] = capo_devops_guru.types.reactive_anomaly.serialize_json(
            value["reactive_anomaly"]
        )
    return out


def deserialize_json(data: dict) -> DescribeAnomalyResponse:
    out: DescribeAnomalyResponse = {}  # type: ignore[typeddict-item]
    if "ProactiveAnomaly" in data:
        import capo_devops_guru.types.proactive_anomaly

        out["proactive_anomaly"] = (
            capo_devops_guru.types.proactive_anomaly.deserialize_json(
                data["ProactiveAnomaly"]
            )
        )
    if "ReactiveAnomaly" in data:
        import capo_devops_guru.types.reactive_anomaly

        out["reactive_anomaly"] = (
            capo_devops_guru.types.reactive_anomaly.deserialize_json(
                data["ReactiveAnomaly"]
            )
        )
    return out
