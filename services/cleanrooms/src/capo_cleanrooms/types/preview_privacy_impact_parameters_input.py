"""Generated from Smithy shape ``com.amazonaws.cleanrooms#PreviewPrivacyImpactParametersInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.differential_privacy_preview_parameters_input


class _PreviewPrivacyImpactParametersInput_differentialPrivacy(TypedDict, closed=True):
    differentialPrivacy: "capo_cleanrooms.types.differential_privacy_preview_parameters_input.DifferentialPrivacyPreviewParametersInput"


PreviewPrivacyImpactParametersInput: TypeAlias = (
    _PreviewPrivacyImpactParametersInput_differentialPrivacy
)


# --- restJson1 ser/de ---
def serialize_json(value: PreviewPrivacyImpactParametersInput) -> dict:
    if "differentialPrivacy" in value:
        import capo_cleanrooms.types.differential_privacy_preview_parameters_input

        return {
            "differentialPrivacy": capo_cleanrooms.types.differential_privacy_preview_parameters_input.serialize_json(
                value["differentialPrivacy"]
            )
        }
    else:
        raise SerializationError(
            "PreviewPrivacyImpactParametersInput: no variant present"
        )


def deserialize_json(data: dict) -> PreviewPrivacyImpactParametersInput:
    if "differentialPrivacy" in data:
        import capo_cleanrooms.types.differential_privacy_preview_parameters_input

        return {
            "differentialPrivacy": capo_cleanrooms.types.differential_privacy_preview_parameters_input.deserialize_json(
                data["differentialPrivacy"]
            )
        }
    else:
        raise DeserializationError(
            "PreviewPrivacyImpactParametersInput: no recognized variant key"
        )
