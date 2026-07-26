"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#SnsTopicSinkConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.arn


class SnsTopicSinkConfiguration(TypedDict, closed=True):
    insights_target: NotRequired["capo_chime_sdk_media_pipelines.types.arn.Arn"]
    """<p>The ARN of the SNS sink.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnsTopicSinkConfiguration) -> dict:
    out: dict = {}
    if "insights_target" in value:
        out["InsightsTarget"] = value["insights_target"]
    return out


def deserialize_json(data: dict) -> SnsTopicSinkConfiguration:
    out: SnsTopicSinkConfiguration = {}  # type: ignore[typeddict-item]
    if "InsightsTarget" in data:
        out["insights_target"] = data["InsightsTarget"]
    return out
