"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobWarning``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.non_empty_string


class AssetBundleExportJobWarning(TypedDict):
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The ARN of the resource whose processing caused a warning.</p>"""
    message: NotRequired["aws_sdk_quicksight.types.non_empty_string.NonEmptyString"]
    """<p>A description of the warning.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobWarning) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AssetBundleExportJobWarning:
    out: AssetBundleExportJobWarning = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
