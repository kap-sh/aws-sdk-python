"""Generated from Smithy shape ``com.amazonaws.ssm#InvalidAssociation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string


class InvalidAssociation_(TypedDict):
    message: NotRequired["aws_sdk_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidAssociation_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidAssociation_:
    out: InvalidAssociation_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidAssociation(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#InvalidAssociation``."""

    code: str | None = "InvalidAssociation"

    def __init__(self, data: InvalidAssociation_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidAssociation",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidAssociation":
        return cls(deserialize_aws_json_1_1(data))
