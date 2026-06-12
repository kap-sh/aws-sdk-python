"""Generated from Smithy shape ``com.amazonaws.swf#UnknownResourceFault``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_swf.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_swf.types.error_message


class UnknownResourceFault_(TypedDict):
    message: NotRequired["aws_sdk_swf.types.error_message.ErrorMessage"]
    """<p>A description that may help with diagnosing the cause of the fault.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UnknownResourceFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UnknownResourceFault_:
    out: UnknownResourceFault_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class UnknownResourceFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.swf#UnknownResourceFault``."""

    code: str | None = "UnknownResourceFault"

    def __init__(self, data: UnknownResourceFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnknownResourceFault",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "UnknownResourceFault":
        return cls(deserialize_aws_json_1_0(data))
