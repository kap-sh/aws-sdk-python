"""Generated from Smithy shape ``com.amazonaws.taxsettings#RomaniaAdditionalInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_taxsettings.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.tax_registration_number_type


class RomaniaAdditionalInfo(TypedDict, closed=True):
    tax_registration_number_type: "aws_sdk_taxsettings.types.tax_registration_number_type.TaxRegistrationNumberType"
    """<p> The tax registration number type. The value can be <code>TaxRegistrationNumber</code> or <code>LocalRegistrationNumber</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RomaniaAdditionalInfo) -> dict:
    out: dict = {}
    import aws_sdk_taxsettings.types.tax_registration_number_type

    out["taxRegistrationNumberType"] = (
        aws_sdk_taxsettings.types.tax_registration_number_type.serialize_json(
            value["tax_registration_number_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> RomaniaAdditionalInfo:
    out: RomaniaAdditionalInfo = {}  # type: ignore[typeddict-item]
    if "taxRegistrationNumberType" in data:
        import aws_sdk_taxsettings.types.tax_registration_number_type

        out["tax_registration_number_type"] = (
            aws_sdk_taxsettings.types.tax_registration_number_type.deserialize_json(
                data["taxRegistrationNumberType"]
            )
        )
    else:
        raise DeserializationError(
            "RomaniaAdditionalInfo.tax_registration_number_type required"
        )
    return out
