"""Generated from Smithy shape ``com.amazonaws.deadline#EnvironmentExitSessionActionDefinitionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.environment_id


class EnvironmentExitSessionActionDefinitionSummary(TypedDict, closed=True):
    environment_id: "capo_deadline.types.environment_id.EnvironmentId"
    """<p>The environment ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentExitSessionActionDefinitionSummary) -> dict:
    out: dict = {}
    out["environmentId"] = value["environment_id"]
    return out


def deserialize_json(data: dict) -> EnvironmentExitSessionActionDefinitionSummary:
    out: EnvironmentExitSessionActionDefinitionSummary = {}  # type: ignore[typeddict-item]
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    else:
        raise DeserializationError(
            "EnvironmentExitSessionActionDefinitionSummary.environment_id required"
        )
    return out
