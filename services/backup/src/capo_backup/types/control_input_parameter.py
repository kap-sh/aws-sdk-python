"""Generated from Smithy shape ``com.amazonaws.backup#ControlInputParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.parameter_name
    import capo_backup.types.parameter_value


class ControlInputParameter(TypedDict, closed=True):
    parameter_name: NotRequired["capo_backup.types.parameter_name.ParameterName"]
    """<p>The name of a parameter, for example, <code>BackupPlanFrequency</code>.</p>"""
    parameter_value: NotRequired["capo_backup.types.parameter_value.ParameterValue"]
    """<p>The value of parameter, for example, <code>hourly</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ControlInputParameter) -> dict:
    out: dict = {}
    if "parameter_name" in value:
        out["ParameterName"] = value["parameter_name"]
    if "parameter_value" in value:
        out["ParameterValue"] = value["parameter_value"]
    return out


def deserialize_json(data: dict) -> ControlInputParameter:
    out: ControlInputParameter = {}  # type: ignore[typeddict-item]
    if "ParameterName" in data:
        out["parameter_name"] = data["ParameterName"]
    if "ParameterValue" in data:
        out["parameter_value"] = data["ParameterValue"]
    return out
