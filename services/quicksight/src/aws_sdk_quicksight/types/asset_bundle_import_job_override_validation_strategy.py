"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobOverrideValidationStrategy``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.boolean


class AssetBundleImportJobOverrideValidationStrategy(TypedDict):
    strict_mode_for_all_resources: "aws_sdk_quicksight.types.boolean.Boolean"
    """<p>A Boolean value that indicates whether to import all analyses and dashboards under strict or lenient mode.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobOverrideValidationStrategy) -> dict:
    out: dict = {}
    out["StrictModeForAllResources"] = value.get("strict_mode_for_all_resources", False)
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobOverrideValidationStrategy:
    out: AssetBundleImportJobOverrideValidationStrategy = {}  # type: ignore[typeddict-item]
    if "StrictModeForAllResources" in data:
        out["strict_mode_for_all_resources"] = data["StrictModeForAllResources"]
    else:
        out["strict_mode_for_all_resources"] = False
    return out
