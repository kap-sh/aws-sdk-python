"""Generated from Smithy shape ``com.amazonaws.ssm#InvalidKeyId``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.string


class InvalidKeyId_(TypedDict, closed=True):
    message: NotRequired["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidKeyId_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidKeyId_:
    out: InvalidKeyId_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidKeyId(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#InvalidKeyId``."""

    code: str | None = "InvalidKeyId"

    def __init__(self, data: InvalidKeyId_):
        super().__init__(
            "client", is_throttling_error=False, is_retryable=False, code="InvalidKeyId"
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidKeyId":
        return cls(deserialize_aws_json_1_1(data))
