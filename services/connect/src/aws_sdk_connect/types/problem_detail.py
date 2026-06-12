"""Generated from Smithy shape ``com.amazonaws.connect#ProblemDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.problem_message_string


class ProblemDetail(TypedDict):
    message: NotRequired[
        "aws_sdk_connect.types.problem_message_string.ProblemMessageString"
    ]
    """<p>The problem detail's message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProblemDetail) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ProblemDetail:
    out: ProblemDetail = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out
