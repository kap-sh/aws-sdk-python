"""Generated from Smithy shape ``com.amazonaws.securityhub#RecommendationError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class RecommendationError(TypedDict, closed=True):
    code: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The error code for a failed retrieval of a recommended policy for a finding.</p>"""
    message: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The error message for a failed retrieval of a recommended policy for a finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationError) -> dict:
    out: dict = {}
    if "code" in value:
        out["Code"] = value["code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RecommendationError:
    out: RecommendationError = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        out["code"] = data["Code"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
