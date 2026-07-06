"""Generated from Smithy shape ``com.amazonaws.taxsettings#PutTaxExemptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_taxsettings.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.account_ids
    import aws_sdk_taxsettings.types.authority
    import aws_sdk_taxsettings.types.exemption_certificate
    import aws_sdk_taxsettings.types.generic_string


class PutTaxExemptionRequest(TypedDict, closed=True):
    account_ids: "aws_sdk_taxsettings.types.account_ids.AccountIds"
    """<p> The list of unique account identifiers. </p>"""
    authority: "aws_sdk_taxsettings.types.authority.Authority"
    exemption_type: "aws_sdk_taxsettings.types.generic_string.GenericString"
    """<p>The exemption type. Use the supported tax exemption type description. </p>"""
    exemption_certificate: (
        "aws_sdk_taxsettings.types.exemption_certificate.ExemptionCertificate"
    )


# --- restJson1 ser/de ---
def serialize_json(value: PutTaxExemptionRequest) -> dict:
    out: dict = {}
    import aws_sdk_taxsettings.types.account_ids

    out["accountIds"] = aws_sdk_taxsettings.types.account_ids.serialize_json(
        value["account_ids"]
    )
    import aws_sdk_taxsettings.types.authority

    out["authority"] = aws_sdk_taxsettings.types.authority.serialize_json(
        value["authority"]
    )
    out["exemptionType"] = value["exemption_type"]
    import aws_sdk_taxsettings.types.exemption_certificate

    out["exemptionCertificate"] = (
        aws_sdk_taxsettings.types.exemption_certificate.serialize_json(
            value["exemption_certificate"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutTaxExemptionRequest:
    out: PutTaxExemptionRequest = {}  # type: ignore[typeddict-item]
    if "accountIds" in data:
        import aws_sdk_taxsettings.types.account_ids

        out["account_ids"] = aws_sdk_taxsettings.types.account_ids.deserialize_json(
            data["accountIds"]
        )
    else:
        raise DeserializationError("PutTaxExemptionRequest.account_ids required")
    if "authority" in data:
        import aws_sdk_taxsettings.types.authority

        out["authority"] = aws_sdk_taxsettings.types.authority.deserialize_json(
            data["authority"]
        )
    else:
        raise DeserializationError("PutTaxExemptionRequest.authority required")
    if "exemptionType" in data:
        out["exemption_type"] = data["exemptionType"]
    else:
        raise DeserializationError("PutTaxExemptionRequest.exemption_type required")
    if "exemptionCertificate" in data:
        import aws_sdk_taxsettings.types.exemption_certificate

        out["exemption_certificate"] = (
            aws_sdk_taxsettings.types.exemption_certificate.deserialize_json(
                data["exemptionCertificate"]
            )
        )
    else:
        raise DeserializationError(
            "PutTaxExemptionRequest.exemption_certificate required"
        )
    return out
