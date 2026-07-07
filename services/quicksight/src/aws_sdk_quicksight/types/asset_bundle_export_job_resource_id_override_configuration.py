"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobResourceIdOverrideConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.boolean


class AssetBundleExportJobResourceIdOverrideConfiguration(TypedDict, closed=True):
    prefix_for_all_resources: "aws_sdk_quicksight.types.boolean.Boolean"
    """<p>An option to request a CloudFormation variable for a prefix to be prepended to each resource's ID before import. The prefix is only added to the asset IDs and does not change the name of the asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobResourceIdOverrideConfiguration) -> dict:
    out: dict = {}
    out["PrefixForAllResources"] = value.get("prefix_for_all_resources", False)
    return out


def deserialize_json(data: dict) -> AssetBundleExportJobResourceIdOverrideConfiguration:
    out: AssetBundleExportJobResourceIdOverrideConfiguration = {}  # type: ignore[typeddict-item]
    if "PrefixForAllResources" in data:
        out["prefix_for_all_resources"] = data["PrefixForAllResources"]
    else:
        out["prefix_for_all_resources"] = False
    return out
