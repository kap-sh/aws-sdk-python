"""Generated from Smithy shape ``com.amazonaws.invoicing#AccessDeniedException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_invoicing.errors import ServiceError
if TYPE_CHECKING:
    import aws_sdk_invoicing.types.basic_string
    import aws_sdk_invoicing.types.invoice_unit_arn_string

class AccessDeniedException_(TypedDict):
    message: NotRequired["aws_sdk_invoicing.types.basic_string.BasicString"]
    resource_name: NotRequired["aws_sdk_invoicing.types.invoice_unit_arn_string.InvoiceUnitArnString"]
    """<p>You don't have sufficient access to perform this action. </p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccessDeniedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AccessDeniedException_:
    out: AccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "resourceName" in data:
        out["resource_name"] = data["resourceName"]
    return out


class AccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.invoicing#AccessDeniedException``."""
    code: str | None = 'AccessDeniedException'

    def __init__(self, data: AccessDeniedException_):
        super().__init__('client', is_throttling_error=False, is_retryable=False, code='AccessDeniedException')
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "AccessDeniedException":
        return cls(deserialize_aws_json_1_0(data))