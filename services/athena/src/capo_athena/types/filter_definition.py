"""Generated from Smithy shape ``com.amazonaws.athena#FilterDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.notebook_name


class FilterDefinition(TypedDict, closed=True):
    name: NotRequired["capo_athena.types.notebook_name.NotebookName"]
    """<p>The name of the notebook to search for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterDefinition) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FilterDefinition:
    out: FilterDefinition = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
