"""Generated from Smithy shape ``com.amazonaws.mediapackage#DescribeHarvestJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackage.types.__string


class DescribeHarvestJobRequest(TypedDict, closed=True):
    id: "aws_sdk_mediapackage.types.__string.__string"
    """The ID of the HarvestJob."""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeHarvestJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeHarvestJobRequest:
    out: DescribeHarvestJobRequest = {}  # type: ignore[typeddict-item]
    return out
