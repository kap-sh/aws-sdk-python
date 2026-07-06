"""Generated from Smithy shape ``com.amazonaws.taxsettings#TaxExemption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_taxsettings.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_taxsettings.types.authority
    import aws_sdk_taxsettings.types.entity_exemption_account_status
    import aws_sdk_taxsettings.types.tax_exemption_type


class TaxExemption(TypedDict, closed=True):
    authority: "aws_sdk_taxsettings.types.authority.Authority"
    """<p>The address domain associate with tax exemption. </p>"""
    tax_exemption_type: "aws_sdk_taxsettings.types.tax_exemption_type.TaxExemptionType"
    """<p>The tax exemption type. </p>"""
    effective_date: NotRequired["datetime.datetime"]
    """<p>The tax exemption effective date. </p>"""
    expiration_date: NotRequired["datetime.datetime"]
    """<p>The tax exemption expiration date. </p>"""
    system_effective_date: NotRequired["datetime.datetime"]
    """<p>The tax exemption recording time in the <code>TaxSettings</code> system. </p>"""
    status: NotRequired[
        "aws_sdk_taxsettings.types.entity_exemption_account_status.EntityExemptionAccountStatus"
    ]
    """<p>The tax exemption status. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TaxExemption) -> dict:
    out: dict = {}
    import aws_sdk_taxsettings.types.authority

    out["authority"] = aws_sdk_taxsettings.types.authority.serialize_json(
        value["authority"]
    )
    import aws_sdk_taxsettings.types.tax_exemption_type

    out["taxExemptionType"] = (
        aws_sdk_taxsettings.types.tax_exemption_type.serialize_json(
            value["tax_exemption_type"]
        )
    )
    if "effective_date" in value:
        import aws_sdk_taxsettings.types._prelude.timestamp

        out["effectiveDate"] = (
            aws_sdk_taxsettings.types._prelude.timestamp.serialize_json(
                value["effective_date"]
            )
        )
    if "expiration_date" in value:
        import aws_sdk_taxsettings.types._prelude.timestamp

        out["expirationDate"] = (
            aws_sdk_taxsettings.types._prelude.timestamp.serialize_json(
                value["expiration_date"]
            )
        )
    if "system_effective_date" in value:
        import aws_sdk_taxsettings.types._prelude.timestamp

        out["systemEffectiveDate"] = (
            aws_sdk_taxsettings.types._prelude.timestamp.serialize_json(
                value["system_effective_date"]
            )
        )
    if "status" in value:
        import aws_sdk_taxsettings.types.entity_exemption_account_status

        out["status"] = (
            aws_sdk_taxsettings.types.entity_exemption_account_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> TaxExemption:
    out: TaxExemption = {}  # type: ignore[typeddict-item]
    if "authority" in data:
        import aws_sdk_taxsettings.types.authority

        out["authority"] = aws_sdk_taxsettings.types.authority.deserialize_json(
            data["authority"]
        )
    else:
        raise DeserializationError("TaxExemption.authority required")
    if "taxExemptionType" in data:
        import aws_sdk_taxsettings.types.tax_exemption_type

        out["tax_exemption_type"] = (
            aws_sdk_taxsettings.types.tax_exemption_type.deserialize_json(
                data["taxExemptionType"]
            )
        )
    else:
        raise DeserializationError("TaxExemption.tax_exemption_type required")
    if "effectiveDate" in data:
        import aws_sdk_taxsettings.types._prelude.timestamp

        out["effective_date"] = (
            aws_sdk_taxsettings.types._prelude.timestamp.deserialize_json(
                data["effectiveDate"]
            )
        )
    if "expirationDate" in data:
        import aws_sdk_taxsettings.types._prelude.timestamp

        out["expiration_date"] = (
            aws_sdk_taxsettings.types._prelude.timestamp.deserialize_json(
                data["expirationDate"]
            )
        )
    if "systemEffectiveDate" in data:
        import aws_sdk_taxsettings.types._prelude.timestamp

        out["system_effective_date"] = (
            aws_sdk_taxsettings.types._prelude.timestamp.deserialize_json(
                data["systemEffectiveDate"]
            )
        )
    if "status" in data:
        import aws_sdk_taxsettings.types.entity_exemption_account_status

        out["status"] = (
            aws_sdk_taxsettings.types.entity_exemption_account_status.deserialize_json(
                data["status"]
            )
        )
    return out
