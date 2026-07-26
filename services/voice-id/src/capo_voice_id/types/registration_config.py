"""Generated from Smithy shape ``com.amazonaws.voiceid#RegistrationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.duplicate_registration_action
    import capo_voice_id.types.registration_config_watchlist_ids
    import capo_voice_id.types.score


class RegistrationConfig(TypedDict, closed=True):
    duplicate_registration_action: NotRequired[
        "capo_voice_id.types.duplicate_registration_action.DuplicateRegistrationAction"
    ]
    """<p>The action to take when a fraudster is identified as a duplicate. The default action is <code>SKIP</code>, which skips registering the duplicate fraudster. Setting the value to <code>REGISTER_AS_NEW</code> always registers a new fraudster into the specified domain.</p>"""
    fraudster_similarity_threshold: NotRequired["capo_voice_id.types.score.Score"]
    """<p>The minimum similarity score between the new and old fraudsters in order to consider the new fraudster a duplicate.</p>"""
    watchlist_ids: NotRequired[
        "capo_voice_id.types.registration_config_watchlist_ids.RegistrationConfigWatchlistIds"
    ]
    """<p>The identifiers of watchlists that a fraudster is registered to. If a watchlist isn't provided, the fraudsters are registered to the default watchlist. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegistrationConfig) -> dict:
    out: dict = {}
    if "duplicate_registration_action" in value:
        out["DuplicateRegistrationAction"] = value["duplicate_registration_action"]
    if "fraudster_similarity_threshold" in value:
        out["FraudsterSimilarityThreshold"] = value["fraudster_similarity_threshold"]
    if "watchlist_ids" in value:
        import capo_voice_id.types.registration_config_watchlist_ids

        out["WatchlistIds"] = (
            capo_voice_id.types.registration_config_watchlist_ids.serialize_aws_json_1_0(
                value["watchlist_ids"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RegistrationConfig:
    out: RegistrationConfig = {}  # type: ignore[typeddict-item]
    if "DuplicateRegistrationAction" in data:
        out["duplicate_registration_action"] = data["DuplicateRegistrationAction"]
    if "FraudsterSimilarityThreshold" in data:
        out["fraudster_similarity_threshold"] = data["FraudsterSimilarityThreshold"]
    if "WatchlistIds" in data:
        import capo_voice_id.types.registration_config_watchlist_ids

        out["watchlist_ids"] = (
            capo_voice_id.types.registration_config_watchlist_ids.deserialize_aws_json_1_0(
                data["WatchlistIds"]
            )
        )
    return out
