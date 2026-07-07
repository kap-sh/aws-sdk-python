"""Generated from Smithy shape ``com.amazonaws.amplifybackend#UpdateBackendAuthPasswordPolicyConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.__double
    import aws_sdk_amplifybackend.types.list_of_additional_constraints_element


class UpdateBackendAuthPasswordPolicyConfig(TypedDict, closed=True):
    additional_constraints: NotRequired[
        "aws_sdk_amplifybackend.types.list_of_additional_constraints_element.ListOfAdditionalConstraintsElement"
    ]
    """<p>Describes additional constraints on password requirements to sign in to the auth resource, configured as a part of your Amplify project.</p>"""
    minimum_length: NotRequired["aws_sdk_amplifybackend.types.__double.__double"]
    """<p>Describes the minimum length of the password required to sign in to the auth resource, configured as a part of your Amplify project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBackendAuthPasswordPolicyConfig) -> dict:
    out: dict = {}
    if "additional_constraints" in value:
        import aws_sdk_amplifybackend.types.list_of_additional_constraints_element

        out["additionalConstraints"] = (
            aws_sdk_amplifybackend.types.list_of_additional_constraints_element.serialize_json(
                value["additional_constraints"]
            )
        )
    if "minimum_length" in value:
        out["minimumLength"] = value["minimum_length"]
    return out


def deserialize_json(data: dict) -> UpdateBackendAuthPasswordPolicyConfig:
    out: UpdateBackendAuthPasswordPolicyConfig = {}  # type: ignore[typeddict-item]
    if "additionalConstraints" in data:
        import aws_sdk_amplifybackend.types.list_of_additional_constraints_element

        out["additional_constraints"] = (
            aws_sdk_amplifybackend.types.list_of_additional_constraints_element.deserialize_json(
                data["additionalConstraints"]
            )
        )
    if "minimumLength" in data:
        out["minimum_length"] = data["minimumLength"]
    return out
