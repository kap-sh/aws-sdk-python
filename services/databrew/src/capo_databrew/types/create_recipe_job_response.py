"""Generated from Smithy shape ``com.amazonaws.databrew#CreateRecipeJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import capo_databrew.types.job_name


class CreateRecipeJobResponse(TypedDict, closed=True):
    name: "capo_databrew.types.job_name.JobName"
    """<p>The name of the job that you created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRecipeJobResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> CreateRecipeJobResponse:
    out: CreateRecipeJobResponse = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateRecipeJobResponse.name required")
    return out
