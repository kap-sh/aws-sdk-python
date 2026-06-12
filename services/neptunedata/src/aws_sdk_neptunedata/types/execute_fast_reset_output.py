"""Generated from Smithy shape ``com.amazonaws.neptunedata#ExecuteFastResetOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_neptunedata.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_neptunedata.types.fast_reset_token

class ExecuteFastResetOutput(TypedDict):
    status: "str"
    """<p>The <code>status</code> is only returned for the <code>performDatabaseReset</code> action, and indicates whether or not the fast reset rquest is accepted.</p>"""
    payload: NotRequired["aws_sdk_neptunedata.types.fast_reset_token.FastResetToken"]
    """<p>The <code>payload</code> is only returned by the <code>initiateDatabaseReset</code> action, and contains the unique token to use with the <code>performDatabaseReset</code> action to make the reset occur.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ExecuteFastResetOutput) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    if "payload" in value:
        import aws_sdk_neptunedata.types.fast_reset_token
        out["payload"] = aws_sdk_neptunedata.types.fast_reset_token.serialize_json(value["payload"])
    return out


def deserialize_json(data: dict) -> ExecuteFastResetOutput:
    out: ExecuteFastResetOutput = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("ExecuteFastResetOutput.status required")
    if "payload" in data:
        import aws_sdk_neptunedata.types.fast_reset_token
        out["payload"] = aws_sdk_neptunedata.types.fast_reset_token.deserialize_json(data["payload"])
    return out