"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.__string


class ListTagsForResourceRequest(TypedDict):
    resource_arn: "aws_sdk_dataexchange.types.__string.__string"
    """<p>An Amazon Resource Name (ARN) that uniquely identifies an AWS resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
