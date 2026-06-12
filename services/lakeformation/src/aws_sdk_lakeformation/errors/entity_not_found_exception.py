"""Generated from Smithy shape ``com.amazonaws.lakeformation#EntityNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lakeformation.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.message_string


class EntityNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_lakeformation.types.message_string.MessageString"]
    """<p>A message describing the problem.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EntityNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> EntityNotFoundException_:
    out: EntityNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class EntityNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lakeformation#EntityNotFoundException``."""

    code: str | None = "EntityNotFoundException"

    def __init__(self, data: EntityNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="EntityNotFoundException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "EntityNotFoundException":
        return cls(deserialize_json(data))
