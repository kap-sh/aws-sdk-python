"""Generated from Smithy shape ``com.amazonaws.codedeploy#InvalidLoadBalancerInfoException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codedeploy.errors import ServiceError

if TYPE_CHECKING:
    import capo_codedeploy.types.message


class InvalidLoadBalancerInfoException_(TypedDict, closed=True):
    message: NotRequired["capo_codedeploy.types.message.Message"]
    """<p>The message that corresponds to the exception thrown by CodeDeploy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidLoadBalancerInfoException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidLoadBalancerInfoException_:
    out: InvalidLoadBalancerInfoException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidLoadBalancerInfoException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codedeploy#InvalidLoadBalancerInfoException``."""

    code: str | None = "InvalidLoadBalancerInfoException"

    def __init__(self, data: InvalidLoadBalancerInfoException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidLoadBalancerInfoException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidLoadBalancerInfoException":
        return cls(deserialize_aws_json_1_1(data))
