"""Generated from Smithy shape ``com.amazonaws.qbusiness#WebExperienceAuthConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_qbusiness.types.saml_configuration


class _WebExperienceAuthConfiguration_samlConfiguration(TypedDict, closed=True):
    samlConfiguration: "capo_qbusiness.types.saml_configuration.SamlConfiguration"


WebExperienceAuthConfiguration: TypeAlias = (
    _WebExperienceAuthConfiguration_samlConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: WebExperienceAuthConfiguration) -> dict:
    if "samlConfiguration" in value:
        import capo_qbusiness.types.saml_configuration

        return {
            "samlConfiguration": capo_qbusiness.types.saml_configuration.serialize_json(
                value["samlConfiguration"]
            )
        }
    else:
        raise SerializationError("WebExperienceAuthConfiguration: no variant present")


def deserialize_json(data: dict) -> WebExperienceAuthConfiguration:
    if "samlConfiguration" in data:
        import capo_qbusiness.types.saml_configuration

        return {
            "samlConfiguration": capo_qbusiness.types.saml_configuration.deserialize_json(
                data["samlConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "WebExperienceAuthConfiguration: no recognized variant key"
        )
