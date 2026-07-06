"""Generated from Smithy shape ``com.amazonaws.ec2instanceconnect#SerialConsoleAccessDisabledException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2_instance_connect.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ec2_instance_connect.types.string


class SerialConsoleAccessDisabledException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_ec2_instance_connect.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SerialConsoleAccessDisabledException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SerialConsoleAccessDisabledException_:
    out: SerialConsoleAccessDisabledException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class SerialConsoleAccessDisabledException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ec2instanceconnect#SerialConsoleAccessDisabledException``."""

    code: str | None = "SerialConsoleAccessDisabledException"

    def __init__(self, data: SerialConsoleAccessDisabledException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SerialConsoleAccessDisabledException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "SerialConsoleAccessDisabledException":
        return cls(deserialize_aws_json_1_1(data))
