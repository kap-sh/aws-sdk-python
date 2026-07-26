"""Generated from Smithy shape ``com.amazonaws.route53recoverycluster#EndpointTemporarilyUnavailableException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route53_recovery_cluster.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_route53_recovery_cluster.types.string


class EndpointTemporarilyUnavailableException_(TypedDict, closed=True):
    message: "capo_route53_recovery_cluster.types.string.String"


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EndpointTemporarilyUnavailableException_) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EndpointTemporarilyUnavailableException_:
    out: EndpointTemporarilyUnavailableException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError(
            "EndpointTemporarilyUnavailableException_.message required"
        )
    return out


class EndpointTemporarilyUnavailableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.route53recoverycluster#EndpointTemporarilyUnavailableException``."""

    code: str | None = "EndpointTemporarilyUnavailableException"

    def __init__(self, data: EndpointTemporarilyUnavailableException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="EndpointTemporarilyUnavailableException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "EndpointTemporarilyUnavailableException":
        return cls(deserialize_aws_json_1_0(data))
