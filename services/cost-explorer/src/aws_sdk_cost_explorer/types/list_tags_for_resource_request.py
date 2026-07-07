"""Generated from Smithy shape ``com.amazonaws.costexplorer#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_cost_explorer.types.arn.Arn"
    r"""<p>The Amazon Resource Name (ARN) of the resource. For a list of supported resources, see <a href=\"https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_ResourceTag.html\">ResourceTag</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("ListTagsForResourceRequest.resource_arn required")
    return out
