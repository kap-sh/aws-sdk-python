"""Generated from Smithy shape ``com.amazonaws.sagemaker#WorkerAccessConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.s3_presign


class WorkerAccessConfiguration(TypedDict):
    s3_presign: NotRequired["aws_sdk_sagemaker.types.s3_presign.S3Presign"]
    """<p>Defines any Amazon S3 resource constraints.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkerAccessConfiguration) -> dict:
    out: dict = {}
    if "s3_presign" in value:
        import aws_sdk_sagemaker.types.s3_presign

        out["S3Presign"] = aws_sdk_sagemaker.types.s3_presign.serialize_aws_json_1_1(
            value["s3_presign"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkerAccessConfiguration:
    out: WorkerAccessConfiguration = {}  # type: ignore[typeddict-item]
    if "S3Presign" in data:
        import aws_sdk_sagemaker.types.s3_presign

        out["s3_presign"] = aws_sdk_sagemaker.types.s3_presign.deserialize_aws_json_1_1(
            data["S3Presign"]
        )
    return out
