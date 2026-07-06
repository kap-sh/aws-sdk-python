"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteConnectionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.connection_id
    import aws_sdk_datazone.types.domain_id


class DeleteConnectionInput(TypedDict, closed=True):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where the connection is deleted.</p>"""
    identifier: "aws_sdk_datazone.types.connection_id.ConnectionId"
    """<p>The ID of the connection that is deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConnectionInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConnectionInput:
    out: DeleteConnectionInput = {}  # type: ignore[typeddict-item]
    return out
