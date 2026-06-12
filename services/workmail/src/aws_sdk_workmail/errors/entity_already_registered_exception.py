"""Generated from Smithy shape ``com.amazonaws.workmail#EntityAlreadyRegisteredException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workmail.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.string


class EntityAlreadyRegisteredException_(TypedDict):
    message: NotRequired["aws_sdk_workmail.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityAlreadyRegisteredException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityAlreadyRegisteredException_:
    out: EntityAlreadyRegisteredException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class EntityAlreadyRegisteredException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.workmail#EntityAlreadyRegisteredException``."""

    code: str | None = "EntityAlreadyRegisteredException"

    def __init__(self, data: EntityAlreadyRegisteredException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="EntityAlreadyRegisteredException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "EntityAlreadyRegisteredException":
        return cls(deserialize_aws_json_1_1(data))
