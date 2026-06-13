"""Generated from Smithy shape ``com.amazonaws.quicksight#LimitExceededException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.exception_resource_type
    import aws_sdk_quicksight.types.string


class LimitExceededException_(TypedDict):
    message: NotRequired["aws_sdk_quicksight.types.string.String"]
    resource_type: NotRequired[
        "aws_sdk_quicksight.types.exception_resource_type.ExceptionResourceType"
    ]
    """<p>Limit exceeded.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LimitExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "resource_type" in value:
        import aws_sdk_quicksight.types.exception_resource_type

        out["ResourceType"] = (
            aws_sdk_quicksight.types.exception_resource_type.serialize_json(
                value["resource_type"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> LimitExceededException_:
    out: LimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "ResourceType" in data:
        import aws_sdk_quicksight.types.exception_resource_type

        out["resource_type"] = (
            aws_sdk_quicksight.types.exception_resource_type.deserialize_json(
                data["ResourceType"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out


class LimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.quicksight#LimitExceededException``."""

    code: str | None = "LimitExceededException"

    def __init__(self, data: LimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="LimitExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "LimitExceededException":
        return cls(deserialize_json(data))
