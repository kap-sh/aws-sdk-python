"""Generated from Smithy shape ``com.amazonaws.route53domains#DomainLimitExceeded``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_route_53_domains.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.error_message


class DomainLimitExceeded_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_route_53_domains.types.error_message.ErrorMessage"]
    """<p>The number of domains has exceeded the allowed threshold for the account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainLimitExceeded_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DomainLimitExceeded_:
    out: DomainLimitExceeded_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class DomainLimitExceeded(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.route53domains#DomainLimitExceeded``."""

    code: str | None = "DomainLimitExceeded"

    def __init__(self, data: DomainLimitExceeded_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DomainLimitExceeded",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "DomainLimitExceeded":
        return cls(deserialize_aws_json_1_1(data))
