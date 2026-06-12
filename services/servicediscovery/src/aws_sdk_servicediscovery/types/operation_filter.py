"""Generated from Smithy shape ``com.amazonaws.servicediscovery#OperationFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.filter_condition
    import aws_sdk_servicediscovery.types.filter_values
    import aws_sdk_servicediscovery.types.operation_filter_name


class OperationFilter(TypedDict):
    name: "aws_sdk_servicediscovery.types.operation_filter_name.OperationFilterName"
    """<p>Specify the operations that you want to get:</p> <ul> <li> <p> <b>NAMESPACE_ID</b>: Gets operations related to specified namespaces.</p> </li> <li> <p> <b>SERVICE_ID</b>: Gets operations related to specified services.</p> </li> <li> <p> <b>STATUS</b>: Gets operations based on the status of the operations: <code>SUBMITTED</code>, <code>PENDING</code>, <code>SUCCEED</code>, or <code>FAIL</code>.</p> </li> <li> <p> <b>TYPE</b>: Gets specified types of operation.</p> </li> <li> <p> <b>UPDATE_DATE</b>: Gets operations that changed status during a specified date/time range. </p> </li> </ul>"""
    values: "aws_sdk_servicediscovery.types.filter_values.FilterValues"
    """<p>Specify values that are applicable to the value that you specify for <code>Name</code>: </p> <ul> <li> <p> <b>NAMESPACE_ID</b>: Specify one namespace ID.</p> </li> <li> <p> <b>SERVICE_ID</b>: Specify one service ID.</p> </li> <li> <p> <b>STATUS</b>: Specify one or more statuses: <code>SUBMITTED</code>, <code>PENDING</code>, <code>SUCCEED</code>, or <code>FAIL</code>.</p> </li> <li> <p> <b>TYPE</b>: Specify one or more of the following types: <code>CREATE_NAMESPACE</code>, <code>DELETE_NAMESPACE</code>, <code>UPDATE_SERVICE</code>, <code>REGISTER_INSTANCE</code>, or <code>DEREGISTER_INSTANCE</code>.</p> </li> <li> <p> <b>UPDATE_DATE</b>: Specify a start date and an end date in Unix date/time format and Coordinated Universal Time (UTC). The start date must be the first value.</p> </li> </ul>"""
    condition: NotRequired[
        "aws_sdk_servicediscovery.types.filter_condition.FilterCondition"
    ]
    """<p>The operator that you want to use to determine whether an operation matches the specified value. Valid values for condition include:</p> <ul> <li> <p> <code>EQ</code>: When you specify <code>EQ</code> for the condition, you can specify only one value. <code>EQ</code> is supported for <code>NAMESPACE_ID</code>, <code>SERVICE_ID</code>, <code>STATUS</code>, and <code>TYPE</code>. <code>EQ</code> is the default condition and can be omitted.</p> </li> <li> <p> <code>IN</code>: When you specify <code>IN</code> for the condition, you can specify a list of one or more values. <code>IN</code> is supported for <code>STATUS</code> and <code>TYPE</code>. An operation must match one of the specified values to be returned in the response.</p> </li> <li> <p> <code>BETWEEN</code>: Specify a start date and an end date in Unix date/time format and Coordinated Universal Time (UTC). The start date must be the first value. <code>BETWEEN</code> is supported for <code>UPDATE_DATE</code>. </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperationFilter) -> dict:
    out: dict = {}
    import aws_sdk_servicediscovery.types.operation_filter_name

    out["Name"] = (
        aws_sdk_servicediscovery.types.operation_filter_name.serialize_aws_json_1_1(
            value["name"]
        )
    )
    import aws_sdk_servicediscovery.types.filter_values

    out["Values"] = aws_sdk_servicediscovery.types.filter_values.serialize_aws_json_1_1(
        value["values"]
    )
    if "condition" in value:
        import aws_sdk_servicediscovery.types.filter_condition

        out["Condition"] = (
            aws_sdk_servicediscovery.types.filter_condition.serialize_aws_json_1_1(
                value["condition"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OperationFilter:
    out: OperationFilter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import aws_sdk_servicediscovery.types.operation_filter_name

        out["name"] = (
            aws_sdk_servicediscovery.types.operation_filter_name.deserialize_aws_json_1_1(
                data["Name"]
            )
        )
    else:
        raise DeserializationError("OperationFilter.name required")
    if "Values" in data:
        import aws_sdk_servicediscovery.types.filter_values

        out["values"] = (
            aws_sdk_servicediscovery.types.filter_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("OperationFilter.values required")
    if "Condition" in data:
        import aws_sdk_servicediscovery.types.filter_condition

        out["condition"] = (
            aws_sdk_servicediscovery.types.filter_condition.deserialize_aws_json_1_1(
                data["Condition"]
            )
        )
    return out
