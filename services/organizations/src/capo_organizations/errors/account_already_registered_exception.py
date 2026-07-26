"""Generated from Smithy shape ``com.amazonaws.organizations#AccountAlreadyRegisteredException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_organizations.errors import ServiceError

if TYPE_CHECKING:
    import capo_organizations.types.exception_message


class AccountAlreadyRegisteredException_(TypedDict, closed=True):
    message: NotRequired["capo_organizations.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountAlreadyRegisteredException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AccountAlreadyRegisteredException_:
    out: AccountAlreadyRegisteredException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class AccountAlreadyRegisteredException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.organizations#AccountAlreadyRegisteredException``."""

    code: str | None = "AccountAlreadyRegisteredException"

    def __init__(self, data: AccountAlreadyRegisteredException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccountAlreadyRegisteredException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "AccountAlreadyRegisteredException":
        return cls(deserialize_aws_json_1_1(data))
