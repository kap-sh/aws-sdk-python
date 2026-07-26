"""Generated from Smithy shape ``com.amazonaws.connect#QualityMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.agent_quality_metrics
    import capo_connect.types.customer_quality_metrics


class QualityMetrics(TypedDict, closed=True):
    agent: NotRequired["capo_connect.types.agent_quality_metrics.AgentQualityMetrics"]
    """<p>Information about the quality of Agent media connection.</p>"""
    customer: NotRequired[
        "capo_connect.types.customer_quality_metrics.CustomerQualityMetrics"
    ]
    """<p>Information about the quality of Customer media connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QualityMetrics) -> dict:
    out: dict = {}
    if "agent" in value:
        import capo_connect.types.agent_quality_metrics

        out["Agent"] = capo_connect.types.agent_quality_metrics.serialize_json(
            value["agent"]
        )
    if "customer" in value:
        import capo_connect.types.customer_quality_metrics

        out["Customer"] = capo_connect.types.customer_quality_metrics.serialize_json(
            value["customer"]
        )
    return out


def deserialize_json(data: dict) -> QualityMetrics:
    out: QualityMetrics = {}  # type: ignore[typeddict-item]
    if "Agent" in data:
        import capo_connect.types.agent_quality_metrics

        out["agent"] = capo_connect.types.agent_quality_metrics.deserialize_json(
            data["Agent"]
        )
    if "Customer" in data:
        import capo_connect.types.customer_quality_metrics

        out["customer"] = capo_connect.types.customer_quality_metrics.deserialize_json(
            data["Customer"]
        )
    return out
