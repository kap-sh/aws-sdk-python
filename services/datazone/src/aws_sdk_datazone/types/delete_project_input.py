"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteProjectInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.project_id


class DeleteProjectInput(TypedDict, closed=True):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the project is deleted.</p>"""
    identifier: "aws_sdk_datazone.types.project_id.ProjectId"
    """<p>The identifier of the project that is to be deleted.</p>"""
    skip_deletion_check: NotRequired["bool"]
    """<p>Specifies the optional flag to delete all child entities within the project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteProjectInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteProjectInput:
    out: DeleteProjectInput = {}  # type: ignore[typeddict-item]
    return out
