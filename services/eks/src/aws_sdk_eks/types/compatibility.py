"""Generated from Smithy shape ``com.amazonaws.eks#Compatibility``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eks.types.boolean
    import aws_sdk_eks.types.string
    import aws_sdk_eks.types.string_list


class Compatibility(TypedDict, closed=True):
    cluster_version: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The supported Kubernetes version of the cluster.</p>"""
    platform_versions: NotRequired["aws_sdk_eks.types.string_list.StringList"]
    """<p>The supported compute platform.</p>"""
    default_version: "aws_sdk_eks.types.boolean.Boolean"
    """<p>The supported default version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Compatibility) -> dict:
    out: dict = {}
    if "cluster_version" in value:
        out["clusterVersion"] = value["cluster_version"]
    if "platform_versions" in value:
        import aws_sdk_eks.types.string_list

        out["platformVersions"] = aws_sdk_eks.types.string_list.serialize_json(
            value["platform_versions"]
        )
    out["defaultVersion"] = value.get("default_version", False)
    return out


def deserialize_json(data: dict) -> Compatibility:
    out: Compatibility = {}  # type: ignore[typeddict-item]
    if "clusterVersion" in data:
        out["cluster_version"] = data["clusterVersion"]
    if "platformVersions" in data:
        import aws_sdk_eks.types.string_list

        out["platform_versions"] = aws_sdk_eks.types.string_list.deserialize_json(
            data["platformVersions"]
        )
    if "defaultVersion" in data:
        out["default_version"] = data["defaultVersion"]
    else:
        out["default_version"] = False
    return out
