"""Generated from Smithy shape ``com.amazonaws.devopsguru#DescribeAnomalyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.proactive_anomaly
    import aws_sdk_devops_guru.types.reactive_anomaly


class DescribeAnomalyResponse(TypedDict):
    proactive_anomaly: NotRequired[
        "aws_sdk_devops_guru.types.proactive_anomaly.ProactiveAnomaly"
    ]
    """<p> A <code>ProactiveAnomaly</code> object that represents the requested anomaly. </p>"""
    reactive_anomaly: NotRequired[
        "aws_sdk_devops_guru.types.reactive_anomaly.ReactiveAnomaly"
    ]
    """<p> A <code>ReactiveAnomaly</code> object that represents the requested anomaly. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAnomalyResponse) -> dict:
    out: dict = {}
    if "proactive_anomaly" in value:
        import aws_sdk_devops_guru.types.proactive_anomaly

        out["ProactiveAnomaly"] = (
            aws_sdk_devops_guru.types.proactive_anomaly.serialize_json(
                value["proactive_anomaly"]
            )
        )
    if "reactive_anomaly" in value:
        import aws_sdk_devops_guru.types.reactive_anomaly

        out["ReactiveAnomaly"] = (
            aws_sdk_devops_guru.types.reactive_anomaly.serialize_json(
                value["reactive_anomaly"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeAnomalyResponse:
    out: DescribeAnomalyResponse = {}  # type: ignore[typeddict-item]
    if "ProactiveAnomaly" in data:
        import aws_sdk_devops_guru.types.proactive_anomaly

        out["proactive_anomaly"] = (
            aws_sdk_devops_guru.types.proactive_anomaly.deserialize_json(
                data["ProactiveAnomaly"]
            )
        )
    if "ReactiveAnomaly" in data:
        import aws_sdk_devops_guru.types.reactive_anomaly

        out["reactive_anomaly"] = (
            aws_sdk_devops_guru.types.reactive_anomaly.deserialize_json(
                data["ReactiveAnomaly"]
            )
        )
    return out
