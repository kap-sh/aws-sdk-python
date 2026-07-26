"""Generated from Smithy shape ``com.amazonaws.docdbelastic#GetPendingMaintenanceActionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_docdb_elastic.types.input_string


class GetPendingMaintenanceActionInput(TypedDict, closed=True):
    resource_arn: "capo_docdb_elastic.types.input_string.InputString"
    """<p>Retrieves pending maintenance actions for a specific Amazon Resource Name (ARN).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPendingMaintenanceActionInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPendingMaintenanceActionInput:
    out: GetPendingMaintenanceActionInput = {}  # type: ignore[typeddict-item]
    return out
