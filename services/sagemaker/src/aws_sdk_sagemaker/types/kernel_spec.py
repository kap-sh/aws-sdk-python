"""Generated from Smithy shape ``com.amazonaws.sagemaker#KernelSpec``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.kernel_display_name
    import aws_sdk_sagemaker.types.kernel_name


class KernelSpec(TypedDict, closed=True):
    name: NotRequired["aws_sdk_sagemaker.types.kernel_name.KernelName"]
    """<p>The name of the Jupyter kernel in the image. This value is case sensitive.</p>"""
    display_name: NotRequired[
        "aws_sdk_sagemaker.types.kernel_display_name.KernelDisplayName"
    ]
    """<p>The display name of the kernel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KernelSpec) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KernelSpec:
    out: KernelSpec = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    return out
