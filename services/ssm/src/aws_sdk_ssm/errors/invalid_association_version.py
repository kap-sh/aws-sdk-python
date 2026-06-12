"""Generated from Smithy shape ``com.amazonaws.ssm#InvalidAssociationVersion``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string


class InvalidAssociationVersion_(TypedDict):
    message: NotRequired["aws_sdk_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidAssociationVersion_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidAssociationVersion_:
    out: InvalidAssociationVersion_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidAssociationVersion(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#InvalidAssociationVersion``."""

    code: str | None = "InvalidAssociationVersion"

    def __init__(self, data: InvalidAssociationVersion_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidAssociationVersion",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidAssociationVersion":
        return cls(deserialize_aws_json_1_1(data))
