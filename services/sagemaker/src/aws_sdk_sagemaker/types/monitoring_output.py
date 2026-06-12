"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.monitoring_s3_output


class MonitoringOutput(TypedDict):
    s3_output: NotRequired[
        "aws_sdk_sagemaker.types.monitoring_s3_output.MonitoringS3Output"
    ]
    """<p>The Amazon S3 storage location where the results of a monitoring job are saved.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringOutput) -> dict:
    out: dict = {}
    if "s3_output" in value:
        import aws_sdk_sagemaker.types.monitoring_s3_output

        out["S3Output"] = (
            aws_sdk_sagemaker.types.monitoring_s3_output.serialize_aws_json_1_1(
                value["s3_output"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MonitoringOutput:
    out: MonitoringOutput = {}  # type: ignore[typeddict-item]
    if "S3Output" in data:
        import aws_sdk_sagemaker.types.monitoring_s3_output

        out["s3_output"] = (
            aws_sdk_sagemaker.types.monitoring_s3_output.deserialize_aws_json_1_1(
                data["S3Output"]
            )
        )
    return out
