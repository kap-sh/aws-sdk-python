"""Generated from Smithy shape ``com.amazonaws.comprehend#TargetedSentimentMention``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.float
    import aws_sdk_comprehend.types.integer
    import aws_sdk_comprehend.types.mention_sentiment
    import aws_sdk_comprehend.types.string
    import aws_sdk_comprehend.types.targeted_sentiment_entity_type


class TargetedSentimentMention(TypedDict):
    score: NotRequired["aws_sdk_comprehend.types.float.Float"]
    """<p>Model confidence that the entity is relevant. Value range is zero to one, where one is highest confidence.</p>"""
    group_score: NotRequired["aws_sdk_comprehend.types.float.Float"]
    """<p>The confidence that all the entities mentioned in the group relate to the same entity.</p>"""
    text: NotRequired["aws_sdk_comprehend.types.string.String"]
    """<p>The text in the document that identifies the entity.</p>"""
    type: NotRequired[
        "aws_sdk_comprehend.types.targeted_sentiment_entity_type.TargetedSentimentEntityType"
    ]
    r"""<p>The type of the entity. Amazon Comprehend supports a variety of <a href=\"https://docs.aws.amazon.com/comprehend/latest/dg/how-targeted-sentiment.html#how-targeted-sentiment-entities\">entity types</a>.</p>"""
    mention_sentiment: NotRequired[
        "aws_sdk_comprehend.types.mention_sentiment.MentionSentiment"
    ]
    """<p>Contains the sentiment and sentiment score for the mention.</p>"""
    begin_offset: NotRequired["aws_sdk_comprehend.types.integer.Integer"]
    """<p>The offset into the document text where the mention begins.</p>"""
    end_offset: NotRequired["aws_sdk_comprehend.types.integer.Integer"]
    """<p>The offset into the document text where the mention ends.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetedSentimentMention) -> dict:
    out: dict = {}
    if "score" in value:
        out["Score"] = value["score"]
    if "group_score" in value:
        out["GroupScore"] = value["group_score"]
    if "text" in value:
        out["Text"] = value["text"]
    if "type" in value:
        import aws_sdk_comprehend.types.targeted_sentiment_entity_type

        out["Type"] = (
            aws_sdk_comprehend.types.targeted_sentiment_entity_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "mention_sentiment" in value:
        import aws_sdk_comprehend.types.mention_sentiment

        out["MentionSentiment"] = (
            aws_sdk_comprehend.types.mention_sentiment.serialize_aws_json_1_1(
                value["mention_sentiment"]
            )
        )
    if "begin_offset" in value:
        out["BeginOffset"] = value["begin_offset"]
    if "end_offset" in value:
        out["EndOffset"] = value["end_offset"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetedSentimentMention:
    out: TargetedSentimentMention = {}  # type: ignore[typeddict-item]
    if "Score" in data:
        out["score"] = data["Score"]
    if "GroupScore" in data:
        out["group_score"] = data["GroupScore"]
    if "Text" in data:
        out["text"] = data["Text"]
    if "Type" in data:
        import aws_sdk_comprehend.types.targeted_sentiment_entity_type

        out["type"] = (
            aws_sdk_comprehend.types.targeted_sentiment_entity_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "MentionSentiment" in data:
        import aws_sdk_comprehend.types.mention_sentiment

        out["mention_sentiment"] = (
            aws_sdk_comprehend.types.mention_sentiment.deserialize_aws_json_1_1(
                data["MentionSentiment"]
            )
        )
    if "BeginOffset" in data:
        out["begin_offset"] = data["BeginOffset"]
    if "EndOffset" in data:
        out["end_offset"] = data["EndOffset"]
    return out
