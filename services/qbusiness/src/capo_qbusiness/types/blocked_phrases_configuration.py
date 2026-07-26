"""Generated from Smithy shape ``com.amazonaws.qbusiness#BlockedPhrasesConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.blocked_phrases
    import capo_qbusiness.types.system_message_override


class BlockedPhrasesConfiguration(TypedDict, closed=True):
    blocked_phrases: NotRequired["capo_qbusiness.types.blocked_phrases.BlockedPhrases"]
    """<p>A list of phrases blocked from a Amazon Q Business web experience chat.</p> <note> <p>Each phrase can contain a maximum of 36 characters. The list can contain a maximum of 20 phrases.</p> </note>"""
    system_message_override: NotRequired[
        "capo_qbusiness.types.system_message_override.SystemMessageOverride"
    ]
    """<p>The configured custom message displayed to an end user informing them that they've used a blocked phrase during chat.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BlockedPhrasesConfiguration) -> dict:
    out: dict = {}
    if "blocked_phrases" in value:
        import capo_qbusiness.types.blocked_phrases

        out["blockedPhrases"] = capo_qbusiness.types.blocked_phrases.serialize_json(
            value["blocked_phrases"]
        )
    if "system_message_override" in value:
        out["systemMessageOverride"] = value["system_message_override"]
    return out


def deserialize_json(data: dict) -> BlockedPhrasesConfiguration:
    out: BlockedPhrasesConfiguration = {}  # type: ignore[typeddict-item]
    if "blockedPhrases" in data:
        import capo_qbusiness.types.blocked_phrases

        out["blocked_phrases"] = capo_qbusiness.types.blocked_phrases.deserialize_json(
            data["blockedPhrases"]
        )
    if "systemMessageOverride" in data:
        out["system_message_override"] = data["systemMessageOverride"]
    return out
