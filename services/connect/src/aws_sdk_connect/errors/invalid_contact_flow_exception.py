"""Generated from Smithy shape ``com.amazonaws.connect#InvalidContactFlowException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_connect.types.problems


class InvalidContactFlowException_(TypedDict, closed=True):
    problems: NotRequired["aws_sdk_connect.types.problems.Problems"]
    """<p>The problems with the flow. Please fix before trying again.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidContactFlowException_) -> dict:
    out: dict = {}
    if "problems" in value:
        import aws_sdk_connect.types.problems

        out["problems"] = aws_sdk_connect.types.problems.serialize_json(
            value["problems"]
        )
    return out


def deserialize_json(data: dict) -> InvalidContactFlowException_:
    out: InvalidContactFlowException_ = {}  # type: ignore[typeddict-item]
    if "problems" in data:
        import aws_sdk_connect.types.problems

        out["problems"] = aws_sdk_connect.types.problems.deserialize_json(
            data["problems"]
        )
    return out


class InvalidContactFlowException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.connect#InvalidContactFlowException``."""

    code: str | None = "InvalidContactFlowException"

    def __init__(self, data: InvalidContactFlowException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidContactFlowException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "InvalidContactFlowException":
        return cls(deserialize_json(data))
