"""Generated from Smithy shape ``com.amazonaws.datazone#GetConnectionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.connection_id
    import aws_sdk_datazone.types.domain_id


class GetConnectionInput(TypedDict, closed=True):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where we get the connection.</p>"""
    identifier: "aws_sdk_datazone.types.connection_id.ConnectionId"
    """<p>The connection ID.</p>"""
    with_secret: NotRequired["bool"]
    """<p>Specifies whether a connection has a secret.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConnectionInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetConnectionInput:
    out: GetConnectionInput = {}  # type: ignore[typeddict-item]
    return out
