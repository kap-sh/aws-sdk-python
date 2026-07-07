"""Generated from Smithy shape ``com.amazonaws.imagebuilder#Logging``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.s3_logs


class Logging(TypedDict, closed=True):
    s3_logs: NotRequired["aws_sdk_imagebuilder.types.s3_logs.S3Logs"]
    """<p>The Amazon S3 logging configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Logging) -> dict:
    out: dict = {}
    if "s3_logs" in value:
        import aws_sdk_imagebuilder.types.s3_logs

        out["s3Logs"] = aws_sdk_imagebuilder.types.s3_logs.serialize_json(
            value["s3_logs"]
        )
    return out


def deserialize_json(data: dict) -> Logging:
    out: Logging = {}  # type: ignore[typeddict-item]
    if "s3Logs" in data:
        import aws_sdk_imagebuilder.types.s3_logs

        out["s3_logs"] = aws_sdk_imagebuilder.types.s3_logs.deserialize_json(
            data["s3Logs"]
        )
    return out
