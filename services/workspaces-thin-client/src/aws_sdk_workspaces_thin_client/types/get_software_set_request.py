"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#GetSoftwareSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_thin_client.types.software_set_id


class GetSoftwareSetRequest(TypedDict, closed=True):
    id: "aws_sdk_workspaces_thin_client.types.software_set_id.SoftwareSetId"
    """<p>The ID of the software set for which to return information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSoftwareSetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSoftwareSetRequest:
    out: GetSoftwareSetRequest = {}  # type: ignore[typeddict-item]
    return out
