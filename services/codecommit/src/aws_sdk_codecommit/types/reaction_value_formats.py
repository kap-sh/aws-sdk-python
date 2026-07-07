"""Generated from Smithy shape ``com.amazonaws.codecommit#ReactionValueFormats``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.reaction_emoji
    import aws_sdk_codecommit.types.reaction_short_code
    import aws_sdk_codecommit.types.reaction_unicode


class ReactionValueFormats(TypedDict, closed=True):
    emoji: NotRequired["aws_sdk_codecommit.types.reaction_emoji.ReactionEmoji"]
    """<p>The Emoji Version 1.0 graphic of the reaction. These graphics are interpreted slightly differently on different operating systems.</p>"""
    short_code: NotRequired[
        "aws_sdk_codecommit.types.reaction_short_code.ReactionShortCode"
    ]
    """<p>The emoji short code for the reaction. Short codes are interpreted slightly differently on different operating systems. </p>"""
    unicode: NotRequired["aws_sdk_codecommit.types.reaction_unicode.ReactionUnicode"]
    """<p>The Unicode codepoint for the reaction.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReactionValueFormats) -> dict:
    out: dict = {}
    if "emoji" in value:
        out["emoji"] = value["emoji"]
    if "short_code" in value:
        out["shortCode"] = value["short_code"]
    if "unicode" in value:
        out["unicode"] = value["unicode"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReactionValueFormats:
    out: ReactionValueFormats = {}  # type: ignore[typeddict-item]
    if "emoji" in data:
        out["emoji"] = data["emoji"]
    if "shortCode" in data:
        out["short_code"] = data["shortCode"]
    if "unicode" in data:
        out["unicode"] = data["unicode"]
    return out
