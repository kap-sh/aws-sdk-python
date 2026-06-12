"""Generated from Smithy shape ``com.amazonaws.connect#QualityMetrics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.agent_quality_metrics
    import aws_sdk_connect.types.customer_quality_metrics


class QualityMetrics(TypedDict):
    agent: NotRequired[
        "aws_sdk_connect.types.agent_quality_metrics.AgentQualityMetrics"
    ]
    """<p>Information about the quality of Agent media connection.</p>"""
    customer: NotRequired[
        "aws_sdk_connect.types.customer_quality_metrics.CustomerQualityMetrics"
    ]
    """<p>Information about the quality of Customer media connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QualityMetrics) -> dict:
    out: dict = {}
    if "agent" in value:
        import aws_sdk_connect.types.agent_quality_metrics

        out["Agent"] = aws_sdk_connect.types.agent_quality_metrics.serialize_json(
            value["agent"]
        )
    if "customer" in value:
        import aws_sdk_connect.types.customer_quality_metrics

        out["Customer"] = aws_sdk_connect.types.customer_quality_metrics.serialize_json(
            value["customer"]
        )
    return out


def deserialize_json(data: dict) -> QualityMetrics:
    out: QualityMetrics = {}  # type: ignore[typeddict-item]
    if "Agent" in data:
        import aws_sdk_connect.types.agent_quality_metrics

        out["agent"] = aws_sdk_connect.types.agent_quality_metrics.deserialize_json(
            data["Agent"]
        )
    if "Customer" in data:
        import aws_sdk_connect.types.customer_quality_metrics

        out["customer"] = (
            aws_sdk_connect.types.customer_quality_metrics.deserialize_json(
                data["Customer"]
            )
        )
    return out
