"""Generated from Smithy shape ``com.amazonaws.datazone#SubscribedProjectInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.project_id


class SubscribedProjectInput(TypedDict, closed=True):
    identifier: NotRequired["capo_datazone.types.project_id.ProjectId"]
    """<p>The identifier of the project that is to be given a subscription grant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubscribedProjectInput) -> dict:
    out: dict = {}
    if "identifier" in value:
        out["identifier"] = value["identifier"]
    return out


def deserialize_json(data: dict) -> SubscribedProjectInput:
    out: SubscribedProjectInput = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    return out
