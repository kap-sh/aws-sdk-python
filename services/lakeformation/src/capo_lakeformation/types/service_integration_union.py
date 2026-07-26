"""Generated from Smithy shape ``com.amazonaws.lakeformation#ServiceIntegrationUnion``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_lakeformation.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_lakeformation.types.redshift_service_integrations


class _ServiceIntegrationUnion_Redshift(TypedDict, closed=True):
    Redshift: "capo_lakeformation.types.redshift_service_integrations.RedshiftServiceIntegrations"


ServiceIntegrationUnion: TypeAlias = _ServiceIntegrationUnion_Redshift


# --- restJson1 ser/de ---
def serialize_json(value: ServiceIntegrationUnion) -> dict:
    if "Redshift" in value:
        import capo_lakeformation.types.redshift_service_integrations

        return {
            "Redshift": capo_lakeformation.types.redshift_service_integrations.serialize_json(
                value["Redshift"]
            )
        }
    else:
        raise SerializationError("ServiceIntegrationUnion: no variant present")


def deserialize_json(data: dict) -> ServiceIntegrationUnion:
    if "Redshift" in data:
        import capo_lakeformation.types.redshift_service_integrations

        return {
            "Redshift": capo_lakeformation.types.redshift_service_integrations.deserialize_json(
                data["Redshift"]
            )
        }
    else:
        raise DeserializationError("ServiceIntegrationUnion: no recognized variant key")
