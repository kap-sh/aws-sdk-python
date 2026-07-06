"""Generated from Smithy shape ``com.amazonaws.ssm#InvalidDeleteInventoryParametersException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.string


class InvalidDeleteInventoryParametersException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_ssm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidDeleteInventoryParametersException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidDeleteInventoryParametersException_:
    out: InvalidDeleteInventoryParametersException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class InvalidDeleteInventoryParametersException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ssm#InvalidDeleteInventoryParametersException``."""

    code: str | None = "InvalidDeleteInventoryParametersException"

    def __init__(self, data: InvalidDeleteInventoryParametersException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidDeleteInventoryParametersException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict
    ) -> "InvalidDeleteInventoryParametersException":
        return cls(deserialize_aws_json_1_1(data))
