"""Generated from Smithy shape ``com.amazonaws.medialive#DescribeOfferingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class DescribeOfferingRequest(TypedDict, closed=True):
    offering_id: "aws_sdk_medialive.types.__string.__string"
    """Unique offering ID, e.g. '87654321'"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeOfferingRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeOfferingRequest:
    out: DescribeOfferingRequest = {}  # type: ignore[typeddict-item]
    return out
