"""Generated from Smithy shape ``com.amazonaws.invoicing#InvoiceProfile``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_invoicing.types.account_id_string
    import aws_sdk_invoicing.types.basic_string_without_space
    import aws_sdk_invoicing.types.receiver_address
    import aws_sdk_invoicing.types.sensitive_basic_string_without_space


class InvoiceProfile(TypedDict):
    account_id: NotRequired["aws_sdk_invoicing.types.account_id_string.AccountIdString"]
    """<p> The account ID the invoice profile is generated for. </p>"""
    receiver_name: NotRequired[
        "aws_sdk_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    ]
    """<p> The name of the person receiving the invoice profile. </p>"""
    receiver_address: NotRequired[
        "aws_sdk_invoicing.types.receiver_address.ReceiverAddress"
    ]
    """<p>The address of the receiver that will be printed on the invoice. </p>"""
    receiver_email: NotRequired[
        "aws_sdk_invoicing.types.sensitive_basic_string_without_space.SensitiveBasicStringWithoutSpace"
    ]
    """<p>The email address for the invoice profile receiver. </p>"""
    issuer: NotRequired[
        "aws_sdk_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    ]
    """<p> This specifies the issuing entity of the invoice. </p>"""
    tax_registration_number: NotRequired[
        "aws_sdk_invoicing.types.sensitive_basic_string_without_space.SensitiveBasicStringWithoutSpace"
    ]
    """<p> Your Tax Registration Number (TRN) information. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvoiceProfile) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "receiver_name" in value:
        out["ReceiverName"] = value["receiver_name"]
    if "receiver_address" in value:
        import aws_sdk_invoicing.types.receiver_address

        out["ReceiverAddress"] = (
            aws_sdk_invoicing.types.receiver_address.serialize_aws_json_1_0(
                value["receiver_address"]
            )
        )
    if "receiver_email" in value:
        out["ReceiverEmail"] = value["receiver_email"]
    if "issuer" in value:
        out["Issuer"] = value["issuer"]
    if "tax_registration_number" in value:
        out["TaxRegistrationNumber"] = value["tax_registration_number"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InvoiceProfile:
    out: InvoiceProfile = {}  # type: ignore[typeddict-item]
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "ReceiverName" in data:
        out["receiver_name"] = data["ReceiverName"]
    if "ReceiverAddress" in data:
        import aws_sdk_invoicing.types.receiver_address

        out["receiver_address"] = (
            aws_sdk_invoicing.types.receiver_address.deserialize_aws_json_1_0(
                data["ReceiverAddress"]
            )
        )
    if "ReceiverEmail" in data:
        out["receiver_email"] = data["ReceiverEmail"]
    if "Issuer" in data:
        out["issuer"] = data["Issuer"]
    if "TaxRegistrationNumber" in data:
        out["tax_registration_number"] = data["TaxRegistrationNumber"]
    return out
