"""Generated from Smithy shape ``com.amazonaws.dax#NodeQuotaForCustomerExceededFault``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_dax.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dax.types.exception_message


class NodeQuotaForCustomerExceededFault_(TypedDict):
    message: NotRequired["aws_sdk_dax.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NodeQuotaForCustomerExceededFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NodeQuotaForCustomerExceededFault_:
    out: NodeQuotaForCustomerExceededFault_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class NodeQuotaForCustomerExceededFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dax#NodeQuotaForCustomerExceededFault``."""

    code: str | None = "NodeQuotaForCustomerExceededFault"

    def __init__(self, data: NodeQuotaForCustomerExceededFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NodeQuotaForCustomerExceededFault",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "NodeQuotaForCustomerExceededFault":
        return cls(deserialize_aws_json_1_1(data))
