"""Generated from Smithy shape ``com.amazonaws.datazone#SubscribedProjectInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.project_id


class SubscribedProjectInput(TypedDict):
    identifier: NotRequired["aws_sdk_datazone.types.project_id.ProjectId"]
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
