"""Generated from Smithy shape ``com.amazonaws.route53domains#UnsupportedTLD``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route_53_domains.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.error_message


class UnsupportedTLD_(TypedDict):
    message: NotRequired["aws_sdk_route_53_domains.types.error_message.ErrorMessage"]
    """<p>Amazon Route 53 does not support this top-level domain (TLD).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsupportedTLD_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnsupportedTLD_:
    out: UnsupportedTLD_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class UnsupportedTLD(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.route53domains#UnsupportedTLD``."""

    code: str | None = "UnsupportedTLD"

    def __init__(self, data: UnsupportedTLD_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedTLD",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "UnsupportedTLD":
        return cls(deserialize_aws_json_1_1(data))
