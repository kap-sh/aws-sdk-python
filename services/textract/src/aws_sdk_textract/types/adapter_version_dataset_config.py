"""Generated from Smithy shape ``com.amazonaws.textract#AdapterVersionDatasetConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_textract.types.s3_object


class AdapterVersionDatasetConfig(TypedDict, closed=True):
    manifest_s3_object: NotRequired["aws_sdk_textract.types.s3_object.S3Object"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdapterVersionDatasetConfig) -> dict:
    out: dict = {}
    if "manifest_s3_object" in value:
        import aws_sdk_textract.types.s3_object

        out["ManifestS3Object"] = (
            aws_sdk_textract.types.s3_object.serialize_aws_json_1_1(
                value["manifest_s3_object"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AdapterVersionDatasetConfig:
    out: AdapterVersionDatasetConfig = {}  # type: ignore[typeddict-item]
    if "ManifestS3Object" in data:
        import aws_sdk_textract.types.s3_object

        out["manifest_s3_object"] = (
            aws_sdk_textract.types.s3_object.deserialize_aws_json_1_1(
                data["ManifestS3Object"]
            )
        )
    return out
