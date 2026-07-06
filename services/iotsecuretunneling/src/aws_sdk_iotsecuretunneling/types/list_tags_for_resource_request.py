"""Generated from Smithy shape ``com.amazonaws.iotsecuretunneling#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotsecuretunneling.types.amazon_resource_name


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: (
        "aws_sdk_iotsecuretunneling.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The resource ARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
