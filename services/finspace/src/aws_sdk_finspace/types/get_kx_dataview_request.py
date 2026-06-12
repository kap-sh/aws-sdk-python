"""Generated from Smithy shape ``com.amazonaws.finspace#GetKxDataviewRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace.types.database_name
    import aws_sdk_finspace.types.environment_id
    import aws_sdk_finspace.types.kx_dataview_name


class GetKxDataviewRequest(TypedDict):
    environment_id: "aws_sdk_finspace.types.environment_id.EnvironmentId"
    """<p>A unique identifier for the kdb environment, from where you want to retrieve the dataview details.</p>"""
    database_name: "aws_sdk_finspace.types.database_name.DatabaseName"
    """<p> The name of the database where you created the dataview.</p>"""
    dataview_name: "aws_sdk_finspace.types.kx_dataview_name.KxDataviewName"
    """<p>A unique identifier for the dataview.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetKxDataviewRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetKxDataviewRequest:
    out: GetKxDataviewRequest = {}  # type: ignore[typeddict-item]
    return out
