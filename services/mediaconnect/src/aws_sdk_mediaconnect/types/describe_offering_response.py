"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DescribeOfferingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.offering


class DescribeOfferingResponse(TypedDict, closed=True):
    offering: NotRequired["aws_sdk_mediaconnect.types.offering.Offering"]
    """<p>The offering that you requested a description of. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeOfferingResponse) -> dict:
    out: dict = {}
    if "offering" in value:
        import aws_sdk_mediaconnect.types.offering

        out["offering"] = aws_sdk_mediaconnect.types.offering.serialize_json(
            value["offering"]
        )
    return out


def deserialize_json(data: dict) -> DescribeOfferingResponse:
    out: DescribeOfferingResponse = {}  # type: ignore[typeddict-item]
    if "offering" in data:
        import aws_sdk_mediaconnect.types.offering

        out["offering"] = aws_sdk_mediaconnect.types.offering.deserialize_json(
            data["offering"]
        )
    return out
