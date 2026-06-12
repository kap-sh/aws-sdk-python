"""Generated from Smithy shape ``com.amazonaws.devopsguru#DescribeInsightResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.proactive_insight
    import aws_sdk_devops_guru.types.reactive_insight


class DescribeInsightResponse(TypedDict):
    proactive_insight: NotRequired[
        "aws_sdk_devops_guru.types.proactive_insight.ProactiveInsight"
    ]
    """<p> A <code>ProactiveInsight</code> object that represents the requested insight. </p>"""
    reactive_insight: NotRequired[
        "aws_sdk_devops_guru.types.reactive_insight.ReactiveInsight"
    ]
    """<p> A <code>ReactiveInsight</code> object that represents the requested insight. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeInsightResponse) -> dict:
    out: dict = {}
    if "proactive_insight" in value:
        import aws_sdk_devops_guru.types.proactive_insight

        out["ProactiveInsight"] = (
            aws_sdk_devops_guru.types.proactive_insight.serialize_json(
                value["proactive_insight"]
            )
        )
    if "reactive_insight" in value:
        import aws_sdk_devops_guru.types.reactive_insight

        out["ReactiveInsight"] = (
            aws_sdk_devops_guru.types.reactive_insight.serialize_json(
                value["reactive_insight"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeInsightResponse:
    out: DescribeInsightResponse = {}  # type: ignore[typeddict-item]
    if "ProactiveInsight" in data:
        import aws_sdk_devops_guru.types.proactive_insight

        out["proactive_insight"] = (
            aws_sdk_devops_guru.types.proactive_insight.deserialize_json(
                data["ProactiveInsight"]
            )
        )
    if "ReactiveInsight" in data:
        import aws_sdk_devops_guru.types.reactive_insight

        out["reactive_insight"] = (
            aws_sdk_devops_guru.types.reactive_insight.deserialize_json(
                data["ReactiveInsight"]
            )
        )
    return out
