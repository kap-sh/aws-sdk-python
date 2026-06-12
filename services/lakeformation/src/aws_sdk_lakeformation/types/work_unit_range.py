"""Generated from Smithy shape ``com.amazonaws.lakeformation#WorkUnitRange``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.work_unit_id_long
    import aws_sdk_lakeformation.types.work_unit_token_string


class WorkUnitRange(TypedDict):
    work_unit_id_max: "aws_sdk_lakeformation.types.work_unit_id_long.WorkUnitIdLong"
    """<p>Defines the maximum work unit ID in the range. The maximum value is inclusive.</p>"""
    work_unit_id_min: "aws_sdk_lakeformation.types.work_unit_id_long.WorkUnitIdLong"
    """<p>Defines the minimum work unit ID in the range.</p>"""
    work_unit_token: (
        "aws_sdk_lakeformation.types.work_unit_token_string.WorkUnitTokenString"
    )
    """<p>A work token used to query the execution service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkUnitRange) -> dict:
    out: dict = {}
    out["WorkUnitIdMax"] = value.get("work_unit_id_max", 0)
    out["WorkUnitIdMin"] = value.get("work_unit_id_min", 0)
    out["WorkUnitToken"] = value["work_unit_token"]
    return out


def deserialize_json(data: dict) -> WorkUnitRange:
    out: WorkUnitRange = {}  # type: ignore[typeddict-item]
    if "WorkUnitIdMax" in data:
        out["work_unit_id_max"] = data["WorkUnitIdMax"]
    else:
        out["work_unit_id_max"] = 0
    if "WorkUnitIdMin" in data:
        out["work_unit_id_min"] = data["WorkUnitIdMin"]
    else:
        out["work_unit_id_min"] = 0
    if "WorkUnitToken" in data:
        out["work_unit_token"] = data["WorkUnitToken"]
    else:
        raise DeserializationError("WorkUnitRange.work_unit_token required")
    return out
