"""Generated from Smithy shape ``com.amazonaws.appstream#DrainSessionInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appstream.types.string


class DrainSessionInstanceRequest(TypedDict, closed=True):
    session_id: NotRequired["aws_sdk_appstream.types.string.String"]
    """<p>The identifier of the streaming session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DrainSessionInstanceRequest) -> dict:
    out: dict = {}
    if "session_id" in value:
        out["SessionId"] = value["session_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DrainSessionInstanceRequest:
    out: DrainSessionInstanceRequest = {}  # type: ignore[typeddict-item]
    if "SessionId" in data:
        out["session_id"] = data["SessionId"]
    return out
