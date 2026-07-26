"""Generated from Smithy shape ``com.amazonaws.ssoadmin#TrustedTokenIssuerUpdateConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_sso_admin.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_sso_admin.types.oidc_jwt_update_configuration


class _TrustedTokenIssuerUpdateConfiguration_OidcJwtConfiguration(
    TypedDict, closed=True
):
    OidcJwtConfiguration: (
        "capo_sso_admin.types.oidc_jwt_update_configuration.OidcJwtUpdateConfiguration"
    )


TrustedTokenIssuerUpdateConfiguration: TypeAlias = (
    _TrustedTokenIssuerUpdateConfiguration_OidcJwtConfiguration
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrustedTokenIssuerUpdateConfiguration) -> dict:
    if "OidcJwtConfiguration" in value:
        import capo_sso_admin.types.oidc_jwt_update_configuration

        return {
            "OidcJwtConfiguration": capo_sso_admin.types.oidc_jwt_update_configuration.serialize_aws_json_1_1(
                value["OidcJwtConfiguration"]
            )
        }
    else:
        raise SerializationError(
            "TrustedTokenIssuerUpdateConfiguration: no variant present"
        )


def deserialize_aws_json_1_1(data: dict) -> TrustedTokenIssuerUpdateConfiguration:
    if "OidcJwtConfiguration" in data:
        import capo_sso_admin.types.oidc_jwt_update_configuration

        return {
            "OidcJwtConfiguration": capo_sso_admin.types.oidc_jwt_update_configuration.deserialize_aws_json_1_1(
                data["OidcJwtConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "TrustedTokenIssuerUpdateConfiguration: no recognized variant key"
        )
