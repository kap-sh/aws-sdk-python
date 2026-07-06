"""Generated from Smithy shape ``com.amazonaws.appconfig#PayloadTooLargeException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appconfig.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.bytes_measure
    import aws_sdk_appconfig.types.float
    import aws_sdk_appconfig.types.string


class PayloadTooLargeException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_appconfig.types.string.String"]
    measure: NotRequired["aws_sdk_appconfig.types.bytes_measure.BytesMeasure"]
    limit: "aws_sdk_appconfig.types.float.Float"
    size: "aws_sdk_appconfig.types.float.Float"


# --- restJson1 ser/de ---
def serialize_json(value: PayloadTooLargeException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "measure" in value:
        import aws_sdk_appconfig.types.bytes_measure

        out["Measure"] = aws_sdk_appconfig.types.bytes_measure.serialize_json(
            value["measure"]
        )
    out["Limit"] = value.get("limit", 0)
    out["Size"] = value.get("size", 0)
    return out


def deserialize_json(data: dict) -> PayloadTooLargeException_:
    out: PayloadTooLargeException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Measure" in data:
        import aws_sdk_appconfig.types.bytes_measure

        out["measure"] = aws_sdk_appconfig.types.bytes_measure.deserialize_json(
            data["Measure"]
        )
    if "Limit" in data:
        out["limit"] = data["Limit"]
    else:
        out["limit"] = 0
    if "Size" in data:
        out["size"] = data["Size"]
    else:
        out["size"] = 0
    return out


class PayloadTooLargeException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.appconfig#PayloadTooLargeException``."""

    code: str | None = "PayloadTooLargeException"

    def __init__(self, data: PayloadTooLargeException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="PayloadTooLargeException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "PayloadTooLargeException":
        return cls(deserialize_json(data))
