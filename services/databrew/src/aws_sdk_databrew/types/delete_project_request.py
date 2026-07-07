"""Generated from Smithy shape ``com.amazonaws.databrew#DeleteProjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_databrew.types.project_name


class DeleteProjectRequest(TypedDict, closed=True):
    name: "aws_sdk_databrew.types.project_name.ProjectName"
    """<p>The name of the project to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteProjectRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteProjectRequest:
    out: DeleteProjectRequest = {}  # type: ignore[typeddict-item]
    return out
