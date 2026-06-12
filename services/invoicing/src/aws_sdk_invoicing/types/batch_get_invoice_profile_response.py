"""Generated from Smithy shape ``com.amazonaws.invoicing#BatchGetInvoiceProfileResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_invoicing.types.profile_list

class BatchGetInvoiceProfileResponse(TypedDict):
    profiles: NotRequired["aws_sdk_invoicing.types.profile_list.ProfileList"]
    """<p> A list of invoice profiles corresponding to the requested accounts. </p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchGetInvoiceProfileResponse) -> dict:
    out: dict = {}
    if "profiles" in value:
        import aws_sdk_invoicing.types.profile_list
        out["Profiles"] = aws_sdk_invoicing.types.profile_list.serialize_aws_json_1_0(value["profiles"])
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchGetInvoiceProfileResponse:
    out: BatchGetInvoiceProfileResponse = {}  # type: ignore[typeddict-item]
    if "Profiles" in data:
        import aws_sdk_invoicing.types.profile_list
        out["profiles"] = aws_sdk_invoicing.types.profile_list.deserialize_aws_json_1_0(data["Profiles"])
    return out