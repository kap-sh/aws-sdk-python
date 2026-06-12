"""Generated from Smithy shape ``com.amazonaws.route53domains#OperationLimitExceeded``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route_53_domains.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.error_message


class OperationLimitExceeded_(TypedDict):
    message: NotRequired["aws_sdk_route_53_domains.types.error_message.ErrorMessage"]
    """<p>The number of operations or jobs running exceeded the allowed threshold for the account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperationLimitExceeded_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OperationLimitExceeded_:
    out: OperationLimitExceeded_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class OperationLimitExceeded(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.route53domains#OperationLimitExceeded``."""

    code: str | None = "OperationLimitExceeded"

    def __init__(self, data: OperationLimitExceeded_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OperationLimitExceeded",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "OperationLimitExceeded":
        return cls(deserialize_aws_json_1_1(data))
