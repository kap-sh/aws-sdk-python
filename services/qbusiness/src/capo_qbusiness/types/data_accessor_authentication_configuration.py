"""Generated from Smithy shape ``com.amazonaws.qbusiness#DataAccessorAuthenticationConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_qbusiness.types.data_accessor_idc_trusted_token_issuer_configuration


class _DataAccessorAuthenticationConfiguration_idcTrustedTokenIssuerConfiguration(
    TypedDict, closed=True
):
    idcTrustedTokenIssuerConfiguration: "capo_qbusiness.types.data_accessor_idc_trusted_token_issuer_configuration.DataAccessorIdcTrustedTokenIssuerConfiguration"


DataAccessorAuthenticationConfiguration: TypeAlias = (
    _DataAccessorAuthenticationConfiguration_idcTrustedTokenIssuerConfiguration
)


# --- restJson1 ser/de ---
def serialize_json(value: DataAccessorAuthenticationConfiguration) -> dict:
    if "idcTrustedTokenIssuerConfiguration" in value:
        import capo_qbusiness.types.data_accessor_idc_trusted_token_issuer_configuration

        return {
            "idcTrustedTokenIssuerConfiguration": capo_qbusiness.types.data_accessor_idc_trusted_token_issuer_configuration.serialize_json(
                value["idcTrustedTokenIssuerConfiguration"]
            )
        }
    else:
        raise SerializationError(
            "DataAccessorAuthenticationConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> DataAccessorAuthenticationConfiguration:
    if "idcTrustedTokenIssuerConfiguration" in data:
        import capo_qbusiness.types.data_accessor_idc_trusted_token_issuer_configuration

        return {
            "idcTrustedTokenIssuerConfiguration": capo_qbusiness.types.data_accessor_idc_trusted_token_issuer_configuration.deserialize_json(
                data["idcTrustedTokenIssuerConfiguration"]
            )
        }
    else:
        raise DeserializationError(
            "DataAccessorAuthenticationConfiguration: no recognized variant key"
        )
