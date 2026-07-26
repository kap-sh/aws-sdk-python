"""Generated from Smithy shape ``com.amazonaws.workmail#EntityAlreadyRegisteredException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_workmail.errors import ServiceError

if TYPE_CHECKING:
    import capo_workmail.types.string


class EntityAlreadyRegisteredException_(TypedDict, closed=True):
    message: NotRequired["capo_workmail.types.string.String"]


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
