"""Generated from Smithy shape ``com.amazonaws.iam#PolicyEvaluationException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_iam.types.policy_evaluation_error_message


class PolicyEvaluationException_(TypedDict):
    message: NotRequired[
        "aws_sdk_iam.types.policy_evaluation_error_message.policyEvaluationErrorMessage"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: PolicyEvaluationException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> PolicyEvaluationException_:
    out: PolicyEvaluationException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class PolicyEvaluationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iam#PolicyEvaluationException``."""

    code: str | None = "PolicyEvaluationException"

    def __init__(self, data: PolicyEvaluationException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="PolicyEvaluationException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "PolicyEvaluationException":
        return cls(deserialize_query(el))
