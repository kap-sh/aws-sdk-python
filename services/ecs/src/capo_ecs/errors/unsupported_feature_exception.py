"""Generated from Smithy shape ``com.amazonaws.ecs#UnsupportedFeatureException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import ServiceError

if TYPE_CHECKING:
    import capo_ecs.types.string


class UnsupportedFeatureException_(TypedDict, closed=True):
    message: NotRequired["capo_ecs.types.string.String"]
    """<p> Message that describes the cause of the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsupportedFeatureException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnsupportedFeatureException_:
    out: UnsupportedFeatureException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class UnsupportedFeatureException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecs#UnsupportedFeatureException``."""

    code: str | None = "UnsupportedFeatureException"

    def __init__(self, data: UnsupportedFeatureException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedFeatureException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "UnsupportedFeatureException":
        return cls(deserialize_aws_json_1_1(data))
