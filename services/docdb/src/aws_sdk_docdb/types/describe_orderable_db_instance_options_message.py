"""Generated from Smithy shape ``com.amazonaws.docdb#DescribeOrderableDBInstanceOptionsMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.boolean_optional
    import aws_sdk_docdb.types.filter_list
    import aws_sdk_docdb.types.integer_optional
    import aws_sdk_docdb.types.string


class DescribeOrderableDBInstanceOptionsMessage(TypedDict):
    engine: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The name of the engine to retrieve instance options for.</p>"""
    engine_version: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The engine version filter value. Specify this parameter to show only the available offerings that match the specified engine version.</p>"""
    db_instance_class: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The instance class filter value. Specify this parameter to show only the available offerings that match the specified instance class.</p>"""
    license_model: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The license model filter value. Specify this parameter to show only the available offerings that match the specified license model.</p>"""
    vpc: NotRequired["aws_sdk_docdb.types.boolean_optional.BooleanOptional"]
    """<p>The virtual private cloud (VPC) filter value. Specify this parameter to show only the available VPC or non-VPC offerings.</p>"""
    filters: NotRequired["aws_sdk_docdb.types.filter_list.FilterList"]
    """<p>This parameter is not currently supported.</p>"""
    max_records: NotRequired["aws_sdk_docdb.types.integer_optional.IntegerOptional"]
    """<p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>"""
    marker: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeOrderableDBInstanceOptionsMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "engine" in value:
        pairs.append((f"{prefix}.Engine", str(value["engine"])))
    if "engine_version" in value:
        pairs.append((f"{prefix}.EngineVersion", str(value["engine_version"])))
    if "db_instance_class" in value:
        pairs.append((f"{prefix}.DBInstanceClass", str(value["db_instance_class"])))
    if "license_model" in value:
        pairs.append((f"{prefix}.LicenseModel", str(value["license_model"])))
    if "vpc" in value:
        pairs.append((f"{prefix}.Vpc", "true" if value["vpc"] else "false"))
    if "filters" in value:
        import aws_sdk_docdb.types.filter_list

        aws_sdk_docdb.types.filter_list.serialize_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeOrderableDBInstanceOptionsMessage:
    out: DescribeOrderableDBInstanceOptionsMessage = {}  # type: ignore[typeddict-item]
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_db_instance_class = el.find("DBInstanceClass")
    if child_db_instance_class is not None:
        out["db_instance_class"] = str(child_db_instance_class.text or "")
    child_license_model = el.find("LicenseModel")
    if child_license_model is not None:
        out["license_model"] = str(child_license_model.text or "")
    child_vpc = el.find("Vpc")
    if child_vpc is not None:
        out["vpc"] = (child_vpc.text or "").lower() == "true"
    child_filters = el.find("Filters")
    if child_filters is not None:
        import aws_sdk_docdb.types.filter_list

        out["filters"] = aws_sdk_docdb.types.filter_list.deserialize_query(
            child_filters
        )
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
