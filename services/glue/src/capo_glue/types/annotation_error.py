"""Generated from Smithy shape ``com.amazonaws.glue#AnnotationError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.description_string
    import capo_glue.types.hash_string


class AnnotationError(TypedDict, closed=True):
    profile_id: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>The Profile ID for the failed annotation.</p>"""
    statistic_id: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>The Statistic ID for the failed annotation.</p>"""
    failure_reason: NotRequired["capo_glue.types.description_string.DescriptionString"]
    """<p>The reason why the annotation failed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AnnotationError) -> dict:
    out: dict = {}
    if "profile_id" in value:
        out["ProfileId"] = value["profile_id"]
    if "statistic_id" in value:
        out["StatisticId"] = value["statistic_id"]
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AnnotationError:
    out: AnnotationError = {}  # type: ignore[typeddict-item]
    if "ProfileId" in data:
        out["profile_id"] = data["ProfileId"]
    if "StatisticId" in data:
        out["statistic_id"] = data["StatisticId"]
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    return out
