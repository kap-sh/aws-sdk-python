"""Generated from Smithy shape ``com.amazonaws.cloudformation#RollbackTrigger``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.arn
    import aws_sdk_cloudformation.types.type


class RollbackTrigger(TypedDict):
    arn: NotRequired["aws_sdk_cloudformation.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the rollback trigger.</p> <p>If a specified trigger is missing, the entire stack operation fails and is rolled back.</p>"""
    type: NotRequired["aws_sdk_cloudformation.types.type.Type"]
    """<p>The resource type of the rollback trigger. Specify either <a href=\"https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-alarm.html\">AWS::CloudWatch::Alarm</a> or <a href=\"https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-compositealarm.html\">AWS::CloudWatch::CompositeAlarm</a> resource types.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RollbackTrigger, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "arn" in value:
        pairs.append((f"{prefix}.Arn", str(value["arn"])))
    if "type" in value:
        pairs.append((f"{prefix}.Type", str(value["type"])))


def deserialize_query(el: Element) -> RollbackTrigger:
    out: RollbackTrigger = {}  # type: ignore[typeddict-item]
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    child_type = el.find("Type")
    if child_type is not None:
        out["type"] = str(child_type.text or "")
    return out
