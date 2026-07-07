"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#UtteranceList``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.list_of_utterance
    import aws_sdk_lex_model_building_service.types.version


class UtteranceList(TypedDict, closed=True):
    bot_version: NotRequired["aws_sdk_lex_model_building_service.types.version.Version"]
    """<p>The version of the bot that processed the list.</p>"""
    utterances: NotRequired[
        "aws_sdk_lex_model_building_service.types.list_of_utterance.ListOfUtterance"
    ]
    """<p>One or more <a>UtteranceData</a> objects that contain information about the utterances that have been made to a bot. The maximum number of object is 100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UtteranceList) -> dict:
    out: dict = {}
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "utterances" in value:
        import aws_sdk_lex_model_building_service.types.list_of_utterance

        out["utterances"] = (
            aws_sdk_lex_model_building_service.types.list_of_utterance.serialize_json(
                value["utterances"]
            )
        )
    return out


def deserialize_json(data: dict) -> UtteranceList:
    out: UtteranceList = {}  # type: ignore[typeddict-item]
    if "botVersion" in data:
        out["bot_version"] = data["botVersion"]
    if "utterances" in data:
        import aws_sdk_lex_model_building_service.types.list_of_utterance

        out["utterances"] = (
            aws_sdk_lex_model_building_service.types.list_of_utterance.deserialize_json(
                data["utterances"]
            )
        )
    return out
