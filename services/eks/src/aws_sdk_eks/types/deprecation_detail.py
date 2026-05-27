"""Generated from Smithy shape ``com.amazonaws.eks#DeprecationDetail``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.client_stats
    import aws_sdk_eks.types.string


class DeprecationDetail(TypedDict):
    usage: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The deprecated version of the resource.</p>"""
    replaced_with: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The newer version of the resource to migrate to if applicable. </p>"""
    stop_serving_version: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The version of the software where the deprecated resource version will stop being served.</p>"""
    start_serving_replacement_version: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The version of the software where the newer resource version became available to migrate to if applicable.</p>"""
    client_stats: NotRequired["aws_sdk_eks.types.client_stats.ClientStats"]
    """<p>Details about Kubernetes clients using the deprecated resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeprecationDetail) -> dict:
    out: dict = {}
    if "usage" in value:
        out["usage"] = value["usage"]
    if "replaced_with" in value:
        out["replacedWith"] = value["replaced_with"]
    if "stop_serving_version" in value:
        out["stopServingVersion"] = value["stop_serving_version"]
    if "start_serving_replacement_version" in value:
        out["startServingReplacementVersion"] = value[
            "start_serving_replacement_version"
        ]
    if "client_stats" in value:
        import aws_sdk_eks.types.client_stats

        out["clientStats"] = aws_sdk_eks.types.client_stats.serialize_json(
            value["client_stats"]
        )
    return out


def deserialize_json(data: dict) -> DeprecationDetail:
    out: DeprecationDetail = {}  # type: ignore[typeddict-item]
    if "usage" in data:
        out["usage"] = data["usage"]
    if "replacedWith" in data:
        out["replaced_with"] = data["replacedWith"]
    if "stopServingVersion" in data:
        out["stop_serving_version"] = data["stopServingVersion"]
    if "startServingReplacementVersion" in data:
        out["start_serving_replacement_version"] = data[
            "startServingReplacementVersion"
        ]
    if "clientStats" in data:
        import aws_sdk_eks.types.client_stats

        out["client_stats"] = aws_sdk_eks.types.client_stats.deserialize_json(
            data["clientStats"]
        )
    return out
