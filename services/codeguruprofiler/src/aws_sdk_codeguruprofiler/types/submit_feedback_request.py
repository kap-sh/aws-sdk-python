"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#SubmitFeedbackRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codeguruprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.anomaly_instance_id
    import aws_sdk_codeguruprofiler.types.feedback_type
    import aws_sdk_codeguruprofiler.types.profiling_group_name


class SubmitFeedbackRequest(TypedDict, closed=True):
    profiling_group_name: (
        "aws_sdk_codeguruprofiler.types.profiling_group_name.ProfilingGroupName"
    )
    """<p>The name of the profiling group that is associated with the analysis data.</p>"""
    anomaly_instance_id: (
        "aws_sdk_codeguruprofiler.types.anomaly_instance_id.AnomalyInstanceId"
    )
    r"""<p>The universally unique identifier (UUID) of the <a href=\"https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AnomalyInstance.html\"> <code>AnomalyInstance</code> </a> object that is included in the analysis data.</p>"""
    type: "aws_sdk_codeguruprofiler.types.feedback_type.FeedbackType"
    """<p> The feedback tpye. Thee are two valid values, <code>Positive</code> and <code>Negative</code>. </p>"""
    comment: NotRequired["str"]
    """<p>Optional feedback about this anomaly.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubmitFeedbackRequest) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    if "comment" in value:
        out["comment"] = value["comment"]
    return out


def deserialize_json(data: dict) -> SubmitFeedbackRequest:
    out: SubmitFeedbackRequest = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("SubmitFeedbackRequest.type required")
    if "comment" in data:
        out["comment"] = data["comment"]
    return out
