"""Generated from Smithy shape ``com.amazonaws.kendra#DocumentsMetadataConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kendra.types.s3_object_key


class DocumentsMetadataConfiguration(TypedDict, closed=True):
    s3_prefix: NotRequired["aws_sdk_kendra.types.s3_object_key.S3ObjectKey"]
    """<p>A prefix used to filter metadata configuration files in the Amazon Web Services S3 bucket. The S3 bucket might contain multiple metadata files. Use <code>S3Prefix</code> to include only the desired metadata files.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentsMetadataConfiguration) -> dict:
    out: dict = {}
    if "s3_prefix" in value:
        out["S3Prefix"] = value["s3_prefix"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentsMetadataConfiguration:
    out: DocumentsMetadataConfiguration = {}  # type: ignore[typeddict-item]
    if "S3Prefix" in data:
        out["s3_prefix"] = data["S3Prefix"]
    return out
