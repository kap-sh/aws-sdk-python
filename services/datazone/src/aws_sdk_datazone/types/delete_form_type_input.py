"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteFormTypeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.form_type_identifier


class DeleteFormTypeInput(TypedDict, closed=True):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the metadata form type is deleted.</p>"""
    form_type_identifier: (
        "aws_sdk_datazone.types.form_type_identifier.FormTypeIdentifier"
    )
    """<p>The ID of the metadata form type that is deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFormTypeInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFormTypeInput:
    out: DeleteFormTypeInput = {}  # type: ignore[typeddict-item]
    return out
