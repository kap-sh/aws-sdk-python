"""Generated from Smithy shape ``com.amazonaws.iot#DescribeIndexRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.index_name


class DescribeIndexRequest(TypedDict):
    index_name: "aws_sdk_iot.types.index_name.IndexName"
    """<p>The index name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeIndexRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeIndexRequest:
    out: DescribeIndexRequest = {}  # type: ignore[typeddict-item]
    return out
