"""Generated from Smithy shape ``com.amazonaws.sagemaker#EnvironmentConfigDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.f_sx_lustre_config
    import aws_sdk_sagemaker.types.s3_uri


class EnvironmentConfigDetails(TypedDict):
    f_sx_lustre_config: NotRequired[
        "aws_sdk_sagemaker.types.f_sx_lustre_config.FSxLustreConfig"
    ]
    """<p>Configuration settings for an Amazon FSx for Lustre file system to be used with the cluster.</p>"""
    s3_output_path: NotRequired["aws_sdk_sagemaker.types.s3_uri.S3Uri"]
    """<p>The Amazon S3 path where output data from the restricted instance group (RIG) environment will be stored.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentConfigDetails) -> dict:
    out: dict = {}
    if "f_sx_lustre_config" in value:
        import aws_sdk_sagemaker.types.f_sx_lustre_config

        out["FSxLustreConfig"] = (
            aws_sdk_sagemaker.types.f_sx_lustre_config.serialize_aws_json_1_1(
                value["f_sx_lustre_config"]
            )
        )
    if "s3_output_path" in value:
        out["S3OutputPath"] = value["s3_output_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EnvironmentConfigDetails:
    out: EnvironmentConfigDetails = {}  # type: ignore[typeddict-item]
    if "FSxLustreConfig" in data:
        import aws_sdk_sagemaker.types.f_sx_lustre_config

        out["f_sx_lustre_config"] = (
            aws_sdk_sagemaker.types.f_sx_lustre_config.deserialize_aws_json_1_1(
                data["FSxLustreConfig"]
            )
        )
    if "S3OutputPath" in data:
        out["s3_output_path"] = data["S3OutputPath"]
    return out
