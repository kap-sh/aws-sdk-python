"""Generated from Smithy shape ``com.amazonaws.memorydb#MultiRegionParameterGroupNotFoundFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_memorydb.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.exception_message


class MultiRegionParameterGroupNotFoundFault_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_memorydb.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MultiRegionParameterGroupNotFoundFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MultiRegionParameterGroupNotFoundFault_:
    out: MultiRegionParameterGroupNotFoundFault_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class MultiRegionParameterGroupNotFoundFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.memorydb#MultiRegionParameterGroupNotFoundFault``."""

    code: str | None = "MultiRegionParameterGroupNotFoundFault"

    def __init__(self, data: MultiRegionParameterGroupNotFoundFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MultiRegionParameterGroupNotFoundFault",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "MultiRegionParameterGroupNotFoundFault":
        return cls(deserialize_aws_json_1_1(data))
