"""Generated from Smithy shape ``com.amazonaws.invoicing#BatchGetInvoiceProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_invoicing.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_invoicing.types.account_id_list

class BatchGetInvoiceProfileRequest(TypedDict):
    account_ids: "aws_sdk_invoicing.types.account_id_list.AccountIdList"
    """<p>Retrieves the corresponding invoice profile data for these account IDs. </p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetInvoiceProfileRequest) -> dict:
    out: dict = {}
    import aws_sdk_invoicing.types.account_id_list
    out["AccountIds"] = aws_sdk_invoicing.types.account_id_list.serialize_aws_json_1_0(value["account_ids"])
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchGetInvoiceProfileRequest:
    out: BatchGetInvoiceProfileRequest = {}  # type: ignore[typeddict-item]
    if "AccountIds" in data:
        import aws_sdk_invoicing.types.account_id_list
        out["account_ids"] = aws_sdk_invoicing.types.account_id_list.deserialize_aws_json_1_0(data["AccountIds"])
    else:
        raise DeserializationError("BatchGetInvoiceProfileRequest.account_ids required")
    return out