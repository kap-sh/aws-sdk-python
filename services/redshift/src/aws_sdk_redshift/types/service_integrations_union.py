"""Generated from Smithy shape ``com.amazonaws.redshift#ServiceIntegrationsUnion``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_redshift.types.lake_formation_service_integrations
    import aws_sdk_redshift.types.redshift_service_integrations
    import aws_sdk_redshift.types.s3_access_grants_service_integrations


class _ServiceIntegrationsUnion_LakeFormation(TypedDict, closed=True):
    LakeFormation: "aws_sdk_redshift.types.lake_formation_service_integrations.LakeFormationServiceIntegrations"


class _ServiceIntegrationsUnion_S3AccessGrants(TypedDict, closed=True):
    S3AccessGrants: "aws_sdk_redshift.types.s3_access_grants_service_integrations.S3AccessGrantsServiceIntegrations"


class _ServiceIntegrationsUnion_Redshift(TypedDict, closed=True):
    Redshift: "aws_sdk_redshift.types.redshift_service_integrations.RedshiftServiceIntegrations"


ServiceIntegrationsUnion: TypeAlias = (
    _ServiceIntegrationsUnion_LakeFormation
    | _ServiceIntegrationsUnion_S3AccessGrants
    | _ServiceIntegrationsUnion_Redshift
)


# --- awsQuery ser/de ---
def serialize_query(
    value: ServiceIntegrationsUnion, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "LakeFormation" in value:
        import aws_sdk_redshift.types.lake_formation_service_integrations

        aws_sdk_redshift.types.lake_formation_service_integrations.serialize_query(
            value["LakeFormation"], pairs, f"{prefix}.LakeFormation"
        )
    elif "S3AccessGrants" in value:
        import aws_sdk_redshift.types.s3_access_grants_service_integrations

        aws_sdk_redshift.types.s3_access_grants_service_integrations.serialize_query(
            value["S3AccessGrants"], pairs, f"{prefix}.S3AccessGrants"
        )
    elif "Redshift" in value:
        import aws_sdk_redshift.types.redshift_service_integrations

        aws_sdk_redshift.types.redshift_service_integrations.serialize_query(
            value["Redshift"], pairs, f"{prefix}.Redshift"
        )
    else:
        raise SerializationError("ServiceIntegrationsUnion: no variant present")


def deserialize_query(el: Element) -> ServiceIntegrationsUnion:
    for child in el:
        if child.tag == "LakeFormation":
            import aws_sdk_redshift.types.lake_formation_service_integrations

            return {
                "LakeFormation": aws_sdk_redshift.types.lake_formation_service_integrations.deserialize_query(
                    child
                )
            }
        elif child.tag == "S3AccessGrants":
            import aws_sdk_redshift.types.s3_access_grants_service_integrations

            return {
                "S3AccessGrants": aws_sdk_redshift.types.s3_access_grants_service_integrations.deserialize_query(
                    child
                )
            }
        elif child.tag == "Redshift":
            import aws_sdk_redshift.types.redshift_service_integrations

            return {
                "Redshift": aws_sdk_redshift.types.redshift_service_integrations.deserialize_query(
                    child
                )
            }
    raise DeserializationError(
        "ServiceIntegrationsUnion: no recognized variant element"
    )
