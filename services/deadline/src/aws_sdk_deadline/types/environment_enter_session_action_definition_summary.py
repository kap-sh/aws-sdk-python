"""Generated from Smithy shape ``com.amazonaws.deadline#EnvironmentEnterSessionActionDefinitionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.environment_id


class EnvironmentEnterSessionActionDefinitionSummary(TypedDict, closed=True):
    environment_id: "aws_sdk_deadline.types.environment_id.EnvironmentId"
    """<p>The environment ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentEnterSessionActionDefinitionSummary) -> dict:
    out: dict = {}
    out["environmentId"] = value["environment_id"]
    return out


def deserialize_json(data: dict) -> EnvironmentEnterSessionActionDefinitionSummary:
    out: EnvironmentEnterSessionActionDefinitionSummary = {}  # type: ignore[typeddict-item]
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    else:
        raise DeserializationError(
            "EnvironmentEnterSessionActionDefinitionSummary.environment_id required"
        )
    return out
