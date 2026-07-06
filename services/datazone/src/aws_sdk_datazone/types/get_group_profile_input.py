"""Generated from Smithy shape ``com.amazonaws.datazone#GetGroupProfileInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.group_identifier


class GetGroupProfileInput(TypedDict, closed=True):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which the group profile exists.</p>"""
    group_identifier: "aws_sdk_datazone.types.group_identifier.GroupIdentifier"
    """<p>The identifier of the group profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGroupProfileInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetGroupProfileInput:
    out: GetGroupProfileInput = {}  # type: ignore[typeddict-item]
    return out
