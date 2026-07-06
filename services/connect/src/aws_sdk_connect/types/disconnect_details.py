"""Generated from Smithy shape ``com.amazonaws.connect#DisconnectDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.potential_disconnect_issue


class DisconnectDetails(TypedDict, closed=True):
    potential_disconnect_issue: NotRequired[
        "aws_sdk_connect.types.potential_disconnect_issue.PotentialDisconnectIssue"
    ]
    """<p>Indicates the potential disconnection issues for a call. This field is not populated if the service does not detect potential issues.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisconnectDetails) -> dict:
    out: dict = {}
    if "potential_disconnect_issue" in value:
        out["PotentialDisconnectIssue"] = value["potential_disconnect_issue"]
    return out


def deserialize_json(data: dict) -> DisconnectDetails:
    out: DisconnectDetails = {}  # type: ignore[typeddict-item]
    if "PotentialDisconnectIssue" in data:
        out["potential_disconnect_issue"] = data["PotentialDisconnectIssue"]
    return out
