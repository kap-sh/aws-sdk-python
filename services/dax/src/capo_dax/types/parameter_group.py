"""Generated from Smithy shape ``com.amazonaws.dax#ParameterGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dax.types.string


class ParameterGroup(TypedDict, closed=True):
    parameter_group_name: NotRequired["capo_dax.types.string.String"]
    """<p>The name of the parameter group.</p>"""
    description: NotRequired["capo_dax.types.string.String"]
    """<p>A description of the parameter group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterGroup) -> dict:
    out: dict = {}
    if "parameter_group_name" in value:
        out["ParameterGroupName"] = value["parameter_group_name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ParameterGroup:
    out: ParameterGroup = {}  # type: ignore[typeddict-item]
    if "ParameterGroupName" in data:
        out["parameter_group_name"] = data["ParameterGroupName"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
