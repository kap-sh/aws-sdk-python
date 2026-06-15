"""Generated from Smithy shape ``com.amazonaws.cloudwatch#ListTagsForResourceInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.amazon_resource_name


class ListTagsForResourceInput(TypedDict):
    resource_arn: NotRequired[
        "aws_sdk_cloudwatch.types.amazon_resource_name.AmazonResourceName"
    ]
    r"""<p>The ARN of the CloudWatch resource that you want to view tags for.</p> <p>The ARN format of an alarm is <code>arn:aws:cloudwatch:<i>Region</i>:<i>account-id</i>:alarm:<i>alarm-name</i> </code> </p> <p>The ARN format of a Contributor Insights rule is <code>arn:aws:cloudwatch:<i>Region</i>:<i>account-id</i>:insight-rule/<i>insight-rule-name</i> </code> </p> <p>The ARN format of a dashboard is <code>arn:aws:cloudwatch::<i>account-id</i>:dashboard/<i>dashboard-name</i> </code> </p> <p>The ARN format of a metric stream is <code>arn:aws:cloudwatch:<i>Region</i>:<i>account-id</i>:metric-stream/<i>metric-stream-name</i> </code> </p> <p>For more information about ARN format, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncloudwatch.html#amazoncloudwatch-resources-for-iam-policies\"> Resource Types Defined by Amazon CloudWatch</a> in the <i>Amazon Web Services General Reference</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceInput) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceInput:
    out: ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: ListTagsForResourceInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_arn" in value:
        pairs.append((f"{prefix}.ResourceARN", str(value["resource_arn"])))


def deserialize_query(el: Element) -> ListTagsForResourceInput:
    out: ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
    child_resource_arn = el.find("ResourceARN")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    return out
