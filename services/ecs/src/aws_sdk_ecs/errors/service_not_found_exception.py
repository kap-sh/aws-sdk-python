"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ecs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class ServiceNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p> Message that describes the cause of the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceNotFoundException_:
    out: ServiceNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ServiceNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecs#ServiceNotFoundException``."""

    code: str | None = "ServiceNotFoundException"

    def __init__(self, data: ServiceNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ServiceNotFoundException":
        return cls(deserialize_aws_json_1_1(data))
