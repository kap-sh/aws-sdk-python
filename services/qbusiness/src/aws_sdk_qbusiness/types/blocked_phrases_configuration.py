"""Generated from Smithy shape ``com.amazonaws.qbusiness#BlockedPhrasesConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.blocked_phrases
    import aws_sdk_qbusiness.types.system_message_override

class BlockedPhrasesConfiguration(TypedDict):
    blocked_phrases: NotRequired["aws_sdk_qbusiness.types.blocked_phrases.BlockedPhrases"]
    """<p>A list of phrases blocked from a Amazon Q Business web experience chat.</p> <note> <p>Each phrase can contain a maximum of 36 characters. The list can contain a maximum of 20 phrases.</p> </note>"""
    system_message_override: NotRequired["aws_sdk_qbusiness.types.system_message_override.SystemMessageOverride"]
    """<p>The configured custom message displayed to an end user informing them that they've used a blocked phrase during chat.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: BlockedPhrasesConfiguration) -> dict:
    out: dict = {}
    if "blocked_phrases" in value:
        import aws_sdk_qbusiness.types.blocked_phrases
        out["blockedPhrases"] = aws_sdk_qbusiness.types.blocked_phrases.serialize_json(value["blocked_phrases"])
    if "system_message_override" in value:
        out["systemMessageOverride"] = value["system_message_override"]
    return out


def deserialize_json(data: dict) -> BlockedPhrasesConfiguration:
    out: BlockedPhrasesConfiguration = {}  # type: ignore[typeddict-item]
    if "blockedPhrases" in data:
        import aws_sdk_qbusiness.types.blocked_phrases
        out["blocked_phrases"] = aws_sdk_qbusiness.types.blocked_phrases.deserialize_json(data["blockedPhrases"])
    if "systemMessageOverride" in data:
        out["system_message_override"] = data["systemMessageOverride"]
    return out