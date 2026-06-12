"""Generated from Smithy shape ``com.amazonaws.ecr#SigningConfigurationNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecr.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.exception_message


class SigningConfigurationNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_ecr.types.exception_message.ExceptionMessage"]
    """<p>The error message associated with the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SigningConfigurationNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SigningConfigurationNotFoundException_:
    out: SigningConfigurationNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class SigningConfigurationNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecr#SigningConfigurationNotFoundException``."""

    code: str | None = "SigningConfigurationNotFoundException"

    def __init__(self, data: SigningConfigurationNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SigningConfigurationNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "SigningConfigurationNotFoundException":
        return cls(deserialize_aws_json_1_1(data))
