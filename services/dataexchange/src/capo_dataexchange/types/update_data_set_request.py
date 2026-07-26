"""Generated from Smithy shape ``com.amazonaws.dataexchange#UpdateDataSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.description
    import capo_dataexchange.types.id
    import capo_dataexchange.types.name


class UpdateDataSetRequest(TypedDict, closed=True):
    data_set_id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for a data set.</p>"""
    description: NotRequired["capo_dataexchange.types.description.Description"]
    """<p>The description for the data set.</p>"""
    name: NotRequired["capo_dataexchange.types.name.Name"]
    """<p>The name of the data set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataSetRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateDataSetRequest:
    out: UpdateDataSetRequest = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
