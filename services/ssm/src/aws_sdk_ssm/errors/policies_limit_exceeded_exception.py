"""Generated from Smithy shape ``com.amazonaws.ssm#PoliciesLimitExceededException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string


class PoliciesLimitExceededException_(TypedDict):
    message: NotRequired["aws_sdk_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PoliciesLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PoliciesLimitExceededException_:
    out: PoliciesLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class PoliciesLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#PoliciesLimitExceededException``."""

    code: str | None = "PoliciesLimitExceededException"

    def __init__(self, data: PoliciesLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PoliciesLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "PoliciesLimitExceededException":
        return cls(deserialize_aws_json_1_1(data))
