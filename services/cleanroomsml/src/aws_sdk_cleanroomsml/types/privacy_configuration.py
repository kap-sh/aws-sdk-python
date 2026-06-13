"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#PrivacyConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.privacy_configuration_policies


class PrivacyConfiguration(TypedDict):
    policies: "aws_sdk_cleanroomsml.types.privacy_configuration_policies.PrivacyConfigurationPolicies"
    """<p>The privacy configuration policies for a configured model algorithm association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrivacyConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_cleanroomsml.types.privacy_configuration_policies

    out["policies"] = (
        aws_sdk_cleanroomsml.types.privacy_configuration_policies.serialize_json(
            value["policies"]
        )
    )
    return out


def deserialize_json(data: dict) -> PrivacyConfiguration:
    out: PrivacyConfiguration = {}  # type: ignore[typeddict-item]
    if "policies" in data:
        import aws_sdk_cleanroomsml.types.privacy_configuration_policies

        out["policies"] = (
            aws_sdk_cleanroomsml.types.privacy_configuration_policies.deserialize_json(
                data["policies"]
            )
        )
    else:
        raise DeserializationError("PrivacyConfiguration.policies required")
    return out
