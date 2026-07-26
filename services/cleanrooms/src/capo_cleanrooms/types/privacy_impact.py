"""Generated from Smithy shape ``com.amazonaws.cleanrooms#PrivacyImpact``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.differential_privacy_privacy_impact


class _PrivacyImpact_differentialPrivacy(TypedDict, closed=True):
    differentialPrivacy: "capo_cleanrooms.types.differential_privacy_privacy_impact.DifferentialPrivacyPrivacyImpact"


PrivacyImpact: TypeAlias = _PrivacyImpact_differentialPrivacy


# --- restJson1 ser/de ---
def serialize_json(value: PrivacyImpact) -> dict:
    if "differentialPrivacy" in value:
        import capo_cleanrooms.types.differential_privacy_privacy_impact

        return {
            "differentialPrivacy": capo_cleanrooms.types.differential_privacy_privacy_impact.serialize_json(
                value["differentialPrivacy"]
            )
        }
    else:
        raise SerializationError("PrivacyImpact: no variant present")


def deserialize_json(data: dict) -> PrivacyImpact:
    if "differentialPrivacy" in data:
        import capo_cleanrooms.types.differential_privacy_privacy_impact

        return {
            "differentialPrivacy": capo_cleanrooms.types.differential_privacy_privacy_impact.deserialize_json(
                data["differentialPrivacy"]
            )
        }
    else:
        raise DeserializationError("PrivacyImpact: no recognized variant key")
