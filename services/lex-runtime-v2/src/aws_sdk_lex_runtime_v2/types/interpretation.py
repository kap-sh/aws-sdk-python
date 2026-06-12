"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#Interpretation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_v2.types.confidence_score
    import aws_sdk_lex_runtime_v2.types.intent
    import aws_sdk_lex_runtime_v2.types.interpretation_source
    import aws_sdk_lex_runtime_v2.types.sentiment_response


class Interpretation(TypedDict):
    nlu_confidence: NotRequired[
        "aws_sdk_lex_runtime_v2.types.confidence_score.ConfidenceScore"
    ]
    """<p>Determines the threshold where Amazon Lex V2 will insert the <code>AMAZON.FallbackIntent</code>, <code>AMAZON.KendraSearchIntent</code>, or both when returning alternative intents in a response. <code>AMAZON.FallbackIntent</code> and <code>AMAZON.KendraSearchIntent</code> are only inserted if they are configured for the bot.</p>"""
    sentiment_response: NotRequired[
        "aws_sdk_lex_runtime_v2.types.sentiment_response.SentimentResponse"
    ]
    """<p>The sentiment expressed in an utterance. </p> <p>When the bot is configured to send utterances to Amazon Comprehend for sentiment analysis, this field contains the result of the analysis.</p>"""
    intent: NotRequired["aws_sdk_lex_runtime_v2.types.intent.Intent"]
    """<p>A list of intents that might satisfy the user's utterance. The intents are ordered by the confidence score.</p>"""
    interpretation_source: NotRequired[
        "aws_sdk_lex_runtime_v2.types.interpretation_source.InterpretationSource"
    ]
    """<p>Specifies the service that interpreted the input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Interpretation) -> dict:
    out: dict = {}
    if "nlu_confidence" in value:
        import aws_sdk_lex_runtime_v2.types.confidence_score

        out["nluConfidence"] = (
            aws_sdk_lex_runtime_v2.types.confidence_score.serialize_json(
                value["nlu_confidence"]
            )
        )
    if "sentiment_response" in value:
        import aws_sdk_lex_runtime_v2.types.sentiment_response

        out["sentimentResponse"] = (
            aws_sdk_lex_runtime_v2.types.sentiment_response.serialize_json(
                value["sentiment_response"]
            )
        )
    if "intent" in value:
        import aws_sdk_lex_runtime_v2.types.intent

        out["intent"] = aws_sdk_lex_runtime_v2.types.intent.serialize_json(
            value["intent"]
        )
    if "interpretation_source" in value:
        import aws_sdk_lex_runtime_v2.types.interpretation_source

        out["interpretationSource"] = (
            aws_sdk_lex_runtime_v2.types.interpretation_source.serialize_json(
                value["interpretation_source"]
            )
        )
    return out


def deserialize_json(data: dict) -> Interpretation:
    out: Interpretation = {}  # type: ignore[typeddict-item]
    if "nluConfidence" in data:
        import aws_sdk_lex_runtime_v2.types.confidence_score

        out["nlu_confidence"] = (
            aws_sdk_lex_runtime_v2.types.confidence_score.deserialize_json(
                data["nluConfidence"]
            )
        )
    if "sentimentResponse" in data:
        import aws_sdk_lex_runtime_v2.types.sentiment_response

        out["sentiment_response"] = (
            aws_sdk_lex_runtime_v2.types.sentiment_response.deserialize_json(
                data["sentimentResponse"]
            )
        )
    if "intent" in data:
        import aws_sdk_lex_runtime_v2.types.intent

        out["intent"] = aws_sdk_lex_runtime_v2.types.intent.deserialize_json(
            data["intent"]
        )
    if "interpretationSource" in data:
        import aws_sdk_lex_runtime_v2.types.interpretation_source

        out["interpretation_source"] = (
            aws_sdk_lex_runtime_v2.types.interpretation_source.deserialize_json(
                data["interpretationSource"]
            )
        )
    return out
