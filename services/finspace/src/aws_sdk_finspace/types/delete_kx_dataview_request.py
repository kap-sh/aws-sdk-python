"""Generated from Smithy shape ``com.amazonaws.finspace#DeleteKxDataviewRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace.types.client_token_string
    import aws_sdk_finspace.types.database_name
    import aws_sdk_finspace.types.environment_id
    import aws_sdk_finspace.types.kx_dataview_name


class DeleteKxDataviewRequest(TypedDict, closed=True):
    environment_id: "aws_sdk_finspace.types.environment_id.EnvironmentId"
    """<p>A unique identifier for the kdb environment, from where you want to delete the dataview. </p>"""
    database_name: "aws_sdk_finspace.types.database_name.DatabaseName"
    """<p>The name of the database whose dataview you want to delete.</p>"""
    dataview_name: "aws_sdk_finspace.types.kx_dataview_name.KxDataviewName"
    """<p>The name of the dataview that you want to delete.</p>"""
    client_token: "aws_sdk_finspace.types.client_token_string.ClientTokenString"
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteKxDataviewRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteKxDataviewRequest:
    out: DeleteKxDataviewRequest = {}  # type: ignore[typeddict-item]
    return out
