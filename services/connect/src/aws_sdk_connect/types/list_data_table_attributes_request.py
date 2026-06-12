"""Generated from Smithy shape ``com.amazonaws.connect#ListDataTableAttributesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.attribute_ids
    import aws_sdk_connect.types.data_table_id
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.max_result1000
    import aws_sdk_connect.types.next_token


class ListDataTableAttributesRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The unique identifier for the Amazon Connect instance.</p>"""
    data_table_id: "aws_sdk_connect.types.data_table_id.DataTableId"
    """<p>The unique identifier for the data table whose attributes should be listed.</p>"""
    attribute_ids: NotRequired["aws_sdk_connect.types.attribute_ids.AttributeIds"]
    """<p>Optional list of specific attribute IDs to retrieve. Used for CloudFormation to effectively describe attributes by ID. If NextToken is provided, this parameter is ignored.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""
    max_results: NotRequired["aws_sdk_connect.types.max_result1000.MaxResult1000"]
    """<p>The maximum number of data table attributes to return in one page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataTableAttributesRequest) -> dict:
    out: dict = {}
    if "attribute_ids" in value:
        import aws_sdk_connect.types.attribute_ids

        out["AttributeIds"] = aws_sdk_connect.types.attribute_ids.serialize_json(
            value["attribute_ids"]
        )
    return out


def deserialize_json(data: dict) -> ListDataTableAttributesRequest:
    out: ListDataTableAttributesRequest = {}  # type: ignore[typeddict-item]
    if "AttributeIds" in data:
        import aws_sdk_connect.types.attribute_ids

        out["attribute_ids"] = aws_sdk_connect.types.attribute_ids.deserialize_json(
            data["AttributeIds"]
        )
    return out
