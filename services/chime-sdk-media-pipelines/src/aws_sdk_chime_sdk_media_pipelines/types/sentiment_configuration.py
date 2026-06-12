"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#SentimentConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.rule_name
    import aws_sdk_chime_sdk_media_pipelines.types.sentiment_time_period_in_seconds
    import aws_sdk_chime_sdk_media_pipelines.types.sentiment_type


class SentimentConfiguration(TypedDict):
    rule_name: "aws_sdk_chime_sdk_media_pipelines.types.rule_name.RuleName"
    """<p>The name of the rule in the sentiment configuration.</p>"""
    sentiment_type: (
        "aws_sdk_chime_sdk_media_pipelines.types.sentiment_type.SentimentType"
    )
    """<p>The type of sentiment, <code>POSITIVE</code>, <code>NEGATIVE</code>, or <code>NEUTRAL</code>.</p>"""
    time_period: "aws_sdk_chime_sdk_media_pipelines.types.sentiment_time_period_in_seconds.SentimentTimePeriodInSeconds"
    """<p>Specifies the analysis interval.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SentimentConfiguration) -> dict:
    out: dict = {}
    out["RuleName"] = value["rule_name"]
    import aws_sdk_chime_sdk_media_pipelines.types.sentiment_type

    out["SentimentType"] = (
        aws_sdk_chime_sdk_media_pipelines.types.sentiment_type.serialize_json(
            value["sentiment_type"]
        )
    )
    out["TimePeriod"] = value["time_period"]
    return out


def deserialize_json(data: dict) -> SentimentConfiguration:
    out: SentimentConfiguration = {}  # type: ignore[typeddict-item]
    if "RuleName" in data:
        out["rule_name"] = data["RuleName"]
    else:
        raise DeserializationError("SentimentConfiguration.rule_name required")
    if "SentimentType" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.sentiment_type

        out["sentiment_type"] = (
            aws_sdk_chime_sdk_media_pipelines.types.sentiment_type.deserialize_json(
                data["SentimentType"]
            )
        )
    else:
        raise DeserializationError("SentimentConfiguration.sentiment_type required")
    if "TimePeriod" in data:
        out["time_period"] = data["TimePeriod"]
    else:
        raise DeserializationError("SentimentConfiguration.time_period required")
    return out
