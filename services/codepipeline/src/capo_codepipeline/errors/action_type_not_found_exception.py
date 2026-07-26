"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionTypeNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codepipeline.errors import ServiceError

if TYPE_CHECKING:
    import capo_codepipeline.types.message


class ActionTypeNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_codepipeline.types.message.Message"]
    """<p>The message provided to the user in the event of an exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionTypeNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ActionTypeNotFoundException_:
    out: ActionTypeNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ActionTypeNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codepipeline#ActionTypeNotFoundException``."""

    code: str | None = "ActionTypeNotFoundException"

    def __init__(self, data: ActionTypeNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ActionTypeNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ActionTypeNotFoundException":
        return cls(deserialize_aws_json_1_1(data))
