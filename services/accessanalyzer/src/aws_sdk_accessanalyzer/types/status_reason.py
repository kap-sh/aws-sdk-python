"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#StatusReason``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.reason_code


class StatusReason(TypedDict, closed=True):
    code: "aws_sdk_accessanalyzer.types.reason_code.ReasonCode"
    """<p>The reason code for the current status of the analyzer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StatusReason) -> dict:
    out: dict = {}
    out["code"] = value["code"]
    return out


def deserialize_json(data: dict) -> StatusReason:
    out: StatusReason = {}  # type: ignore[typeddict-item]
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("StatusReason.code required")
    return out
