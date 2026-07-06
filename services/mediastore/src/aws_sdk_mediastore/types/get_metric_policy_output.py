"""Generated from Smithy shape ``com.amazonaws.mediastore#GetMetricPolicyOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mediastore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediastore.types.metric_policy


class GetMetricPolicyOutput(TypedDict, closed=True):
    metric_policy: "aws_sdk_mediastore.types.metric_policy.MetricPolicy"
    """<p>The metric policy that is associated with the specific container.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMetricPolicyOutput) -> dict:
    out: dict = {}
    import aws_sdk_mediastore.types.metric_policy

    out["MetricPolicy"] = aws_sdk_mediastore.types.metric_policy.serialize_aws_json_1_1(
        value["metric_policy"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMetricPolicyOutput:
    out: GetMetricPolicyOutput = {}  # type: ignore[typeddict-item]
    if "MetricPolicy" in data:
        import aws_sdk_mediastore.types.metric_policy

        out["metric_policy"] = (
            aws_sdk_mediastore.types.metric_policy.deserialize_aws_json_1_1(
                data["MetricPolicy"]
            )
        )
    else:
        raise DeserializationError("GetMetricPolicyOutput.metric_policy required")
    return out
