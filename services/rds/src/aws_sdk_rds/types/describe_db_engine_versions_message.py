"""Generated from Smithy shape ``com.amazonaws.rds#DescribeDBEngineVersionsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.boolean
    import aws_sdk_rds.types.boolean_optional
    import aws_sdk_rds.types.filter_list
    import aws_sdk_rds.types.integer_optional
    import aws_sdk_rds.types.string


class DescribeDBEngineVersionsMessage(TypedDict, closed=True):
    engine: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The database engine to return version details for.</p> <p>Valid Values:</p> <ul> <li> <p> <code>aurora-mysql</code> </p> </li> <li> <p> <code>aurora-postgresql</code> </p> </li> <li> <p> <code>custom-oracle-ee</code> </p> </li> <li> <p> <code>custom-oracle-ee-cdb</code> </p> </li> <li> <p> <code>custom-oracle-se2</code> </p> </li> <li> <p> <code>custom-oracle-se2-cdb</code> </p> </li> <li> <p> <code>db2-ae</code> </p> </li> <li> <p> <code>db2-se</code> </p> </li> <li> <p> <code>mariadb</code> </p> </li> <li> <p> <code>mysql</code> </p> </li> <li> <p> <code>oracle-ee</code> </p> </li> <li> <p> <code>oracle-ee-cdb</code> </p> </li> <li> <p> <code>oracle-se2</code> </p> </li> <li> <p> <code>oracle-se2-cdb</code> </p> </li> <li> <p> <code>postgres</code> </p> </li> <li> <p> <code>sqlserver-ee</code> </p> </li> <li> <p> <code>sqlserver-se</code> </p> </li> <li> <p> <code>sqlserver-ex</code> </p> </li> <li> <p> <code>sqlserver-web</code> </p> </li> </ul>"""
    engine_version: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>A specific database engine version to return details for.</p> <p>Example: <code>5.1.49</code> </p>"""
    db_parameter_group_family: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The name of a specific DB parameter group family to return details for.</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match an existing DB parameter group family.</p> </li> </ul>"""
    filters: NotRequired["aws_sdk_rds.types.filter_list.FilterList"]
    """<p>A filter that specifies one or more DB engine versions to describe.</p> <p>Supported filters:</p> <ul> <li> <p> <code>db-parameter-group-family</code> - Accepts parameter groups family names. The results list only includes information about the DB engine versions for these parameter group families.</p> </li> <li> <p> <code>engine</code> - Accepts engine names. The results list only includes information about the DB engine versions for these engines.</p> </li> <li> <p> <code>engine-mode</code> - Accepts DB engine modes. The results list only includes information about the DB engine versions for these engine modes. Valid DB engine modes are the following:</p> <ul> <li> <p> <code>global</code> </p> </li> <li> <p> <code>multimaster</code> </p> </li> <li> <p> <code>parallelquery</code> </p> </li> <li> <p> <code>provisioned</code> </p> </li> <li> <p> <code>serverless</code> </p> </li> </ul> </li> <li> <p> <code>engine-version</code> - Accepts engine versions. The results list only includes information about the DB engine versions for these engine versions.</p> </li> <li> <p> <code>status</code> - Accepts engine version statuses. The results list only includes information about the DB engine versions for these statuses. Valid statuses are the following:</p> <ul> <li> <p> <code>available</code> </p> </li> <li> <p> <code>deprecated</code> </p> </li> </ul> </li> </ul>"""
    max_records: NotRequired["aws_sdk_rds.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more than the <code>MaxRecords</code> value is available, a pagination token called a marker is included in the response so you can retrieve the remaining results.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>"""
    marker: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    default_only: NotRequired["aws_sdk_rds.types.boolean.Boolean"]
    """<p>Specifies whether to return only the default version of the specified engine or the engine and major version combination.</p>"""
    list_supported_character_sets: NotRequired[
        "aws_sdk_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to list the supported character sets for each engine version.</p> <p>If this parameter is enabled and the requested engine supports the <code>CharacterSetName</code> parameter for <code>CreateDBInstance</code>, the response includes a list of supported character sets for each engine version.</p> <p>For RDS Custom, the default is not to list supported character sets. If you enable this parameter, RDS Custom returns no results.</p>"""
    list_supported_timezones: NotRequired[
        "aws_sdk_rds.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether to list the supported time zones for each engine version.</p> <p>If this parameter is enabled and the requested engine supports the <code>TimeZone</code> parameter for <code>CreateDBInstance</code>, the response includes a list of supported time zones for each engine version.</p> <p>For RDS Custom, the default is not to list supported time zones. If you enable this parameter, RDS Custom returns no results.</p>"""
    include_all: NotRequired["aws_sdk_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether to also list the engine versions that aren't available. The default is to list only available engine versions.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDBEngineVersionsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "engine" in value:
        pairs.append((f"{prefix}.Engine", str(value["engine"])))
    if "engine_version" in value:
        pairs.append((f"{prefix}.EngineVersion", str(value["engine_version"])))
    if "db_parameter_group_family" in value:
        pairs.append(
            (
                f"{prefix}.DBParameterGroupFamily",
                str(value["db_parameter_group_family"]),
            )
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
    if "default_only" in value:
        pairs.append(
            (f"{prefix}.DefaultOnly", "true" if value["default_only"] else "false")
        )
    if "list_supported_character_sets" in value:
        pairs.append(
            (
                f"{prefix}.ListSupportedCharacterSets",
                "true" if value["list_supported_character_sets"] else "false",
            )
        )
    if "list_supported_timezones" in value:
        pairs.append(
            (
                f"{prefix}.ListSupportedTimezones",
                "true" if value["list_supported_timezones"] else "false",
            )
        )
    if "include_all" in value:
        pairs.append(
            (f"{prefix}.IncludeAll", "true" if value["include_all"] else "false")
        )


def deserialize_query(el: Element) -> DescribeDBEngineVersionsMessage:
    out: DescribeDBEngineVersionsMessage = {}  # type: ignore[typeddict-item]
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_engine_version = el.find("EngineVersion")
    if child_engine_version is not None:
        out["engine_version"] = str(child_engine_version.text or "")
    child_db_parameter_group_family = el.find("DBParameterGroupFamily")
    if child_db_parameter_group_family is not None:
        out["db_parameter_group_family"] = str(
            child_db_parameter_group_family.text or ""
        )
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
    child_default_only = el.find("DefaultOnly")
    if child_default_only is not None:
        out["default_only"] = (child_default_only.text or "").lower() == "true"
    child_list_supported_character_sets = el.find("ListSupportedCharacterSets")
    if child_list_supported_character_sets is not None:
        out["list_supported_character_sets"] = (
            child_list_supported_character_sets.text or ""
        ).lower() == "true"
    child_list_supported_timezones = el.find("ListSupportedTimezones")
    if child_list_supported_timezones is not None:
        out["list_supported_timezones"] = (
            child_list_supported_timezones.text or ""
        ).lower() == "true"
    child_include_all = el.find("IncludeAll")
    if child_include_all is not None:
        out["include_all"] = (child_include_all.text or "").lower() == "true"
    return out
