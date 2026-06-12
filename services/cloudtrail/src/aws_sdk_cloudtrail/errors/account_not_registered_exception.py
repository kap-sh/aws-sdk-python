"""Generated from Smithy shape ``com.amazonaws.cloudtrail#AccountNotRegisteredException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudtrail.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.error_message


class AccountNotRegisteredException_(TypedDict):
    message: NotRequired["aws_sdk_cloudtrail.types.error_message.ErrorMessage"]
    """<p>Brief description of the exception returned by the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountNotRegisteredException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AccountNotRegisteredException_:
    out: AccountNotRegisteredException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class AccountNotRegisteredException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudtrail#AccountNotRegisteredException``."""

    code: str | None = "AccountNotRegisteredException"

    def __init__(self, data: AccountNotRegisteredException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccountNotRegisteredException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "AccountNotRegisteredException":
        return cls(deserialize_aws_json_1_1(data))
