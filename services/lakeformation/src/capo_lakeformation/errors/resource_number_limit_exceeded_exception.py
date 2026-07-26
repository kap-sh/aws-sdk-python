"""Generated from Smithy shape ``com.amazonaws.lakeformation#ResourceNumberLimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lakeformation.errors import ServiceError

if TYPE_CHECKING:
    import capo_lakeformation.types.message_string


class ResourceNumberLimitExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_lakeformation.types.message_string.MessageString"]
    """<p>A message describing the problem.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceNumberLimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ResourceNumberLimitExceededException_:
    out: ResourceNumberLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ResourceNumberLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lakeformation#ResourceNumberLimitExceededException``."""

    code: str | None = "ResourceNumberLimitExceededException"

    def __init__(self, data: ResourceNumberLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceNumberLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ResourceNumberLimitExceededException":
        return cls(deserialize_json(data))
