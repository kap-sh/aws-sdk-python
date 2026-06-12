"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#DestinationDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.s3_detail


class DestinationDetail(TypedDict):
    s3: NotRequired["aws_sdk_ivs_realtime.types.s3_detail.S3Detail"]
    """<p>An S3 detail object to return information about the S3 destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DestinationDetail) -> dict:
    out: dict = {}
    if "s3" in value:
        import aws_sdk_ivs_realtime.types.s3_detail

        out["s3"] = aws_sdk_ivs_realtime.types.s3_detail.serialize_json(value["s3"])
    return out


def deserialize_json(data: dict) -> DestinationDetail:
    out: DestinationDetail = {}  # type: ignore[typeddict-item]
    if "s3" in data:
        import aws_sdk_ivs_realtime.types.s3_detail

        out["s3"] = aws_sdk_ivs_realtime.types.s3_detail.deserialize_json(data["s3"])
    return out
