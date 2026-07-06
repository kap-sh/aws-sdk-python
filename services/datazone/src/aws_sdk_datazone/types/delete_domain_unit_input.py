"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteDomainUnitInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.domain_unit_id


class DeleteDomainUnitInput(TypedDict, closed=True):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where you want to delete a domain unit.</p>"""
    identifier: "aws_sdk_datazone.types.domain_unit_id.DomainUnitId"
    """<p>The ID of the domain unit that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDomainUnitInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDomainUnitInput:
    out: DeleteDomainUnitInput = {}  # type: ignore[typeddict-item]
    return out
