"""Generated from Smithy shape ``com.amazonaws.glue#ListIntegrationResourcePropertiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.integration_integer
    import aws_sdk_glue.types.integration_resource_property_filter_list
    import aws_sdk_glue.types.string1024


class ListIntegrationResourcePropertiesRequest(TypedDict, closed=True):
    marker: NotRequired["aws_sdk_glue.types.string1024.String1024"]
    """<p>This is the pagination token for next page, initial value is <code>null</code>.</p>"""
    filters: NotRequired[
        "aws_sdk_glue.types.integration_resource_property_filter_list.IntegrationResourcePropertyFilterList"
    ]
    """<p>A list of filters, supported filter Key is <code>SourceArn</code> and <code>TargetArn</code>.</p>"""
    max_records: NotRequired[
        "aws_sdk_glue.types.integration_integer.IntegrationInteger"
    ]
    """<p>This is total number of items to be evaluated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListIntegrationResourcePropertiesRequest) -> dict:
    out: dict = {}
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "filters" in value:
        import aws_sdk_glue.types.integration_resource_property_filter_list

        out["Filters"] = (
            aws_sdk_glue.types.integration_resource_property_filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "max_records" in value:
        out["MaxRecords"] = value["max_records"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListIntegrationResourcePropertiesRequest:
    out: ListIntegrationResourcePropertiesRequest = {}  # type: ignore[typeddict-item]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "Filters" in data:
        import aws_sdk_glue.types.integration_resource_property_filter_list

        out["filters"] = (
            aws_sdk_glue.types.integration_resource_property_filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if "MaxRecords" in data:
        out["max_records"] = data["MaxRecords"]
    return out
