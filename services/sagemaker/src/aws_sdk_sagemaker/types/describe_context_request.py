"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeContextRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.context_name_or_arn


class DescribeContextRequest(TypedDict):
    context_name: NotRequired[
        "aws_sdk_sagemaker.types.context_name_or_arn.ContextNameOrArn"
    ]
    """<p>The name of the context to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeContextRequest) -> dict:
    out: dict = {}
    if "context_name" in value:
        out["ContextName"] = value["context_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeContextRequest:
    out: DescribeContextRequest = {}  # type: ignore[typeddict-item]
    if "ContextName" in data:
        out["context_name"] = data["ContextName"]
    return out
