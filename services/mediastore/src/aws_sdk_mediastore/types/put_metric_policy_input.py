"""Generated from Smithy shape ``com.amazonaws.mediastore#PutMetricPolicyInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mediastore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediastore.types.container_name
    import aws_sdk_mediastore.types.metric_policy


class PutMetricPolicyInput(TypedDict):
    container_name: "aws_sdk_mediastore.types.container_name.ContainerName"
    """<p>The name of the container that you want to add the metric policy to.</p>"""
    metric_policy: "aws_sdk_mediastore.types.metric_policy.MetricPolicy"
    """<p>The metric policy that you want to associate with the container. In the policy, you must indicate whether you want MediaStore to send container-level metrics. You can also include up to five rules to define groups of objects that you want MediaStore to send object-level metrics for. If you include rules in the policy, construct each rule with both of the following:</p> <ul> <li> <p>An object group that defines which objects to include in the group. The definition can be a path or a file name, but it can't have more than 900 characters. Valid characters are: a-z, A-Z, 0-9, _ (underscore), = (equal), : (colon), . (period), - (hyphen), ~ (tilde), / (forward slash), and * (asterisk). Wildcards (*) are acceptable.</p> </li> <li> <p>An object group name that allows you to refer to the object group. The name can't have more than 30 characters. Valid characters are: a-z, A-Z, 0-9, and _ (underscore).</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutMetricPolicyInput) -> dict:
    out: dict = {}
    out["ContainerName"] = value["container_name"]
    import aws_sdk_mediastore.types.metric_policy

    out["MetricPolicy"] = aws_sdk_mediastore.types.metric_policy.serialize_aws_json_1_1(
        value["metric_policy"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutMetricPolicyInput:
    out: PutMetricPolicyInput = {}  # type: ignore[typeddict-item]
    if "ContainerName" in data:
        out["container_name"] = data["ContainerName"]
    else:
        raise DeserializationError("PutMetricPolicyInput.container_name required")
    if "MetricPolicy" in data:
        import aws_sdk_mediastore.types.metric_policy

        out["metric_policy"] = (
            aws_sdk_mediastore.types.metric_policy.deserialize_aws_json_1_1(
                data["MetricPolicy"]
            )
        )
    else:
        raise DeserializationError("PutMetricPolicyInput.metric_policy required")
    return out
