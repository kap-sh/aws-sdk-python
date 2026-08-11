"""Generated from Smithy shape ``com.amazonaws.ecr#ExclusionNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecr.errors import ServiceError

if TYPE_CHECKING:
    import capo_ecr.types.exception_message


class ExclusionNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_ecr.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExclusionNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExclusionNotFoundException_:
    out: ExclusionNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ExclusionNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecr#ExclusionNotFoundException``."""

    code: str | None = "ExclusionNotFoundException"

    def __init__(self, data: ExclusionNotFoundException_, message: str | None = None):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ExclusionNotFoundException",
            message=message if message is not None else data.get("message"),
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None
    ) -> "ExclusionNotFoundException":
        return cls(deserialize_aws_json_1_1(data), message)
