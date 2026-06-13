"""Generated from Smithy shape ``com.amazonaws.datazone#GetProjectProfileInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.project_profile_id


class GetProjectProfileInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain.</p>"""
    identifier: "aws_sdk_datazone.types.project_profile_id.ProjectProfileId"
    """<p>The ID of the project profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProjectProfileInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetProjectProfileInput:
    out: GetProjectProfileInput = {}  # type: ignore[typeddict-item]
    return out
