"""Generated from Smithy shape ``com.amazonaws.taxsettings#VietnamAdditionalInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_taxsettings.types.date_string
    import aws_sdk_taxsettings.types.electronic_transaction_code_number
    import aws_sdk_taxsettings.types.enterprise_identification_number
    import aws_sdk_taxsettings.types.payment_voucher_number


class VietnamAdditionalInfo(TypedDict, closed=True):
    enterprise_identification_number: NotRequired[
        "aws_sdk_taxsettings.types.enterprise_identification_number.EnterpriseIdentificationNumber"
    ]
    """<p>The enterprise identification number for tax registration. This field must be provided for successful API operation.</p>"""
    electronic_transaction_code_number: NotRequired[
        "aws_sdk_taxsettings.types.electronic_transaction_code_number.ElectronicTransactionCodeNumber"
    ]
    """<p>The electronic transaction code number on the tax return document. This field must be provided for successful API operation.</p>"""
    payment_voucher_number: NotRequired[
        "aws_sdk_taxsettings.types.payment_voucher_number.PaymentVoucherNumber"
    ]
    """<p>The payment voucher number on the tax return payment document. This field must be provided for successful API operation.</p>"""
    payment_voucher_number_date: NotRequired[
        "aws_sdk_taxsettings.types.date_string.DateString"
    ]
    """<p>The date on the tax return payment document. This field must be provided for successful API operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VietnamAdditionalInfo) -> dict:
    out: dict = {}
    if "enterprise_identification_number" in value:
        out["enterpriseIdentificationNumber"] = value[
            "enterprise_identification_number"
        ]
    if "electronic_transaction_code_number" in value:
        out["electronicTransactionCodeNumber"] = value[
            "electronic_transaction_code_number"
        ]
    if "payment_voucher_number" in value:
        out["paymentVoucherNumber"] = value["payment_voucher_number"]
    if "payment_voucher_number_date" in value:
        out["paymentVoucherNumberDate"] = value["payment_voucher_number_date"]
    return out


def deserialize_json(data: dict) -> VietnamAdditionalInfo:
    out: VietnamAdditionalInfo = {}  # type: ignore[typeddict-item]
    if "enterpriseIdentificationNumber" in data:
        out["enterprise_identification_number"] = data["enterpriseIdentificationNumber"]
    if "electronicTransactionCodeNumber" in data:
        out["electronic_transaction_code_number"] = data[
            "electronicTransactionCodeNumber"
        ]
    if "paymentVoucherNumber" in data:
        out["payment_voucher_number"] = data["paymentVoucherNumber"]
    if "paymentVoucherNumberDate" in data:
        out["payment_voucher_number_date"] = data["paymentVoucherNumberDate"]
    return out
