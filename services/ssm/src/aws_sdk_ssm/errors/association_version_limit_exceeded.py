"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationVersionLimitExceeded``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string


class AssociationVersionLimitExceeded_(TypedDict):
    message: NotRequired["aws_sdk_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationVersionLimitExceeded_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociationVersionLimitExceeded_:
    out: AssociationVersionLimitExceeded_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class AssociationVersionLimitExceeded(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#AssociationVersionLimitExceeded``."""

    code: str | None = "AssociationVersionLimitExceeded"

    def __init__(self, data: AssociationVersionLimitExceeded_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AssociationVersionLimitExceeded",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "AssociationVersionLimitExceeded":
        return cls(deserialize_aws_json_1_1(data))
