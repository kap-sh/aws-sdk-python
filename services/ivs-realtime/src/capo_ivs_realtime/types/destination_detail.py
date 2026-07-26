"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#DestinationDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.s3_detail


class DestinationDetail(TypedDict, closed=True):
    s3: NotRequired["capo_ivs_realtime.types.s3_detail.S3Detail"]
    """<p>An S3 detail object to return information about the S3 destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DestinationDetail) -> dict:
    out: dict = {}
    if "s3" in value:
        import capo_ivs_realtime.types.s3_detail

        out["s3"] = capo_ivs_realtime.types.s3_detail.serialize_json(value["s3"])
    return out


def deserialize_json(data: dict) -> DestinationDetail:
    out: DestinationDetail = {}  # type: ignore[typeddict-item]
    if "s3" in data:
        import capo_ivs_realtime.types.s3_detail

        out["s3"] = capo_ivs_realtime.types.s3_detail.deserialize_json(data["s3"])
    return out
