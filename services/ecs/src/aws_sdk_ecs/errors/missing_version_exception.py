"""Generated from Smithy shape ``com.amazonaws.ecs#MissingVersionException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class MissingVersionException_(TypedDict):
    message: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p> Message that describes the cause of the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MissingVersionException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MissingVersionException_:
    out: MissingVersionException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class MissingVersionException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecs#MissingVersionException``."""

    code: str | None = "MissingVersionException"

    def __init__(self, data: MissingVersionException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MissingVersionException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "MissingVersionException":
        return cls(deserialize_aws_json_1_1(data))
