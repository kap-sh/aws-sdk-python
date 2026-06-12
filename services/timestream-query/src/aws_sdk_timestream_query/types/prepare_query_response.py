"""Generated from Smithy shape ``com.amazonaws.timestreamquery#PrepareQueryResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_timestream_query.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_query.types.parameter_mapping_list
    import aws_sdk_timestream_query.types.query_string
    import aws_sdk_timestream_query.types.select_column_list


class PrepareQueryResponse(TypedDict):
    query_string: "aws_sdk_timestream_query.types.query_string.QueryString"
    """<p>The query string that you want prepare.</p>"""
    columns: "aws_sdk_timestream_query.types.select_column_list.SelectColumnList"
    """<p>A list of SELECT clause columns of the submitted query string. </p>"""
    parameters: (
        "aws_sdk_timestream_query.types.parameter_mapping_list.ParameterMappingList"
    )
    """<p>A list of parameters used in the submitted query string. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PrepareQueryResponse) -> dict:
    out: dict = {}
    out["QueryString"] = value["query_string"]
    import aws_sdk_timestream_query.types.select_column_list

    out["Columns"] = (
        aws_sdk_timestream_query.types.select_column_list.serialize_aws_json_1_0(
            value["columns"]
        )
    )
    import aws_sdk_timestream_query.types.parameter_mapping_list

    out["Parameters"] = (
        aws_sdk_timestream_query.types.parameter_mapping_list.serialize_aws_json_1_0(
            value["parameters"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> PrepareQueryResponse:
    out: PrepareQueryResponse = {}  # type: ignore[typeddict-item]
    if "QueryString" in data:
        out["query_string"] = data["QueryString"]
    else:
        raise DeserializationError("PrepareQueryResponse.query_string required")
    if "Columns" in data:
        import aws_sdk_timestream_query.types.select_column_list

        out["columns"] = (
            aws_sdk_timestream_query.types.select_column_list.deserialize_aws_json_1_0(
                data["Columns"]
            )
        )
    else:
        raise DeserializationError("PrepareQueryResponse.columns required")
    if "Parameters" in data:
        import aws_sdk_timestream_query.types.parameter_mapping_list

        out["parameters"] = (
            aws_sdk_timestream_query.types.parameter_mapping_list.deserialize_aws_json_1_0(
                data["Parameters"]
            )
        )
    else:
        raise DeserializationError("PrepareQueryResponse.parameters required")
    return out
