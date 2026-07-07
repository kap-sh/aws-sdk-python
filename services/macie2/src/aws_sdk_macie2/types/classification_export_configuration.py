"""Generated from Smithy shape ``com.amazonaws.macie2#ClassificationExportConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.s3_destination


class ClassificationExportConfiguration(TypedDict, closed=True):
    s3_destination: NotRequired["aws_sdk_macie2.types.s3_destination.S3Destination"]
    """<p>The S3 bucket to store data classification results in, and the encryption settings to use when storing results in that bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClassificationExportConfiguration) -> dict:
    out: dict = {}
    if "s3_destination" in value:
        import aws_sdk_macie2.types.s3_destination

        out["s3Destination"] = aws_sdk_macie2.types.s3_destination.serialize_json(
            value["s3_destination"]
        )
    return out


def deserialize_json(data: dict) -> ClassificationExportConfiguration:
    out: ClassificationExportConfiguration = {}  # type: ignore[typeddict-item]
    if "s3Destination" in data:
        import aws_sdk_macie2.types.s3_destination

        out["s3_destination"] = aws_sdk_macie2.types.s3_destination.deserialize_json(
            data["s3Destination"]
        )
    return out
