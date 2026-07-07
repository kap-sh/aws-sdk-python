"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetSchemaInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.collaboration_identifier
    import aws_sdk_cleanrooms.types.table_alias


class GetSchemaInput(TypedDict, closed=True):
    collaboration_identifier: (
        "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier"
    )
    """<p>A unique identifier for the collaboration that the schema belongs to. Currently accepts a collaboration ID.</p>"""
    name: "aws_sdk_cleanrooms.types.table_alias.TableAlias"
    """<p>The name of the relation to retrieve the schema for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSchemaInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSchemaInput:
    out: GetSchemaInput = {}  # type: ignore[typeddict-item]
    return out
