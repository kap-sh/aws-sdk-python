"""Generated from Smithy shape ``com.amazonaws.codebuild#AccountSuspendedException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codebuild.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.string


class AccountSuspendedException_(TypedDict):
    message: NotRequired["aws_sdk_codebuild.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountSuspendedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AccountSuspendedException_:
    out: AccountSuspendedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class AccountSuspendedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codebuild#AccountSuspendedException``."""

    code: str | None = "AccountSuspendedException"

    def __init__(self, data: AccountSuspendedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccountSuspendedException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "AccountSuspendedException":
        return cls(deserialize_aws_json_1_1(data))
