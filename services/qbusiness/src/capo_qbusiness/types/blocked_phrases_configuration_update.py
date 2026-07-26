"""Generated from Smithy shape ``com.amazonaws.qbusiness#BlockedPhrasesConfigurationUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.blocked_phrases
    import capo_qbusiness.types.system_message_override


class BlockedPhrasesConfigurationUpdate(TypedDict, closed=True):
    blocked_phrases_to_create_or_update: NotRequired[
        "capo_qbusiness.types.blocked_phrases.BlockedPhrases"
    ]
    """<p>Creates or updates a blocked phrases configuration in your Amazon Q Business application.</p>"""
    blocked_phrases_to_delete: NotRequired[
        "capo_qbusiness.types.blocked_phrases.BlockedPhrases"
    ]
    """<p>Deletes a blocked phrases configuration in your Amazon Q Business application.</p>"""
    system_message_override: NotRequired[
        "capo_qbusiness.types.system_message_override.SystemMessageOverride"
    ]
    """<p>The configured custom message displayed to your end user when they use blocked phrase during chat.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BlockedPhrasesConfigurationUpdate) -> dict:
    out: dict = {}
    if "blocked_phrases_to_create_or_update" in value:
        import capo_qbusiness.types.blocked_phrases

        out["blockedPhrasesToCreateOrUpdate"] = (
            capo_qbusiness.types.blocked_phrases.serialize_json(
                value["blocked_phrases_to_create_or_update"]
            )
        )
    if "blocked_phrases_to_delete" in value:
        import capo_qbusiness.types.blocked_phrases

        out["blockedPhrasesToDelete"] = (
            capo_qbusiness.types.blocked_phrases.serialize_json(
                value["blocked_phrases_to_delete"]
            )
        )
    if "system_message_override" in value:
        out["systemMessageOverride"] = value["system_message_override"]
    return out


def deserialize_json(data: dict) -> BlockedPhrasesConfigurationUpdate:
    out: BlockedPhrasesConfigurationUpdate = {}  # type: ignore[typeddict-item]
    if "blockedPhrasesToCreateOrUpdate" in data:
        import capo_qbusiness.types.blocked_phrases

        out["blocked_phrases_to_create_or_update"] = (
            capo_qbusiness.types.blocked_phrases.deserialize_json(
                data["blockedPhrasesToCreateOrUpdate"]
            )
        )
    if "blockedPhrasesToDelete" in data:
        import capo_qbusiness.types.blocked_phrases

        out["blocked_phrases_to_delete"] = (
            capo_qbusiness.types.blocked_phrases.deserialize_json(
                data["blockedPhrasesToDelete"]
            )
        )
    if "systemMessageOverride" in data:
        out["system_message_override"] = data["systemMessageOverride"]
    return out
