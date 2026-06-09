"""Generated from Smithy shape ``com.amazonaws.ecs#ClusterContainsServicesException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class ClusterContainsServicesException_(TypedDict):
    message: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p> Message that describes the cause of the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterContainsServicesException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterContainsServicesException_:
    out: ClusterContainsServicesException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ClusterContainsServicesException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecs#ClusterContainsServicesException``."""

    code: str | None = "ClusterContainsServicesException"

    def __init__(self, data: ClusterContainsServicesException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ClusterContainsServicesException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ClusterContainsServicesException":
        return cls(deserialize_aws_json_1_1(data))
