"""Generated from Smithy shape ``com.amazonaws.codedeploy#InvalidExternalIdException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codedeploy.errors import ServiceError

if TYPE_CHECKING:
    import capo_codedeploy.types.message


class InvalidExternalIdException_(TypedDict, closed=True):
    message: NotRequired["capo_codedeploy.types.message.Message"]
    """<p>The message that corresponds to the exception thrown by CodeDeploy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidExternalIdException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidExternalIdException_:
    out: InvalidExternalIdException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidExternalIdException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codedeploy#InvalidExternalIdException``."""

    code: str | None = "InvalidExternalIdException"

    def __init__(self, data: InvalidExternalIdException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidExternalIdException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidExternalIdException":
        return cls(deserialize_aws_json_1_1(data))
