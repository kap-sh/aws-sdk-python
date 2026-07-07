"""Generated from Smithy shape ``com.amazonaws.sagemaker#EnvironmentConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.f_sx_lustre_config


class EnvironmentConfig(TypedDict, closed=True):
    f_sx_lustre_config: NotRequired[
        "aws_sdk_sagemaker.types.f_sx_lustre_config.FSxLustreConfig"
    ]
    """<p>Configuration settings for an Amazon FSx for Lustre file system to be used with the cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentConfig) -> dict:
    out: dict = {}
    if "f_sx_lustre_config" in value:
        import aws_sdk_sagemaker.types.f_sx_lustre_config

        out["FSxLustreConfig"] = (
            aws_sdk_sagemaker.types.f_sx_lustre_config.serialize_aws_json_1_1(
                value["f_sx_lustre_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EnvironmentConfig:
    out: EnvironmentConfig = {}  # type: ignore[typeddict-item]
    if "FSxLustreConfig" in data:
        import aws_sdk_sagemaker.types.f_sx_lustre_config

        out["f_sx_lustre_config"] = (
            aws_sdk_sagemaker.types.f_sx_lustre_config.deserialize_aws_json_1_1(
                data["FSxLustreConfig"]
            )
        )
    return out
