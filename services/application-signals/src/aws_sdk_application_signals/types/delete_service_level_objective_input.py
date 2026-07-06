"""Generated from Smithy shape ``com.amazonaws.applicationsignals#DeleteServiceLevelObjectiveInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.service_level_objective_id


class DeleteServiceLevelObjectiveInput(TypedDict, closed=True):
    id: "aws_sdk_application_signals.types.service_level_objective_id.ServiceLevelObjectiveId"
    """<p>The ARN or name of the service level objective to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteServiceLevelObjectiveInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteServiceLevelObjectiveInput:
    out: DeleteServiceLevelObjectiveInput = {}  # type: ignore[typeddict-item]
    return out
