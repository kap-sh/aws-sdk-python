"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ThrottlingException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wellarchitected.errors import ServiceError

if TYPE_CHECKING:
    import capo_wellarchitected.types.exception_message
    import capo_wellarchitected.types.quota_code
    import capo_wellarchitected.types.service_code


class ThrottlingException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_wellarchitected.types.exception_message.ExceptionMessage"
    ]
    quota_code: NotRequired["capo_wellarchitected.types.quota_code.QuotaCode"]
    service_code: NotRequired["capo_wellarchitected.types.service_code.ServiceCode"]


# --- restJson1 ser/de ---
def serialize_json(value: ThrottlingException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "quota_code" in value:
        out["QuotaCode"] = value["quota_code"]
    if "service_code" in value:
        out["ServiceCode"] = value["service_code"]
    return out


def deserialize_json(data: dict) -> ThrottlingException_:
    out: ThrottlingException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "QuotaCode" in data:
        out["quota_code"] = data["QuotaCode"]
    if "ServiceCode" in data:
        out["service_code"] = data["ServiceCode"]
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wellarchitected#ThrottlingException``."""

    code: str | None = "ThrottlingException"

    def __init__(self, data: ThrottlingException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ThrottlingException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ThrottlingException":
        return cls(deserialize_json(data))
