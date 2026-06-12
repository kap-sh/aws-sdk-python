"""Generated from Smithy shape ``com.amazonaws.amplify#GenerateAccessLogsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amplify.types.log_url


class GenerateAccessLogsResult(TypedDict):
    log_url: NotRequired["aws_sdk_amplify.types.log_url.LogUrl"]
    """<p>The pre-signed URL for the requested access logs. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerateAccessLogsResult) -> dict:
    out: dict = {}
    if "log_url" in value:
        out["logUrl"] = value["log_url"]
    return out


def deserialize_json(data: dict) -> GenerateAccessLogsResult:
    out: GenerateAccessLogsResult = {}  # type: ignore[typeddict-item]
    if "logUrl" in data:
        out["log_url"] = data["logUrl"]
    return out
