"""Generated from Smithy shape ``com.amazonaws.groundstation#DescribeEphemerisRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.uuid


class DescribeEphemerisRequest(TypedDict, closed=True):
    ephemeris_id: "aws_sdk_groundstation.types.uuid.Uuid"
    """<p>The AWS Ground Station ephemeris ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeEphemerisRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeEphemerisRequest:
    out: DescribeEphemerisRequest = {}  # type: ignore[typeddict-item]
    return out
