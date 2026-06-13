"""Generated from Smithy shape ``com.amazonaws.entityresolution#ExceedsLimitException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_entityresolution.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.error_message


class ExceedsLimitException_(TypedDict):
    message: NotRequired["aws_sdk_entityresolution.types.error_message.ErrorMessage"]
    quota_name: NotRequired["str"]
    """<p>The name of the quota that has been breached.</p>"""
    quota_value: NotRequired["int"]
    """<p>The current quota value for the customers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExceedsLimitException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "quota_name" in value:
        out["quotaName"] = value["quota_name"]
    if "quota_value" in value:
        out["quotaValue"] = value["quota_value"]
    return out


def deserialize_json(data: dict) -> ExceedsLimitException_:
    out: ExceedsLimitException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "quotaName" in data:
        out["quota_name"] = data["quotaName"]
    if "quotaValue" in data:
        out["quota_value"] = data["quotaValue"]
    return out


class ExceedsLimitException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.entityresolution#ExceedsLimitException``."""

    code: str | None = "ExceedsLimitException"

    def __init__(self, data: ExceedsLimitException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ExceedsLimitException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ExceedsLimitException":
        return cls(deserialize_json(data))
