"""Generated from Smithy shape ``com.amazonaws.dax#DeleteParameterGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_dax.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dax.types.string


class DeleteParameterGroupRequest(TypedDict):
    parameter_group_name: "aws_sdk_dax.types.string.String"
    """<p>The name of the parameter group to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteParameterGroupRequest) -> dict:
    out: dict = {}
    out["ParameterGroupName"] = value["parameter_group_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteParameterGroupRequest:
    out: DeleteParameterGroupRequest = {}  # type: ignore[typeddict-item]
    if "ParameterGroupName" in data:
        out["parameter_group_name"] = data["ParameterGroupName"]
    else:
        raise DeserializationError(
            "DeleteParameterGroupRequest.parameter_group_name required"
        )
    return out
