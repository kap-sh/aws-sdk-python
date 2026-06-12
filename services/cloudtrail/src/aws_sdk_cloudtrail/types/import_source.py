"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ImportSource``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.s3_import_source


class ImportSource(TypedDict):
    s3: "aws_sdk_cloudtrail.types.s3_import_source.S3ImportSource"
    """<p> The source S3 bucket. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportSource) -> dict:
    out: dict = {}
    import aws_sdk_cloudtrail.types.s3_import_source

    out["S3"] = aws_sdk_cloudtrail.types.s3_import_source.serialize_aws_json_1_1(
        value["s3"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportSource:
    out: ImportSource = {}  # type: ignore[typeddict-item]
    if "S3" in data:
        import aws_sdk_cloudtrail.types.s3_import_source

        out["s3"] = aws_sdk_cloudtrail.types.s3_import_source.deserialize_aws_json_1_1(
            data["S3"]
        )
    else:
        raise DeserializationError("ImportSource.s3 required")
    return out
