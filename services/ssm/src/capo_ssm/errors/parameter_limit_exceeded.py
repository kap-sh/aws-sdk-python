"""Generated from Smithy shape ``com.amazonaws.ssm#ParameterLimitExceeded``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ssm.errors import ServiceError

if TYPE_CHECKING:
    import capo_ssm.types.string


class ParameterLimitExceeded_(TypedDict, closed=True):
    message: NotRequired["capo_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterLimitExceeded_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ParameterLimitExceeded_:
    out: ParameterLimitExceeded_ = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out


class ParameterLimitExceeded(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#ParameterLimitExceeded``."""

    code: str | None = "ParameterLimitExceeded"

    def __init__(self, data: ParameterLimitExceeded_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ParameterLimitExceeded",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None
    ) -> "ParameterLimitExceeded":
        return cls(deserialize_aws_json_1_1(data), message)
