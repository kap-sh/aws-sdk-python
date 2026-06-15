"""Generated from Smithy shape ``com.amazonaws.dax#UpdateParameterGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_dax.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dax.types.parameter_name_value_list
    import aws_sdk_dax.types.string


class UpdateParameterGroupRequest(TypedDict):
    parameter_group_name: "aws_sdk_dax.types.string.String"
    """<p>The name of the parameter group.</p>"""
    parameter_name_values: (
        "aws_sdk_dax.types.parameter_name_value_list.ParameterNameValueList"
    )
    r"""<p>An array of name-value pairs for the parameters in the group. Each element in the array represents a single parameter.</p> <note> <p> <code>record-ttl-millis</code> and <code>query-ttl-millis</code> are the only supported parameter names. For more details, see <a href=\"https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.cluster-management.html#DAX.cluster-management.custom-settings.ttl\">Configuring TTL Settings</a>.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateParameterGroupRequest) -> dict:
    out: dict = {}
    out["ParameterGroupName"] = value["parameter_group_name"]
    import aws_sdk_dax.types.parameter_name_value_list

    out["ParameterNameValues"] = (
        aws_sdk_dax.types.parameter_name_value_list.serialize_aws_json_1_1(
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
        import aws_sdk_dax.types.parameter_name_value_list

        out["parameter_name_values"] = (
            aws_sdk_dax.types.parameter_name_value_list.deserialize_aws_json_1_1(
                data["ParameterNameValues"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateParameterGroupRequest.parameter_name_values required"
        )
    return out
