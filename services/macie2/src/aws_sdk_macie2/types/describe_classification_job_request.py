"""Generated from Smithy shape ``com.amazonaws.macie2#DescribeClassificationJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__string


class DescribeClassificationJobRequest(TypedDict):
    job_id: "aws_sdk_macie2.types.__string.__string"
    """<p>The unique identifier for the classification job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeClassificationJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeClassificationJobRequest:
    out: DescribeClassificationJobRequest = {}  # type: ignore[typeddict-item]
    return out
