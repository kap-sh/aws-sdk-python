"""Generated from Smithy shape ``com.amazonaws.dax#CreateParameterGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dax.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dax.types.string


class CreateParameterGroupRequest(TypedDict, closed=True):
    parameter_group_name: "capo_dax.types.string.String"
    """<p>The name of the parameter group to apply to all of the clusters in this replication group.</p>"""
    description: NotRequired["capo_dax.types.string.String"]
    """<p>A description of the parameter group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateParameterGroupRequest) -> dict:
    out: dict = {}
    out["ParameterGroupName"] = value["parameter_group_name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateParameterGroupRequest:
    out: CreateParameterGroupRequest = {}  # type: ignore[typeddict-item]
    if "ParameterGroupName" in data:
        out["parameter_group_name"] = data["ParameterGroupName"]
    else:
        raise DeserializationError(
            "CreateParameterGroupRequest.parameter_group_name required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    return out
