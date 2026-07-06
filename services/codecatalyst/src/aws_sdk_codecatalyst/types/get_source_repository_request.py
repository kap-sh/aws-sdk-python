"""Generated from Smithy shape ``com.amazonaws.codecatalyst#GetSourceRepositoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.name_string
    import aws_sdk_codecatalyst.types.source_repository_name_string


class GetSourceRepositoryRequest(TypedDict, closed=True):
    space_name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    project_name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the project in the space.</p>"""
    name: "aws_sdk_codecatalyst.types.source_repository_name_string.SourceRepositoryNameString"
    """<p>The name of the source repository.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSourceRepositoryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSourceRepositoryRequest:
    out: GetSourceRepositoryRequest = {}  # type: ignore[typeddict-item]
    return out
