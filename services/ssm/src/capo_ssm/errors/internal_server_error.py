"""Generated from Smithy shape ``com.amazonaws.ssm#InternalServerError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.string


class InternalServerError_(TypedDict, closed=True):
    message: NotRequired["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InternalServerError_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InternalServerError_:
    out: InternalServerError_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out


class InternalServerError(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#InternalServerError``."""

    code: str | None = "InternalServerError"

    def __init__(self, data: InternalServerError_, message: str | None = None):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="InternalServerError",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None
    ) -> "InternalServerError":
        return cls(deserialize_aws_json_1_1(data), message)
