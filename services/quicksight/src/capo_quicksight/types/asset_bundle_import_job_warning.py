"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobWarning``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.non_empty_string


class AssetBundleImportJobWarning(TypedDict, closed=True):
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The ARN of the resource that the warning occurred for.</p>"""
    message: NotRequired["capo_quicksight.types.non_empty_string.NonEmptyString"]
    """<p>A description of the warning that occurred during an Asset Bundle import job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobWarning) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobWarning:
    out: AssetBundleImportJobWarning = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
