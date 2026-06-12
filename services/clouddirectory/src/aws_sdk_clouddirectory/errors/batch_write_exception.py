"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchWriteException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_clouddirectory.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.batch_operation_index
    import aws_sdk_clouddirectory.types.batch_write_exception_type
    import aws_sdk_clouddirectory.types.exception_message


class BatchWriteException_(TypedDict):
    index: "aws_sdk_clouddirectory.types.batch_operation_index.BatchOperationIndex"
    type: NotRequired[
        "aws_sdk_clouddirectory.types.batch_write_exception_type.BatchWriteExceptionType"
    ]
    message: NotRequired[
        "aws_sdk_clouddirectory.types.exception_message.ExceptionMessage"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: BatchWriteException_) -> dict:
    out: dict = {}
    out["Index"] = value.get("index", 0)
    if "type" in value:
        import aws_sdk_clouddirectory.types.batch_write_exception_type

        out["Type"] = (
            aws_sdk_clouddirectory.types.batch_write_exception_type.serialize_json(
                value["type"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchWriteException_:
    out: BatchWriteException_ = {}  # type: ignore[typeddict-item]
    if "Index" in data:
        out["index"] = data["Index"]
    else:
        out["index"] = 0
    if "Type" in data:
        import aws_sdk_clouddirectory.types.batch_write_exception_type

        out["type"] = (
            aws_sdk_clouddirectory.types.batch_write_exception_type.deserialize_json(
                data["Type"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class BatchWriteException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.clouddirectory#BatchWriteException``."""

    code: str | None = "BatchWriteException"

    def __init__(self, data: BatchWriteException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BatchWriteException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "BatchWriteException":
        return cls(deserialize_json(data))
