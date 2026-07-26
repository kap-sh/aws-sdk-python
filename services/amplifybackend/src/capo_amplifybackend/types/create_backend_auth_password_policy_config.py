"""Generated from Smithy shape ``com.amazonaws.amplifybackend#CreateBackendAuthPasswordPolicyConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifybackend.types.__double
    import capo_amplifybackend.types.list_of_additional_constraints_element


class CreateBackendAuthPasswordPolicyConfig(TypedDict, closed=True):
    additional_constraints: NotRequired[
        "capo_amplifybackend.types.list_of_additional_constraints_element.ListOfAdditionalConstraintsElement"
    ]
    """<p>Additional constraints for the password used to access the backend of your Amplify project.</p>"""
    minimum_length: NotRequired["capo_amplifybackend.types.__double.__double"]
    """<p>The minimum length of the password used to access the backend of your Amplify project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBackendAuthPasswordPolicyConfig) -> dict:
    out: dict = {}
    if "additional_constraints" in value:
        import capo_amplifybackend.types.list_of_additional_constraints_element

        out["additionalConstraints"] = (
            capo_amplifybackend.types.list_of_additional_constraints_element.serialize_json(
                value["additional_constraints"]
            )
        )
    if "minimum_length" in value:
        out["minimumLength"] = value["minimum_length"]
    return out


def deserialize_json(data: dict) -> CreateBackendAuthPasswordPolicyConfig:
    out: CreateBackendAuthPasswordPolicyConfig = {}  # type: ignore[typeddict-item]
    if "additionalConstraints" in data:
        import capo_amplifybackend.types.list_of_additional_constraints_element

        out["additional_constraints"] = (
            capo_amplifybackend.types.list_of_additional_constraints_element.deserialize_json(
                data["additionalConstraints"]
            )
        )
    if "minimumLength" in data:
        out["minimum_length"] = data["minimumLength"]
    return out
