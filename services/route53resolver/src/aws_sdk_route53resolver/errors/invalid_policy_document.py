"""Generated from Smithy shape ``com.amazonaws.route53resolver#InvalidPolicyDocument``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_route53resolver.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.exception_message


class InvalidPolicyDocument_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_route53resolver.types.exception_message.ExceptionMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidPolicyDocument_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidPolicyDocument_:
    out: InvalidPolicyDocument_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidPolicyDocument(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.route53resolver#InvalidPolicyDocument``."""

    code: str | None = "InvalidPolicyDocument"

    def __init__(self, data: InvalidPolicyDocument_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidPolicyDocument",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidPolicyDocument":
        return cls(deserialize_aws_json_1_1(data))
