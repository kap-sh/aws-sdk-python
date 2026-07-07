"""Generated from Smithy shape ``com.amazonaws.cloudtrail#TrailNotProvidedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudtrail.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.error_message


class TrailNotProvidedException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_cloudtrail.types.error_message.ErrorMessage"]
    """<p>Brief description of the exception returned by the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrailNotProvidedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TrailNotProvidedException_:
    out: TrailNotProvidedException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class TrailNotProvidedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudtrail#TrailNotProvidedException``."""

    code: str | None = "TrailNotProvidedException"

    def __init__(self, data: TrailNotProvidedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TrailNotProvidedException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "TrailNotProvidedException":
        return cls(deserialize_aws_json_1_1(data))
