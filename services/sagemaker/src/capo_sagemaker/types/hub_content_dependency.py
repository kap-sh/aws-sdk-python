"""Generated from Smithy shape ``com.amazonaws.sagemaker#HubContentDependency``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.dependency_copy_path
    import capo_sagemaker.types.dependency_origin_path


class HubContentDependency(TypedDict, closed=True):
    dependency_origin_path: NotRequired[
        "capo_sagemaker.types.dependency_origin_path.DependencyOriginPath"
    ]
    """<p>The hub content dependency origin path.</p>"""
    dependency_copy_path: NotRequired[
        "capo_sagemaker.types.dependency_copy_path.DependencyCopyPath"
    ]
    """<p>The hub content dependency copy path.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HubContentDependency) -> dict:
    out: dict = {}
    if "dependency_origin_path" in value:
        out["DependencyOriginPath"] = value["dependency_origin_path"]
    if "dependency_copy_path" in value:
        out["DependencyCopyPath"] = value["dependency_copy_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HubContentDependency:
    out: HubContentDependency = {}  # type: ignore[typeddict-item]
    if "DependencyOriginPath" in data:
        out["dependency_origin_path"] = data["DependencyOriginPath"]
    if "DependencyCopyPath" in data:
        out["dependency_copy_path"] = data["DependencyCopyPath"]
    return out
