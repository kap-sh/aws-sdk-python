"""Generated from Smithy shape ``com.amazonaws.dataexchange#ServiceLimitExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_dataexchange.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.__double
    import aws_sdk_dataexchange.types.__string
    import aws_sdk_dataexchange.types.limit_name


class ServiceLimitExceededException_(TypedDict, closed=True):
    limit_name: NotRequired["aws_sdk_dataexchange.types.limit_name.LimitName"]
    """<p>The name of the limit that was reached.</p>"""
    limit_value: "aws_sdk_dataexchange.types.__double.__double"
    """<p>The value of the exceeded limit.</p>"""
    message: "aws_sdk_dataexchange.types.__string.__string"
    """<p>The request has exceeded the quotas imposed by the service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceLimitExceededException_) -> dict:
    out: dict = {}
    if "limit_name" in value:
        out["LimitName"] = value["limit_name"]
    out["LimitValue"] = value.get("limit_value", 0)
    out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ServiceLimitExceededException_:
    out: ServiceLimitExceededException_ = {}  # type: ignore[typeddict-item]
    if "LimitName" in data:
        out["limit_name"] = data["LimitName"]
    if "LimitValue" in data:
        out["limit_value"] = data["LimitValue"]
    else:
        out["limit_value"] = 0
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("ServiceLimitExceededException_.message required")
    return out


class ServiceLimitExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.dataexchange#ServiceLimitExceededException``."""

    code: str | None = "ServiceLimitExceededException"

    def __init__(self, data: ServiceLimitExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceLimitExceededException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ServiceLimitExceededException":
        return cls(deserialize_json(data))
