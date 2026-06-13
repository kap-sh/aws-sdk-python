"""Generated from Smithy shape ``com.amazonaws.datazone#GetFormTypeInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.form_type_identifier
    import aws_sdk_datazone.types.revision


class GetFormTypeInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which this metadata form type exists.</p>"""
    form_type_identifier: (
        "aws_sdk_datazone.types.form_type_identifier.FormTypeIdentifier"
    )
    """<p>The ID of the metadata form type.</p>"""
    revision: NotRequired["aws_sdk_datazone.types.revision.Revision"]
    """<p>The revision of this metadata form type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFormTypeInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFormTypeInput:
    out: GetFormTypeInput = {}  # type: ignore[typeddict-item]
    return out
