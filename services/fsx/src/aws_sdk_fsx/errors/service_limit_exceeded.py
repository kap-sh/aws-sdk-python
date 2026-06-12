"""Generated from Smithy shape ``com.amazonaws.fsx#ServiceLimitExceeded``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_fsx.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_fsx.types.error_message
    import aws_sdk_fsx.types.service_limit


class ServiceLimitExceeded_(TypedDict):
    limit: NotRequired["aws_sdk_fsx.types.service_limit.ServiceLimit"]
    """<p>Enumeration of the service limit that was exceeded. </p>"""
    message: NotRequired["aws_sdk_fsx.types.error_message.ErrorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceLimitExceeded_) -> dict:
    out: dict = {}
    if "limit" in value:
        import aws_sdk_fsx.types.service_limit

        out["Limit"] = aws_sdk_fsx.types.service_limit.serialize_aws_json_1_1(
            value["limit"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceLimitExceeded_:
    out: ServiceLimitExceeded_ = {}  # type: ignore[typeddict-item]
    if "Limit" in data:
        import aws_sdk_fsx.types.service_limit

        out["limit"] = aws_sdk_fsx.types.service_limit.deserialize_aws_json_1_1(
            data["Limit"]
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class ServiceLimitExceeded(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.fsx#ServiceLimitExceeded``."""

    code: str | None = "ServiceLimitExceeded"

    def __init__(self, data: ServiceLimitExceeded_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceLimitExceeded",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ServiceLimitExceeded":
        return cls(deserialize_aws_json_1_1(data))
