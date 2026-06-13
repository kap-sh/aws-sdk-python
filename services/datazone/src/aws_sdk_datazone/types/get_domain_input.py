"""Generated from Smithy shape ``com.amazonaws.datazone#GetDomainInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id


class GetDomainInput(TypedDict):
    identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the specified Amazon DataZone domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDomainInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDomainInput:
    out: GetDomainInput = {}  # type: ignore[typeddict-item]
    return out
