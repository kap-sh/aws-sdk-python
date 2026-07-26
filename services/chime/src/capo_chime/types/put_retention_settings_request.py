"""Generated from Smithy shape ``com.amazonaws.chime#PutRetentionSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_chime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime.types.non_empty_string
    import capo_chime.types.retention_settings


class PutRetentionSettingsRequest(TypedDict, closed=True):
    account_id: "capo_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    retention_settings: "capo_chime.types.retention_settings.RetentionSettings"
    """<p>The retention settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutRetentionSettingsRequest) -> dict:
    out: dict = {}
    import capo_chime.types.retention_settings

    out["RetentionSettings"] = capo_chime.types.retention_settings.serialize_json(
        value["retention_settings"]
    )
    return out


def deserialize_json(data: dict) -> PutRetentionSettingsRequest:
    out: PutRetentionSettingsRequest = {}  # type: ignore[typeddict-item]
    if "RetentionSettings" in data:
        import capo_chime.types.retention_settings

        out["retention_settings"] = (
            capo_chime.types.retention_settings.deserialize_json(
                data["RetentionSettings"]
            )
        )
    else:
        raise DeserializationError(
            "PutRetentionSettingsRequest.retention_settings required"
        )
    return out
