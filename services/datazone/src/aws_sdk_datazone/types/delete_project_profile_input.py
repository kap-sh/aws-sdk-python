"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteProjectProfileInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.project_profile_id


class DeleteProjectProfileInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where a project profile is deleted.</p>"""
    identifier: "aws_sdk_datazone.types.project_profile_id.ProjectProfileId"
    """<p>The ID of the project profile that is deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteProjectProfileInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteProjectProfileInput:
    out: DeleteProjectProfileInput = {}  # type: ignore[typeddict-item]
    return out
