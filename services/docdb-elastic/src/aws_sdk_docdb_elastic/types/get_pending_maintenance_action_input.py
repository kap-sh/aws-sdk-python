"""Generated from Smithy shape ``com.amazonaws.docdbelastic#GetPendingMaintenanceActionInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_docdb_elastic.types.input_string


class GetPendingMaintenanceActionInput(TypedDict):
    resource_arn: "aws_sdk_docdb_elastic.types.input_string.InputString"
    """<p>Retrieves pending maintenance actions for a specific Amazon Resource Name (ARN).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPendingMaintenanceActionInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPendingMaintenanceActionInput:
    out: GetPendingMaintenanceActionInput = {}  # type: ignore[typeddict-item]
    return out
