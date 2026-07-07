"""Generated from Smithy shape ``com.amazonaws.cleanrooms#PreviewPrivacyImpactInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.membership_identifier
    import aws_sdk_cleanrooms.types.preview_privacy_impact_parameters_input


class PreviewPrivacyImpactInput(TypedDict, closed=True):
    membership_identifier: (
        "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>A unique identifier for one of your memberships for a collaboration. Accepts a membership ID.</p>"""
    parameters: "aws_sdk_cleanrooms.types.preview_privacy_impact_parameters_input.PreviewPrivacyImpactParametersInput"
    """<p>Specifies the desired epsilon and noise parameters to preview.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PreviewPrivacyImpactInput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.preview_privacy_impact_parameters_input

    out["parameters"] = (
        aws_sdk_cleanrooms.types.preview_privacy_impact_parameters_input.serialize_json(
            value["parameters"]
        )
    )
    return out


def deserialize_json(data: dict) -> PreviewPrivacyImpactInput:
    out: PreviewPrivacyImpactInput = {}  # type: ignore[typeddict-item]
    if "parameters" in data:
        import aws_sdk_cleanrooms.types.preview_privacy_impact_parameters_input

        out["parameters"] = (
            aws_sdk_cleanrooms.types.preview_privacy_impact_parameters_input.deserialize_json(
                data["parameters"]
            )
        )
    else:
        raise DeserializationError("PreviewPrivacyImpactInput.parameters required")
    return out
