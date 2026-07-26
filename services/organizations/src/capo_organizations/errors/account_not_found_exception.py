"""Generated from Smithy shape ``com.amazonaws.organizations#AccountNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_organizations.errors import ServiceError

if TYPE_CHECKING:
    import capo_organizations.types.exception_message


class AccountNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_organizations.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AccountNotFoundException_:
    out: AccountNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class AccountNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.organizations#AccountNotFoundException``."""

    code: str | None = "AccountNotFoundException"

    def __init__(self, data: AccountNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AccountNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "AccountNotFoundException":
        return cls(deserialize_aws_json_1_1(data))
