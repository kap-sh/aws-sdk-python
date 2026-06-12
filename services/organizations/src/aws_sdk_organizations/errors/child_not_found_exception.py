"""Generated from Smithy shape ``com.amazonaws.organizations#ChildNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_organizations.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_organizations.types.exception_message


class ChildNotFoundException_(TypedDict):
    message: NotRequired[
        "aws_sdk_organizations.types.exception_message.ExceptionMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChildNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ChildNotFoundException_:
    out: ChildNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ChildNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.organizations#ChildNotFoundException``."""

    code: str | None = "ChildNotFoundException"

    def __init__(self, data: ChildNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ChildNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ChildNotFoundException":
        return cls(deserialize_aws_json_1_1(data))
