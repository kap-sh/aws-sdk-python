"""Generated from Smithy shape ``com.amazonaws.qbusiness#DataAccessorIdcTrustedTokenIssuerConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.idc_trusted_token_issuer_arn


class DataAccessorIdcTrustedTokenIssuerConfiguration(TypedDict, closed=True):
    idc_trusted_token_issuer_arn: (
        "aws_sdk_qbusiness.types.idc_trusted_token_issuer_arn.IdcTrustedTokenIssuerArn"
    )
    """<p>The Amazon Resource Name (ARN) of the IAM Identity Center Trusted Token Issuer that will be used for authentication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataAccessorIdcTrustedTokenIssuerConfiguration) -> dict:
    out: dict = {}
    out["idcTrustedTokenIssuerArn"] = value["idc_trusted_token_issuer_arn"]
    return out


def deserialize_json(data: dict) -> DataAccessorIdcTrustedTokenIssuerConfiguration:
    out: DataAccessorIdcTrustedTokenIssuerConfiguration = {}  # type: ignore[typeddict-item]
    if "idcTrustedTokenIssuerArn" in data:
        out["idc_trusted_token_issuer_arn"] = data["idcTrustedTokenIssuerArn"]
    else:
        raise DeserializationError(
            "DataAccessorIdcTrustedTokenIssuerConfiguration.idc_trusted_token_issuer_arn required"
        )
    return out
