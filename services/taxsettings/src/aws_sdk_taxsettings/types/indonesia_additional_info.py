"""Generated from Smithy shape ``com.amazonaws.taxsettings#IndonesiaAdditionalInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.decision_number
    import aws_sdk_taxsettings.types.indonesia_tax_registration_number_type
    import aws_sdk_taxsettings.types.ppn_exception_designation_code


class IndonesiaAdditionalInfo(TypedDict, closed=True):
    tax_registration_number_type: NotRequired[
        "aws_sdk_taxsettings.types.indonesia_tax_registration_number_type.IndonesiaTaxRegistrationNumberType"
    ]
    """<p>The tax registration number type.</p>"""
    ppn_exception_designation_code: NotRequired[
        "aws_sdk_taxsettings.types.ppn_exception_designation_code.PpnExceptionDesignationCode"
    ]
    """<p>Exception code if you are designated by Directorate General of Taxation (DGT) as a VAT collector, non-collected VAT, or VAT-exempt customer.</p>"""
    decision_number: NotRequired[
        "aws_sdk_taxsettings.types.decision_number.DecisionNumber"
    ]
    """<p>VAT-exempt customers have a Directorate General of Taxation (DGT) exemption letter or certificate (Surat Keterangan Bebas) decision number. Non-collected VAT have a DGT letter or certificate (Surat Keterangan Tidak Dipungut).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IndonesiaAdditionalInfo) -> dict:
    out: dict = {}
    if "tax_registration_number_type" in value:
        import aws_sdk_taxsettings.types.indonesia_tax_registration_number_type

        out["taxRegistrationNumberType"] = (
            aws_sdk_taxsettings.types.indonesia_tax_registration_number_type.serialize_json(
                value["tax_registration_number_type"]
            )
        )
    if "ppn_exception_designation_code" in value:
        out["ppnExceptionDesignationCode"] = value["ppn_exception_designation_code"]
    if "decision_number" in value:
        out["decisionNumber"] = value["decision_number"]
    return out


def deserialize_json(data: dict) -> IndonesiaAdditionalInfo:
    out: IndonesiaAdditionalInfo = {}  # type: ignore[typeddict-item]
    if "taxRegistrationNumberType" in data:
        import aws_sdk_taxsettings.types.indonesia_tax_registration_number_type

        out["tax_registration_number_type"] = (
            aws_sdk_taxsettings.types.indonesia_tax_registration_number_type.deserialize_json(
                data["taxRegistrationNumberType"]
            )
        )
    if "ppnExceptionDesignationCode" in data:
        out["ppn_exception_designation_code"] = data["ppnExceptionDesignationCode"]
    if "decisionNumber" in data:
        out["decision_number"] = data["decisionNumber"]
    return out
