"""Generated from Smithy shape ``com.amazonaws.taxsettings#MalaysiaAdditionalInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.business_registration_number
    import aws_sdk_taxsettings.types.malaysia_service_tax_codes_list
    import aws_sdk_taxsettings.types.tax_information_number


class MalaysiaAdditionalInfo(TypedDict):
    service_tax_codes: "aws_sdk_taxsettings.types.malaysia_service_tax_codes_list.MalaysiaServiceTaxCodesList"
    """<p>List of service tax codes for your TRN in Malaysia.</p>"""
    tax_information_number: NotRequired[
        "aws_sdk_taxsettings.types.tax_information_number.TaxInformationNumber"
    ]
    """<p>The tax information number in Malaysia. </p> <p>For individual, you can specify the <code>taxInformationNumber</code> in <code>MalaysiaAdditionalInfo</code> with NRIC type, and a valid MyKad or NRIC number. For business resellers, you must specify a <code>businessRegistrationNumber</code> and <code>taxInformationNumber</code> in <code>MalaysiaAdditionalInfo</code> with a sales and service tax (SST) type and a valid SST number. </p> <p>For business resellers with service codes, you must specify <code>businessRegistrationNumber</code>, <code>taxInformationNumber</code>, and distinct <code>serviceTaxCodes</code> in <code>MalaysiaAdditionalInfo</code> with a SST type and valid sales and service tax (SST) number. By using this API operation, Amazon Web Services registers your self-declaration that you’re an authorized business reseller registered with the Royal Malaysia Customs Department (RMCD), and have a valid SST number.</p>"""
    business_registration_number: NotRequired[
        "aws_sdk_taxsettings.types.business_registration_number.BusinessRegistrationNumber"
    ]
    """<p>The tax registration number (TRN) in Malaysia. </p> <p>For individual, you can specify the <code>taxInformationNumber</code> in <code>MalaysiaAdditionalInfo</code> with NRIC type, and a valid MyKad or NRIC number. For business, you must specify a <code>businessRegistrationNumber</code> in <code>MalaysiaAdditionalInfo</code> with a TIN type and tax identification number. For business resellers, you must specify a <code>businessRegistrationNumber</code> and <code>taxInformationNumber</code> in <code>MalaysiaAdditionalInfo</code> with a sales and service tax (SST) type and a valid SST number. </p> <p>For business resellers with service codes, you must specify <code>businessRegistrationNumber</code>, <code>taxInformationNumber</code>, and distinct <code>serviceTaxCodes</code> in <code>MalaysiaAdditionalInfo</code> with a SST type and valid sales and service tax (SST) number. By using this API operation, Amazon Web Services registers your self-declaration that you’re an authorized business reseller registered with the Royal Malaysia Customs Department (RMCD), and have a valid SST number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MalaysiaAdditionalInfo) -> dict:
    out: dict = {}
    import aws_sdk_taxsettings.types.malaysia_service_tax_codes_list

    out["serviceTaxCodes"] = (
        aws_sdk_taxsettings.types.malaysia_service_tax_codes_list.serialize_json(
            value.get("service_tax_codes", [])
        )
    )
    if "tax_information_number" in value:
        out["taxInformationNumber"] = value["tax_information_number"]
    if "business_registration_number" in value:
        out["businessRegistrationNumber"] = value["business_registration_number"]
    return out


def deserialize_json(data: dict) -> MalaysiaAdditionalInfo:
    out: MalaysiaAdditionalInfo = {}  # type: ignore[typeddict-item]
    if "serviceTaxCodes" in data:
        import aws_sdk_taxsettings.types.malaysia_service_tax_codes_list

        out["service_tax_codes"] = (
            aws_sdk_taxsettings.types.malaysia_service_tax_codes_list.deserialize_json(
                data["serviceTaxCodes"]
            )
        )
    else:
        out["service_tax_codes"] = []
    if "taxInformationNumber" in data:
        out["tax_information_number"] = data["taxInformationNumber"]
    if "businessRegistrationNumber" in data:
        out["business_registration_number"] = data["businessRegistrationNumber"]
    return out
