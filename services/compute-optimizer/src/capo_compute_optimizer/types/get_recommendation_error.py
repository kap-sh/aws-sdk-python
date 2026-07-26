"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#GetRecommendationError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.code
    import capo_compute_optimizer.types.identifier
    import capo_compute_optimizer.types.message


class GetRecommendationError(TypedDict, closed=True):
    identifier: NotRequired["capo_compute_optimizer.types.identifier.Identifier"]
    """<p>The ID of the error.</p>"""
    code: NotRequired["capo_compute_optimizer.types.code.Code"]
    """<p>The error code.</p>"""
    message: NotRequired["capo_compute_optimizer.types.message.Message"]
    """<p>The message, or reason, for the error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRecommendationError) -> dict:
    out: dict = {}
    if "identifier" in value:
        out["identifier"] = value["identifier"]
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRecommendationError:
    out: GetRecommendationError = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    if "code" in data:
        out["code"] = data["code"]
    if "message" in data:
        out["message"] = data["message"]
    return out
