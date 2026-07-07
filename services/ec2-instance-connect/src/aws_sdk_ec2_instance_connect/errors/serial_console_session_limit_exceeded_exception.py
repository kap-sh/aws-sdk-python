"""Generated from Smithy shape ``com.amazonaws.ec2instanceconnect#SerialConsoleSessionLimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2_instance_connect.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ec2_instance_connect.types.string


class SerialConsoleSessionLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_ec2_instance_connect.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SerialConsoleSessionLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SerialConsoleSessionLimitExceededException_:
    out: SerialConsoleSessionLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class SerialConsoleSessionLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ec2instanceconnect#SerialConsoleSessionLimitExceededException``."""

    code: str | None = "SerialConsoleSessionLimitExceededException"

    def __init__(self, data: SerialConsoleSessionLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SerialConsoleSessionLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict
    ) -> "SerialConsoleSessionLimitExceededException":
        return cls(deserialize_aws_json_1_1(data))
