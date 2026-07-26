"""Generated from Smithy shape ``com.amazonaws.securityagent#ErrorInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.error_code


class ErrorInformation(TypedDict, closed=True):
    code: NotRequired["capo_securityagent.types.error_code.ErrorCode"]
    """<p>The error code. Valid values include CLIENT_ERROR, INTERNAL_ERROR, and STOPPED_BY_USER.</p>"""
    message: NotRequired["str"]
    """<p>A message describing the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorInformation) -> dict:
    out: dict = {}
    if "code" in value:
        import capo_securityagent.types.error_code

        out["code"] = capo_securityagent.types.error_code.serialize_json(value["code"])
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ErrorInformation:
    out: ErrorInformation = {}  # type: ignore[typeddict-item]
    if "code" in data:
        import capo_securityagent.types.error_code

        out["code"] = capo_securityagent.types.error_code.deserialize_json(data["code"])
    if "message" in data:
        out["message"] = data["message"]
    return out
