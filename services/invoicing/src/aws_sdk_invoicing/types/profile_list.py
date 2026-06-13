"""Generated from Smithy shape ``com.amazonaws.invoicing#ProfileList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_invoicing.types.invoice_profile

ProfileList: TypeAlias = list["aws_sdk_invoicing.types.invoice_profile.InvoiceProfile"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProfileList) -> list:
    import aws_sdk_invoicing.types.invoice_profile

    out: list = []
    for item in value:
        out.append(aws_sdk_invoicing.types.invoice_profile.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ProfileList:
    import aws_sdk_invoicing.types.invoice_profile

    out: ProfileList = []
    for item in data:
        out.append(
            aws_sdk_invoicing.types.invoice_profile.deserialize_aws_json_1_0(item)
        )
    return out
