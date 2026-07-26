"""Generated from Smithy shape ``com.amazonaws.databrew#DescribeProjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.project_name


class DescribeProjectRequest(TypedDict, closed=True):
    name: "capo_databrew.types.project_name.ProjectName"
    """<p>The name of the project to be described.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeProjectRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeProjectRequest:
    out: DescribeProjectRequest = {}  # type: ignore[typeddict-item]
    return out
