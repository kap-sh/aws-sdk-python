"""Generated from Smithy shape ``com.amazonaws.route53domains#InvalidInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route_53_domains.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_route_53_domains.types.error_message


class InvalidInput_(TypedDict):
    message: NotRequired["aws_sdk_route_53_domains.types.error_message.ErrorMessage"]
    """<p>The requested item is not acceptable. For example, for an OperationId it might refer to the ID of an operation that is already completed. For a domain name, it might not be a valid domain name or belong to the requester account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidInput_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidInput_:
    out: InvalidInput_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidInput(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.route53domains#InvalidInput``."""

    code: str | None = "InvalidInput"

    def __init__(self, data: InvalidInput_):
        super().__init__(
            "client", is_throttling_error=False, is_retryable=False, code="InvalidInput"
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidInput":
        return cls(deserialize_aws_json_1_1(data))
