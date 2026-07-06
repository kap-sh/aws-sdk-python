"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotdeviceadvisor.types.amazon_resource_name


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: (
        "aws_sdk_iotdeviceadvisor.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The resource ARN of the IoT Device Advisor resource. This can be SuiteDefinition ARN or SuiteRun ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
