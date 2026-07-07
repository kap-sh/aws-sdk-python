"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#SqsQueueSinkConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.arn


class SqsQueueSinkConfiguration(TypedDict, closed=True):
    insights_target: NotRequired["aws_sdk_chime_sdk_media_pipelines.types.arn.Arn"]
    """<p>The ARN of the SQS sink.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SqsQueueSinkConfiguration) -> dict:
    out: dict = {}
    if "insights_target" in value:
        out["InsightsTarget"] = value["insights_target"]
    return out


def deserialize_json(data: dict) -> SqsQueueSinkConfiguration:
    out: SqsQueueSinkConfiguration = {}  # type: ignore[typeddict-item]
    if "InsightsTarget" in data:
        out["insights_target"] = data["InsightsTarget"]
    return out
