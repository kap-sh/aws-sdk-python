"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobResourceIdOverrideConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.string


class AssetBundleImportJobResourceIdOverrideConfiguration(TypedDict, closed=True):
    prefix_for_all_resources: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>An option to request a CloudFormation variable for a prefix to be prepended to each resource's ID before import. The prefix is only added to the asset IDs and does not change the name of the asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobResourceIdOverrideConfiguration) -> dict:
    out: dict = {}
    if "prefix_for_all_resources" in value:
        out["PrefixForAllResources"] = value["prefix_for_all_resources"]
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobResourceIdOverrideConfiguration:
    out: AssetBundleImportJobResourceIdOverrideConfiguration = {}  # type: ignore[typeddict-item]
    if "PrefixForAllResources" in data:
        out["prefix_for_all_resources"] = data["PrefixForAllResources"]
    return out
