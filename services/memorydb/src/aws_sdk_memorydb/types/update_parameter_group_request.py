"""Generated from Smithy shape ``com.amazonaws.memorydb#UpdateParameterGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_memorydb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.parameter_name_value_list
    import aws_sdk_memorydb.types.string


class UpdateParameterGroupRequest(TypedDict):
    parameter_group_name: "aws_sdk_memorydb.types.string.String"
    """<p>The name of the parameter group to update.</p>"""
    parameter_name_values: (
        "aws_sdk_memorydb.types.parameter_name_value_list.ParameterNameValueList"
    )
    """<p>An array of parameter names and values for the parameter update. You must supply at least one parameter name and value; subsequent arguments are optional. A maximum of 20 parameters may be updated per request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateParameterGroupRequest) -> dict:
    out: dict = {}
    out["ParameterGroupName"] = value["parameter_group_name"]
    import aws_sdk_memorydb.types.parameter_name_value_list

    out["ParameterNameValues"] = (
        aws_sdk_memorydb.types.parameter_name_value_list.serialize_aws_json_1_1(
            value["parameter_name_values"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateParameterGroupRequest:
    out: UpdateParameterGroupRequest = {}  # type: ignore[typeddict-item]
    if "ParameterGroupName" in data:
        out["parameter_group_name"] = data["ParameterGroupName"]
    else:
        raise DeserializationError(
            "UpdateParameterGroupRequest.parameter_group_name required"
        )
    if "ParameterNameValues" in data:
        import aws_sdk_memorydb.types.parameter_name_value_list

        out["parameter_name_values"] = (
            aws_sdk_memorydb.types.parameter_name_value_list.deserialize_aws_json_1_1(
                data["ParameterNameValues"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateParameterGroupRequest.parameter_name_values required"
        )
    return out
