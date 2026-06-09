"""Generated from Smithy shape ``com.amazonaws.ecs#ClusterNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class ClusterNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p> Message that describes the cause of the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterNotFoundException_:
    out: ClusterNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ClusterNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecs#ClusterNotFoundException``."""

    code: str | None = "ClusterNotFoundException"

    def __init__(self, data: ClusterNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ClusterNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ClusterNotFoundException":
        return cls(deserialize_aws_json_1_1(data))
