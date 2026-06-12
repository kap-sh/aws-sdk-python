"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestSetImportInputLocation``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.s3_bucket_name
    import aws_sdk_lex_models_v2.types.s3_object_path


class TestSetImportInputLocation(TypedDict):
    s3_bucket_name: "aws_sdk_lex_models_v2.types.s3_bucket_name.S3BucketName"
    """<p>The name of the Amazon S3 bucket.</p>"""
    s3_path: "aws_sdk_lex_models_v2.types.s3_object_path.S3ObjectPath"
    """<p>The path inside the Amazon S3 bucket pointing to the test-set CSV file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestSetImportInputLocation) -> dict:
    out: dict = {}
    out["s3BucketName"] = value["s3_bucket_name"]
    out["s3Path"] = value["s3_path"]
    return out


def deserialize_json(data: dict) -> TestSetImportInputLocation:
    out: TestSetImportInputLocation = {}  # type: ignore[typeddict-item]
    if "s3BucketName" in data:
        out["s3_bucket_name"] = data["s3BucketName"]
    else:
        raise DeserializationError("TestSetImportInputLocation.s3_bucket_name required")
    if "s3Path" in data:
        out["s3_path"] = data["s3Path"]
    else:
        raise DeserializationError("TestSetImportInputLocation.s3_path required")
    return out
