"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ExpirationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_chime_sdk_messaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.expiration_criterion
    import capo_chime_sdk_messaging.types.expiration_days


class ExpirationSettings(TypedDict, closed=True):
    expiration_days: "capo_chime_sdk_messaging.types.expiration_days.ExpirationDays"
    """<p>The period in days after which the system automatically deletes a channel.</p>"""
    expiration_criterion: (
        "capo_chime_sdk_messaging.types.expiration_criterion.ExpirationCriterion"
    )
    """<p>The conditions that must be met for a channel to expire.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExpirationSettings) -> dict:
    out: dict = {}
    out["ExpirationDays"] = value["expiration_days"]
    import capo_chime_sdk_messaging.types.expiration_criterion

    out["ExpirationCriterion"] = (
        capo_chime_sdk_messaging.types.expiration_criterion.serialize_json(
            value["expiration_criterion"]
        )
    )
    return out


def deserialize_json(data: dict) -> ExpirationSettings:
    out: ExpirationSettings = {}  # type: ignore[typeddict-item]
    if "ExpirationDays" in data:
        out["expiration_days"] = data["ExpirationDays"]
    else:
        raise DeserializationError("ExpirationSettings.expiration_days required")
    if "ExpirationCriterion" in data:
        import capo_chime_sdk_messaging.types.expiration_criterion

        out["expiration_criterion"] = (
            capo_chime_sdk_messaging.types.expiration_criterion.deserialize_json(
                data["ExpirationCriterion"]
            )
        )
    else:
        raise DeserializationError("ExpirationSettings.expiration_criterion required")
    return out
