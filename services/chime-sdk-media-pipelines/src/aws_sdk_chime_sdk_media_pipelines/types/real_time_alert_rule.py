"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#RealTimeAlertRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.issue_detection_configuration
    import aws_sdk_chime_sdk_media_pipelines.types.keyword_match_configuration
    import aws_sdk_chime_sdk_media_pipelines.types.real_time_alert_rule_type
    import aws_sdk_chime_sdk_media_pipelines.types.sentiment_configuration


class RealTimeAlertRule(TypedDict, closed=True):
    type: "aws_sdk_chime_sdk_media_pipelines.types.real_time_alert_rule_type.RealTimeAlertRuleType"
    """<p>The type of alert rule.</p>"""
    keyword_match_configuration: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.keyword_match_configuration.KeywordMatchConfiguration"
    ]
    """<p>Specifies the settings for matching the keywords in a real-time alert rule.</p>"""
    sentiment_configuration: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.sentiment_configuration.SentimentConfiguration"
    ]
    """<p>Specifies the settings for predicting sentiment in a real-time alert rule.</p>"""
    issue_detection_configuration: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.issue_detection_configuration.IssueDetectionConfiguration"
    ]
    """<p>Specifies the issue detection settings for a real-time alert rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeAlertRule) -> dict:
    out: dict = {}
    import aws_sdk_chime_sdk_media_pipelines.types.real_time_alert_rule_type

    out["Type"] = (
        aws_sdk_chime_sdk_media_pipelines.types.real_time_alert_rule_type.serialize_json(
            value["type"]
        )
    )
    if "keyword_match_configuration" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.keyword_match_configuration

        out["KeywordMatchConfiguration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.keyword_match_configuration.serialize_json(
                value["keyword_match_configuration"]
            )
        )
    if "sentiment_configuration" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.sentiment_configuration

        out["SentimentConfiguration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.sentiment_configuration.serialize_json(
                value["sentiment_configuration"]
            )
        )
    if "issue_detection_configuration" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.issue_detection_configuration

        out["IssueDetectionConfiguration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.issue_detection_configuration.serialize_json(
                value["issue_detection_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> RealTimeAlertRule:
    out: RealTimeAlertRule = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.real_time_alert_rule_type

        out["type"] = (
            aws_sdk_chime_sdk_media_pipelines.types.real_time_alert_rule_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("RealTimeAlertRule.type required")
    if "KeywordMatchConfiguration" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.keyword_match_configuration

        out["keyword_match_configuration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.keyword_match_configuration.deserialize_json(
                data["KeywordMatchConfiguration"]
            )
        )
    if "SentimentConfiguration" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.sentiment_configuration

        out["sentiment_configuration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.sentiment_configuration.deserialize_json(
                data["SentimentConfiguration"]
            )
        )
    if "IssueDetectionConfiguration" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.issue_detection_configuration

        out["issue_detection_configuration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.issue_detection_configuration.deserialize_json(
                data["IssueDetectionConfiguration"]
            )
        )
    return out
