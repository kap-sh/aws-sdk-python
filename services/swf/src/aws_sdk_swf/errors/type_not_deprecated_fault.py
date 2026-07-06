"""Generated from Smithy shape ``com.amazonaws.swf#TypeNotDeprecatedFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_swf.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_swf.types.error_message


class TypeNotDeprecatedFault_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_swf.types.error_message.ErrorMessage"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TypeNotDeprecatedFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TypeNotDeprecatedFault_:
    out: TypeNotDeprecatedFault_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class TypeNotDeprecatedFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.swf#TypeNotDeprecatedFault``."""

    code: str | None = "TypeNotDeprecatedFault"

    def __init__(self, data: TypeNotDeprecatedFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TypeNotDeprecatedFault",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "TypeNotDeprecatedFault":
        return cls(deserialize_aws_json_1_0(data))
