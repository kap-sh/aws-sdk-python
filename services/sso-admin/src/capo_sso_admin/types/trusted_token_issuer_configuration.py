"""Generated from Smithy shape ``com.amazonaws.ssoadmin#TrustedTokenIssuerConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_sso_admin.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_sso_admin.types.oidc_jwt_configuration


class _TrustedTokenIssuerConfiguration_OidcJwtConfiguration(TypedDict, closed=True):
    OidcJwtConfiguration: (
        "capo_sso_admin.types.oidc_jwt_configuration.OidcJwtConfiguration"
    )


TrustedTokenIssuerConfiguration: TypeAlias = (
    _TrustedTokenIssuerConfiguration_OidcJwtConfiguration
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrustedTokenIssuerConfiguration) -> dict:
    if "OidcJwtConfiguration" in value:
        import capo_sso_admin.types.oidc_jwt_configuration

        return {
            "OidcJwtConfiguration": capo_sso_admin.types.oidc_jwt_configuration.serialize_aws_json_1_1(
                value["OidcJwtConfiguration"]
            )
        }
    else:
        raise SerializationError("TrustedTokenIssuerConfiguration: no variant present")


def deserialize_aws_json_1_1(data: dict) -> TrustedTokenIssuerConfiguration:
    if "OidcJwtConfiguration" in data:
        import capo_sso_admin.types.oidc_jwt_configuration

        return {
            "OidcJwtConfiguration": capo_sso_admin.types.oidc_jwt_configuration.deserialize_aws_json_1_1(
                data["OidcJwtConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "TrustedTokenIssuerConfiguration: no recognized variant key"
        )
