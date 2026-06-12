"""Generated from Smithy shape ``com.amazonaws.sagemaker#TensorBoardAppSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.resource_spec


class TensorBoardAppSettings(TypedDict):
    default_resource_spec: NotRequired[
        "aws_sdk_sagemaker.types.resource_spec.ResourceSpec"
    ]
    """<p>The default instance type and the Amazon Resource Name (ARN) of the SageMaker AI image created on the instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TensorBoardAppSettings) -> dict:
    out: dict = {}
    if "default_resource_spec" in value:
        import aws_sdk_sagemaker.types.resource_spec

        out["DefaultResourceSpec"] = (
            aws_sdk_sagemaker.types.resource_spec.serialize_aws_json_1_1(
                value["default_resource_spec"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TensorBoardAppSettings:
    out: TensorBoardAppSettings = {}  # type: ignore[typeddict-item]
    if "DefaultResourceSpec" in data:
        import aws_sdk_sagemaker.types.resource_spec

        out["default_resource_spec"] = (
            aws_sdk_sagemaker.types.resource_spec.deserialize_aws_json_1_1(
                data["DefaultResourceSpec"]
            )
        )
    return out
