"""Generated from Smithy shape ``com.amazonaws.dax#SubnetQuotaExceededFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_dax.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dax.types.exception_message


class SubnetQuotaExceededFault_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_dax.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubnetQuotaExceededFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SubnetQuotaExceededFault_:
    out: SubnetQuotaExceededFault_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class SubnetQuotaExceededFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dax#SubnetQuotaExceededFault``."""

    code: str | None = "SubnetQuotaExceededFault"

    def __init__(self, data: SubnetQuotaExceededFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SubnetQuotaExceededFault",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "SubnetQuotaExceededFault":
        return cls(deserialize_aws_json_1_1(data))
