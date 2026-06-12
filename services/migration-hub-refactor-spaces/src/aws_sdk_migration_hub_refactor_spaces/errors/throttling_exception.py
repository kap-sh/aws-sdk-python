"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#ThrottlingException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_migration_hub_refactor_spaces.errors import (
    DeserializationError,
    ServiceError,
)

if TYPE_CHECKING:
    import aws_sdk_migration_hub_refactor_spaces.types.retry_after_seconds
    import aws_sdk_migration_hub_refactor_spaces.types.string


class ThrottlingException_(TypedDict):
    message: "aws_sdk_migration_hub_refactor_spaces.types.string.String"
    quota_code: NotRequired["aws_sdk_migration_hub_refactor_spaces.types.string.String"]
    """<p>Service quota requirement to identify originating quota. Reached throttling quota exception. </p>"""
    service_code: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.string.String"
    ]
    """<p>Service quota requirement to identify originating service. Reached throttling quota exception service code. </p>"""
    retry_after_seconds: "aws_sdk_migration_hub_refactor_spaces.types.retry_after_seconds.RetryAfterSeconds"
    """<p>The number of seconds to wait before retrying. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThrottlingException_) -> dict:
    out: dict = {}
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
    else:
        raise DeserializationError("ThrottlingException_.message required")
    if "QuotaCode" in data:
        out["quota_code"] = data["QuotaCode"]
    if "ServiceCode" in data:
        out["service_code"] = data["ServiceCode"]
    return out


class ThrottlingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.migrationhubrefactorspaces#ThrottlingException``."""

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
