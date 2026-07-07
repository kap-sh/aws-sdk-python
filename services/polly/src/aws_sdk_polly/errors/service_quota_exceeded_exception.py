"""Generated from Smithy shape ``com.amazonaws.polly#ServiceQuotaExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_polly._protocol.eventstream import HeaderValue, Message
from aws_sdk_polly.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_polly.types.error_message
    import aws_sdk_polly.types.quota_code
    import aws_sdk_polly.types.service_code


class ServiceQuotaExceededException_(TypedDict, closed=True):
    message: "aws_sdk_polly.types.error_message.ErrorMessage"
    quota_code: "aws_sdk_polly.types.quota_code.QuotaCode"
    """<p>The quota code identifying the specific quota.</p>"""
    service_code: "aws_sdk_polly.types.service_code.ServiceCode"
    """<p>The service code identifying the originating service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceQuotaExceededException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    import aws_sdk_polly.types.quota_code

    out["quotaCode"] = aws_sdk_polly.types.quota_code.serialize_json(
        value["quota_code"]
    )
    import aws_sdk_polly.types.service_code

    out["serviceCode"] = aws_sdk_polly.types.service_code.serialize_json(
        value["service_code"]
    )
    return out


def deserialize_json(data: dict) -> ServiceQuotaExceededException_:
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("ServiceQuotaExceededException_.message required")
    if "quotaCode" in data:
        import aws_sdk_polly.types.quota_code

        out["quota_code"] = aws_sdk_polly.types.quota_code.deserialize_json(
            data["quotaCode"]
        )
    else:
        raise DeserializationError("ServiceQuotaExceededException_.quota_code required")
    if "serviceCode" in data:
        import aws_sdk_polly.types.service_code

        out["service_code"] = aws_sdk_polly.types.service_code.deserialize_json(
            data["serviceCode"]
        )
    else:
        raise DeserializationError(
            "ServiceQuotaExceededException_.service_code required"
        )
    return out


class ServiceQuotaExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.polly#ServiceQuotaExceededException``."""

    code: str | None = "ServiceQuotaExceededException"

    def __init__(self, data: ServiceQuotaExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceQuotaExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ServiceQuotaExceededException":
        return cls(deserialize_json(data))


def serialize_event_json(value: ServiceQuotaExceededException_) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "ServiceQuotaExceededException"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> ServiceQuotaExceededException_:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: ServiceQuotaExceededException_ = {}  # type: ignore[typeddict-item]
    return out
