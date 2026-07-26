"""Generated from Smithy shape ``com.amazonaws.ecr#LayerInaccessibleException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecr.errors import ServiceError

if TYPE_CHECKING:
    import capo_ecr.types.exception_message


class LayerInaccessibleException_(TypedDict, closed=True):
    message: NotRequired["capo_ecr.types.exception_message.ExceptionMessage"]
    """<p>The error message associated with the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LayerInaccessibleException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LayerInaccessibleException_:
    out: LayerInaccessibleException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class LayerInaccessibleException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecr#LayerInaccessibleException``."""

    code: str | None = "LayerInaccessibleException"

    def __init__(self, data: LayerInaccessibleException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="LayerInaccessibleException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "LayerInaccessibleException":
        return cls(deserialize_aws_json_1_1(data))
