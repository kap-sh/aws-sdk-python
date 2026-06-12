"""Generated from Smithy shape ``com.amazonaws.connect#EvaluateDataTableValuesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.data_table_id
    import aws_sdk_connect.types.data_table_value_evaluation_set_list
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.max_result100
    import aws_sdk_connect.types.next_token
    import aws_sdk_connect.types.time_zone


class EvaluateDataTableValuesRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The unique identifier for the Amazon Connect instance.</p>"""
    data_table_id: "aws_sdk_connect.types.data_table_id.DataTableId"
    """<p>The unique identifier for the data table. Must also accept the table ARN with or without a version alias.</p>"""
    values: "aws_sdk_connect.types.data_table_value_evaluation_set_list.DataTableValueEvaluationSetList"
    """<p>A list of value evaluation sets specifying which primary values and attributes to evaluate.</p>"""
    time_zone: NotRequired["aws_sdk_connect.types.time_zone.TimeZone"]
    """<p>Optional IANA timezone identifier to use when resolving time based dynamic values. Defaults to the data table time zone if not provided.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""
    max_results: NotRequired["aws_sdk_connect.types.max_result100.MaxResult100"]
    """<p>The maximum number of data table values to return in one page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluateDataTableValuesRequest) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.data_table_value_evaluation_set_list

    out["Values"] = (
        aws_sdk_connect.types.data_table_value_evaluation_set_list.serialize_json(
            value["values"]
        )
    )
    if "time_zone" in value:
        out["TimeZone"] = value["time_zone"]
    return out


def deserialize_json(data: dict) -> EvaluateDataTableValuesRequest:
    out: EvaluateDataTableValuesRequest = {}  # type: ignore[typeddict-item]
    if "Values" in data:
        import aws_sdk_connect.types.data_table_value_evaluation_set_list

        out["values"] = (
            aws_sdk_connect.types.data_table_value_evaluation_set_list.deserialize_json(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("EvaluateDataTableValuesRequest.values required")
    if "TimeZone" in data:
        out["time_zone"] = data["TimeZone"]
    return out
