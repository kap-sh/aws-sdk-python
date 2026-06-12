"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DescribeTagOptionInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.tag_option_id


class DescribeTagOptionInput(TypedDict):
    id: "aws_sdk_service_catalog.types.tag_option_id.TagOptionId"
    """<p>The TagOption identifier.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTagOptionInput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTagOptionInput:
    out: DescribeTagOptionInput = {}  # type: ignore[typeddict-item]
    return out
