"""Generated from Smithy shape ``com.amazonaws.costexplorer#UnresolvableUsageUnitException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cost_explorer.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.error_message


class UnresolvableUsageUnitException_(TypedDict):
    message: NotRequired["aws_sdk_cost_explorer.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnresolvableUsageUnitException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnresolvableUsageUnitException_:
    out: UnresolvableUsageUnitException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class UnresolvableUsageUnitException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.costexplorer#UnresolvableUsageUnitException``."""

    code: str | None = "UnresolvableUsageUnitException"

    def __init__(self, data: UnresolvableUsageUnitException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnresolvableUsageUnitException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "UnresolvableUsageUnitException":
        return cls(deserialize_aws_json_1_1(data))
