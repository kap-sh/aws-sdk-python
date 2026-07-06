"""Generated from Smithy shape ``com.amazonaws.qbusiness#DeleteApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id


class DeleteApplicationRequest(TypedDict, closed=True):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteApplicationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteApplicationRequest:
    out: DeleteApplicationRequest = {}  # type: ignore[typeddict-item]
    return out
