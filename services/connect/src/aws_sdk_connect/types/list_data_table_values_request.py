"""Generated from Smithy shape ``com.amazonaws.connect#ListDataTableValuesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.data_table_id
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.max_result1000
    import aws_sdk_connect.types.next_token
    import aws_sdk_connect.types.primary_attribute_value_filters
    import aws_sdk_connect.types.record_ids


class ListDataTableValuesRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The unique identifier for the Amazon Connect instance.</p>"""
    data_table_id: "aws_sdk_connect.types.data_table_id.DataTableId"
    """<p>The unique identifier for the data table whose values should be listed.</p>"""
    record_ids: NotRequired["aws_sdk_connect.types.record_ids.RecordIds"]
    """<p>Optional list of specific record IDs to retrieve values for.</p>"""
    primary_attribute_values: NotRequired[
        "aws_sdk_connect.types.primary_attribute_value_filters.PrimaryAttributeValueFilters"
    ]
    """<p>Optional filter to retrieve values for records matching specific primary attribute criteria.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""
    max_results: NotRequired["aws_sdk_connect.types.max_result1000.MaxResult1000"]
    """<p>The maximum number of data table values to return in one page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataTableValuesRequest) -> dict:
    out: dict = {}
    if "record_ids" in value:
        import aws_sdk_connect.types.record_ids

        out["RecordIds"] = aws_sdk_connect.types.record_ids.serialize_json(
            value["record_ids"]
        )
    if "primary_attribute_values" in value:
        import aws_sdk_connect.types.primary_attribute_value_filters

        out["PrimaryAttributeValues"] = (
            aws_sdk_connect.types.primary_attribute_value_filters.serialize_json(
                value["primary_attribute_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListDataTableValuesRequest:
    out: ListDataTableValuesRequest = {}  # type: ignore[typeddict-item]
    if "RecordIds" in data:
        import aws_sdk_connect.types.record_ids

        out["record_ids"] = aws_sdk_connect.types.record_ids.deserialize_json(
            data["RecordIds"]
        )
    if "PrimaryAttributeValues" in data:
        import aws_sdk_connect.types.primary_attribute_value_filters

        out["primary_attribute_values"] = (
            aws_sdk_connect.types.primary_attribute_value_filters.deserialize_json(
                data["PrimaryAttributeValues"]
            )
        )
    return out
