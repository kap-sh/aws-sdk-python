"""Generated from Smithy shape ``com.amazonaws.iot#FileLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.s3_location
    import aws_sdk_iot.types.stream


class FileLocation(TypedDict, closed=True):
    stream: NotRequired["aws_sdk_iot.types.stream.Stream"]
    """<p>The stream that contains the OTA update.</p>"""
    s3_location: NotRequired["aws_sdk_iot.types.s3_location.S3Location"]
    """<p>The location of the updated firmware in S3.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FileLocation) -> dict:
    out: dict = {}
    if "stream" in value:
        import aws_sdk_iot.types.stream

        out["stream"] = aws_sdk_iot.types.stream.serialize_json(value["stream"])
    if "s3_location" in value:
        import aws_sdk_iot.types.s3_location

        out["s3Location"] = aws_sdk_iot.types.s3_location.serialize_json(
            value["s3_location"]
        )
    return out


def deserialize_json(data: dict) -> FileLocation:
    out: FileLocation = {}  # type: ignore[typeddict-item]
    if "stream" in data:
        import aws_sdk_iot.types.stream

        out["stream"] = aws_sdk_iot.types.stream.deserialize_json(data["stream"])
    if "s3Location" in data:
        import aws_sdk_iot.types.s3_location

        out["s3_location"] = aws_sdk_iot.types.s3_location.deserialize_json(
            data["s3Location"]
        )
    return out
