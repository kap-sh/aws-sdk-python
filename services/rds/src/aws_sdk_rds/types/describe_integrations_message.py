"""Generated from Smithy shape ``com.amazonaws.rds#DescribeIntegrationsMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.filter_list
    import aws_sdk_rds.types.integer_optional
    import aws_sdk_rds.types.integration_identifier
    import aws_sdk_rds.types.marker


class DescribeIntegrationsMessage(TypedDict):
    integration_identifier: NotRequired[
        "aws_sdk_rds.types.integration_identifier.IntegrationIdentifier"
    ]
    """<p>The unique identifier of the integration.</p>"""
    filters: NotRequired["aws_sdk_rds.types.filter_list.FilterList"]
    """<p>A filter that specifies one or more resources to return.</p>"""
    max_records: NotRequired["aws_sdk_rds.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that you can retrieve the remaining results.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>"""
    marker: NotRequired["aws_sdk_rds.types.marker.Marker"]
    """<p>An optional pagination token provided by a previous <code>DescribeIntegrations</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeIntegrationsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "integration_identifier" in value:
        pairs.append(
            (f"{prefix}.IntegrationIdentifier", str(value["integration_identifier"]))
        )
    if "filters" in value:
        import aws_sdk_rds.types.filter_list

        aws_sdk_rds.types.filter_list.serialize_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeIntegrationsMessage:
    out: DescribeIntegrationsMessage = {}  # type: ignore[typeddict-item]
    child_integration_identifier = el.find("IntegrationIdentifier")
    if child_integration_identifier is not None:
        out["integration_identifier"] = str(child_integration_identifier.text or "")
    child_filters = el.find("Filters")
    if child_filters is not None:
        import aws_sdk_rds.types.filter_list

        out["filters"] = aws_sdk_rds.types.filter_list.deserialize_query(child_filters)
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
