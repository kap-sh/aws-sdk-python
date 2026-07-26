"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#PrivacyConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanroomsml.types.privacy_configuration_policies


class PrivacyConfiguration(TypedDict, closed=True):
    policies: "capo_cleanroomsml.types.privacy_configuration_policies.PrivacyConfigurationPolicies"
    """<p>The privacy configuration policies for a configured model algorithm association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrivacyConfiguration) -> dict:
    out: dict = {}
    import capo_cleanroomsml.types.privacy_configuration_policies

    out["policies"] = (
        capo_cleanroomsml.types.privacy_configuration_policies.serialize_json(
            value["policies"]
        )
    )
    return out


def deserialize_json(data: dict) -> PrivacyConfiguration:
    out: PrivacyConfiguration = {}  # type: ignore[typeddict-item]
    if "policies" in data:
        import capo_cleanroomsml.types.privacy_configuration_policies

        out["policies"] = (
            capo_cleanroomsml.types.privacy_configuration_policies.deserialize_json(
                data["policies"]
            )
        )
    else:
        raise DeserializationError("PrivacyConfiguration.policies required")
    return out
