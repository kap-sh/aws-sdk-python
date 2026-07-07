"""Generated from Smithy shape ``com.amazonaws.route53domains#TLDRulesViolation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_route_53_domains.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.error_message


class TLDRulesViolation_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_route_53_domains.types.error_message.ErrorMessage"]
    """<p>The top-level domain does not support this operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TLDRulesViolation_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TLDRulesViolation_:
    out: TLDRulesViolation_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class TLDRulesViolation(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.route53domains#TLDRulesViolation``."""

    code: str | None = "TLDRulesViolation"

    def __init__(self, data: TLDRulesViolation_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TLDRulesViolation",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "TLDRulesViolation":
        return cls(deserialize_aws_json_1_1(data))
