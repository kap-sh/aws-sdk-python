"""Generated from Smithy shape ``com.amazonaws.iot#DeleteCommandResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.status_code


class DeleteCommandResponse(TypedDict, closed=True):
    status_code: "aws_sdk_iot.types.status_code.StatusCode"
    """<p>The status code for the command deletion request. The status code is in the 200 range for a successful request.</p> <ul> <li> <p>If the command hasn't been deprecated, or has been deprecated for a duration that is shorter than the maximum time out duration of 12 hours, when calling the <code>DeleteCommand</code> request, the deletion will be scheduled and a 202 status code will be returned. While the command is being deleted, it will be in a <code>pendingDeletion</code> state. Once the time out duration has been reached, the command will be permanently removed from your account.</p> </li> <li> <p>If the command has been deprecated for a duration that is longer than the maximum time out duration of 12 hours, when calling the <code>DeleteCommand</code> request, the command will be deleted immediately and a 204 status code will be returned.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCommandResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCommandResponse:
    out: DeleteCommandResponse = {}  # type: ignore[typeddict-item]
    return out
