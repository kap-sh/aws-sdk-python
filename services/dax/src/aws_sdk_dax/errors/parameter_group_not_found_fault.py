"""Generated from Smithy shape ``com.amazonaws.dax#ParameterGroupNotFoundFault``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_dax.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_dax.types.exception_message


class ParameterGroupNotFoundFault_(TypedDict):
    message: NotRequired["aws_sdk_dax.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterGroupNotFoundFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ParameterGroupNotFoundFault_:
    out: ParameterGroupNotFoundFault_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ParameterGroupNotFoundFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dax#ParameterGroupNotFoundFault``."""

    code: str | None = "ParameterGroupNotFoundFault"

    def __init__(self, data: ParameterGroupNotFoundFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ParameterGroupNotFoundFault",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ParameterGroupNotFoundFault":
        return cls(deserialize_aws_json_1_1(data))
