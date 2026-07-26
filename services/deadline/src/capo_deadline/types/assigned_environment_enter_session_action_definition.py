"""Generated from Smithy shape ``com.amazonaws.deadline#AssignedEnvironmentEnterSessionActionDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.environment_id


class AssignedEnvironmentEnterSessionActionDefinition(TypedDict, closed=True):
    environment_id: "capo_deadline.types.environment_id.EnvironmentId"
    """<p>The environment ID of the assigned environment at the start of a session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssignedEnvironmentEnterSessionActionDefinition) -> dict:
    out: dict = {}
    out["environmentId"] = value["environment_id"]
    return out


def deserialize_json(data: dict) -> AssignedEnvironmentEnterSessionActionDefinition:
    out: AssignedEnvironmentEnterSessionActionDefinition = {}  # type: ignore[typeddict-item]
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    else:
        raise DeserializationError(
            "AssignedEnvironmentEnterSessionActionDefinition.environment_id required"
        )
    return out
