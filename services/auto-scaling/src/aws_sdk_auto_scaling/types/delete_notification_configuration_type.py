"""Generated from Smithy shape ``com.amazonaws.autoscaling#DeleteNotificationConfigurationType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.xml_string_max_len255


class DeleteNotificationConfigurationType(TypedDict, closed=True):
    auto_scaling_group_name: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the Auto Scaling group.</p>"""
    topic_arn: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The Amazon Resource Name (ARN) of the Amazon SNS topic.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteNotificationConfigurationType,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "auto_scaling_group_name" in value:
        pairs.append(
            (f"{prefix}.AutoScalingGroupName", str(value["auto_scaling_group_name"]))
        )
    if "topic_arn" in value:
        pairs.append((f"{prefix}.TopicARN", str(value["topic_arn"])))


def deserialize_query(el: Element) -> DeleteNotificationConfigurationType:
    out: DeleteNotificationConfigurationType = {}  # type: ignore[typeddict-item]
    child_auto_scaling_group_name = el.find("AutoScalingGroupName")
    if child_auto_scaling_group_name is not None:
        out["auto_scaling_group_name"] = str(child_auto_scaling_group_name.text or "")
    child_topic_arn = el.find("TopicARN")
    if child_topic_arn is not None:
        out["topic_arn"] = str(child_topic_arn.text or "")
    return out
