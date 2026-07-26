"""Generated from Smithy shape ``com.amazonaws.sagemaker#TensorBoardAppSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.resource_spec


class TensorBoardAppSettings(TypedDict, closed=True):
    default_resource_spec: NotRequired[
        "capo_sagemaker.types.resource_spec.ResourceSpec"
    ]
    """<p>The default instance type and the Amazon Resource Name (ARN) of the SageMaker AI image created on the instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TensorBoardAppSettings) -> dict:
    out: dict = {}
    if "default_resource_spec" in value:
        import capo_sagemaker.types.resource_spec

        out["DefaultResourceSpec"] = (
            capo_sagemaker.types.resource_spec.serialize_aws_json_1_1(
                value["default_resource_spec"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TensorBoardAppSettings:
    out: TensorBoardAppSettings = {}  # type: ignore[typeddict-item]
    if "DefaultResourceSpec" in data:
        import capo_sagemaker.types.resource_spec

        out["default_resource_spec"] = (
            capo_sagemaker.types.resource_spec.deserialize_aws_json_1_1(
                data["DefaultResourceSpec"]
            )
        )
    return out
