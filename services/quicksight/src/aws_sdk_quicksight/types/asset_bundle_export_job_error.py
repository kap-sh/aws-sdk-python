"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleExportJobError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.non_empty_string


class AssetBundleExportJobError(TypedDict):
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The ARN of the resource whose processing caused an error.</p>"""
    type: NotRequired["aws_sdk_quicksight.types.non_empty_string.NonEmptyString"]
    """<p>The specific error type of the error that occurred.</p>"""
    message: NotRequired["aws_sdk_quicksight.types.non_empty_string.NonEmptyString"]
    """<p>A description of the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleExportJobError) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AssetBundleExportJobError:
    out: AssetBundleExportJobError = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
