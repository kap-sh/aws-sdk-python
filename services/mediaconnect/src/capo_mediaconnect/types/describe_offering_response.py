"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DescribeOfferingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.offering


class DescribeOfferingResponse(TypedDict, closed=True):
    offering: NotRequired["capo_mediaconnect.types.offering.Offering"]
    """<p>The offering that you requested a description of. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeOfferingResponse) -> dict:
    out: dict = {}
    if "offering" in value:
        import capo_mediaconnect.types.offering

        out["offering"] = capo_mediaconnect.types.offering.serialize_json(
            value["offering"]
        )
    return out


def deserialize_json(data: dict) -> DescribeOfferingResponse:
    out: DescribeOfferingResponse = {}  # type: ignore[typeddict-item]
    if "offering" in data:
        import capo_mediaconnect.types.offering

        out["offering"] = capo_mediaconnect.types.offering.deserialize_json(
            data["offering"]
        )
    return out
