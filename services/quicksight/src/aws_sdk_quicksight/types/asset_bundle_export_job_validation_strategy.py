"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobValidationStrategy``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.boolean


class AssetBundleExportJobValidationStrategy(TypedDict):
    strict_mode_for_all_resources: "aws_sdk_quicksight.types.boolean.Boolean"
    """<p>A Boolean value that indicates whether to export resources under strict or lenient mode.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobValidationStrategy) -> dict:
    out: dict = {}
    out["StrictModeForAllResources"] = value.get("strict_mode_for_all_resources", False)
    return out


def deserialize_json(data: dict) -> AssetBundleExportJobValidationStrategy:
    out: AssetBundleExportJobValidationStrategy = {}  # type: ignore[typeddict-item]
    if "StrictModeForAllResources" in data:
        out["strict_mode_for_all_resources"] = data["StrictModeForAllResources"]
    else:
        out["strict_mode_for_all_resources"] = False
    return out
