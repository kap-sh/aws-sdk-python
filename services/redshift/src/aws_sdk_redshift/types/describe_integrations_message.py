"""Generated from Smithy shape ``com.amazonaws.redshift#DescribeIntegrationsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.describe_integrations_filter_list
    import aws_sdk_redshift.types.integer_optional
    import aws_sdk_redshift.types.integration_arn
    import aws_sdk_redshift.types.string


class DescribeIntegrationsMessage(TypedDict, closed=True):
    integration_arn: NotRequired[
        "aws_sdk_redshift.types.integration_arn.IntegrationArn"
    ]
    """<p>The unique identifier of the integration.</p>"""
    max_records: NotRequired["aws_sdk_redshift.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p> <p>Default: <code>100</code> </p> <p>Constraints: minimum 20, maximum 100.</p>"""
    marker: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>An optional pagination token provided by a previous <code>DescribeIntegrations</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    filters: NotRequired[
        "aws_sdk_redshift.types.describe_integrations_filter_list.DescribeIntegrationsFilterList"
    ]
    """<p>A filter that specifies one or more resources to return.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeIntegrationsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "integration_arn" in value:
        pairs.append((f"{prefix}.IntegrationArn", str(value["integration_arn"])))
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "filters" in value:
        import aws_sdk_redshift.types.describe_integrations_filter_list

        aws_sdk_redshift.types.describe_integrations_filter_list.serialize_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )


def deserialize_query(el: Element) -> DescribeIntegrationsMessage:
    out: DescribeIntegrationsMessage = {}  # type: ignore[typeddict-item]
    child_integration_arn = el.find("IntegrationArn")
    if child_integration_arn is not None:
        out["integration_arn"] = str(child_integration_arn.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_filters = el.find("Filters")
    if child_filters is not None:
        import aws_sdk_redshift.types.describe_integrations_filter_list

        out["filters"] = (
            aws_sdk_redshift.types.describe_integrations_filter_list.deserialize_query(
                child_filters
            )
        )
    return out
