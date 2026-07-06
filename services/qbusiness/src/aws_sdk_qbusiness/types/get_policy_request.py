"""Generated from Smithy shape ``com.amazonaws.qbusiness#GetPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_id


class GetPolicyRequest(TypedDict, closed=True):
    application_id: "aws_sdk_qbusiness.types.application_id.ApplicationId"
    """<p>The unique identifier of the Amazon Q Business application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPolicyRequest:
    out: GetPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
