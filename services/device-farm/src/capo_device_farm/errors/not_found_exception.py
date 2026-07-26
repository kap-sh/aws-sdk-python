"""Generated from Smithy shape ``com.amazonaws.devicefarm#NotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_device_farm.errors import ServiceError

if TYPE_CHECKING:
    import capo_device_farm.types.message


class NotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_device_farm.types.message.Message"]
    """<p>Any additional information about the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NotFoundException_:
    out: NotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class NotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.devicefarm#NotFoundException``."""

    code: str | None = "NotFoundException"

    def __init__(self, data: NotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "NotFoundException":
        return cls(deserialize_aws_json_1_1(data))
