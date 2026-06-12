"""Generated from Smithy shape ``com.amazonaws.rds#DescribeOrderableDBInstanceOptionsMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.boolean_optional
    import aws_sdk_rds.types.filter_list
    import aws_sdk_rds.types.integer_optional
    import aws_sdk_rds.types.string


class DescribeOrderableDBInstanceOptionsMessage(TypedDict):
    engine: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The name of the database engine to describe DB instance options for.</p> <p>Valid Values:</p> <ul> <li> <p> <code>aurora-mysql</code> </p> </li> <li> <p> <code>aurora-postgresql</code> </p> </li> <li> <p> <code>custom-oracle-ee</code> </p> </li> <li> <p> <code>custom-oracle-ee-cdb</code> </p> </li> <li> <p> <code>custom-oracle-se2</code> </p> </li> <li> <p> <code>custom-oracle-se2-cdb</code> </p> </li> <li> <p> <code>db2-ae</code> </p> </li> <li> <p> <code>db2-se</code> </p> </li> <li> <p> <code>mariadb</code> </p> </li> <li> <p> <code>mysql</code> </p> </li> <li> <p> <code>oracle-ee</code> </p> </li> <li> <p> <code>oracle-ee-cdb</code> </p> </li> <li> <p> <code>oracle-se2</code> </p> </li> <li> <p> <code>oracle-se2-cdb</code> </p> </li> <li> <p> <code>postgres</code> </p> </li> <li> <p> <code>sqlserver-ee</code> </p> </li> <li> <p> <code>sqlserver-se</code> </p> </li> <li> <p> <code>sqlserver-ex</code> </p> </li> <li> <p> <code>sqlserver-web</code> </p> </li> </ul>"""
    engine_version: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>A filter to include only the available options for the specified engine version.</p>"""
    db_instance_class: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>A filter to include only the available options for the specified DB instance class.</p>"""
    license_model: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>A filter to include only the available options for the specified license model.</p> <p>RDS Custom supports only the BYOL licensing model.</p>"""
    availability_zone_group: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The Availability Zone group associated with a Local Zone. Specify this parameter to retrieve available options for the Local Zones in the group.</p> <p>Omit this parameter to show the available options in the specified Amazon Web Services Region.</p> <p>This setting doesn't apply to RDS Custom DB instances.</p>"""
    vpc: NotRequired["aws_sdk_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether to show only VPC or non-VPC offerings. RDS Custom supports only VPC offerings.</p> <p>RDS Custom supports only VPC offerings. If you describe non-VPC offerings for RDS Custom, the output shows VPC offerings.</p>"""
    filters: NotRequired["aws_sdk_rds.types.filter_list.FilterList"]
    """<p>This parameter isn't currently supported.</p>"""
    max_records: NotRequired["aws_sdk_rds.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that you can retrieve the remaining results.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 1000.</p>"""
    marker: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous DescribeOrderableDBInstanceOptions request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""


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
    if "availability_zone_group" in value:
        pairs.append(
            (f"{prefix}.AvailabilityZoneGroup", str(value["availability_zone_group"]))
        )
    if "vpc" in value:
        pairs.append((f"{prefix}.Vpc", "true" if value["vpc"] else "false"))
    if "filters" in value:
        import aws_sdk_rds.types.filter_list

        aws_sdk_rds.types.filter_list.serialize_query(
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
    child_availability_zone_group = el.find("AvailabilityZoneGroup")
    if child_availability_zone_group is not None:
        out["availability_zone_group"] = str(child_availability_zone_group.text or "")
    child_vpc = el.find("Vpc")
    if child_vpc is not None:
        out["vpc"] = (child_vpc.text or "").lower() == "true"
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
