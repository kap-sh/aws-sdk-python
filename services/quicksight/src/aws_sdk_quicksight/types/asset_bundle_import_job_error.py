"""Generated from Smithy shape ``com.amazonaws.quicksight#AssetBundleImportJobError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.non_empty_string


class AssetBundleImportJobError(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The ARN of the resource whose processing caused an error.</p>"""
    type: NotRequired["aws_sdk_quicksight.types.non_empty_string.NonEmptyString"]
    """<p>The specific error type or the error that occurred.</p>"""
    message: NotRequired["aws_sdk_quicksight.types.non_empty_string.NonEmptyString"]
    """<p>A description of the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetBundleImportJobError) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "type" in value:
        out["Type"] = value["type"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AssetBundleImportJobError:
    out: AssetBundleImportJobError = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
