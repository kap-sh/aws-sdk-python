"""Generated from Smithy shape ``com.amazonaws.neptune#DescribeDBEngineVersionsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.boolean
    import aws_sdk_neptune.types.boolean_optional
    import aws_sdk_neptune.types.filter_list
    import aws_sdk_neptune.types.integer_optional
    import aws_sdk_neptune.types.string


class DescribeDBEngineVersionsMessage(TypedDict, closed=True):
    engine: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>The database engine to return.</p>"""
    engine_version: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>The database engine version to return.</p> <p>Example: <code>5.1.49</code> </p>"""
    db_parameter_group_family: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p>The name of a specific DB parameter group family to return details for.</p> <p>Constraints:</p> <ul> <li> <p>If supplied, must match an existing DBParameterGroupFamily.</p> </li> </ul>"""
    filters: NotRequired["aws_sdk_neptune.types.filter_list.FilterList"]
    """<p>Not currently supported.</p>"""
    max_records: NotRequired["aws_sdk_neptune.types.integer_optional.IntegerOptional"]
    """<p> The maximum number of records to include in the response. If more than the <code>MaxRecords</code> value is available, a pagination token called a marker is included in the response so that the following results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>"""
    marker: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    default_only: NotRequired["aws_sdk_neptune.types.boolean.Boolean"]
    """<p>Indicates that only the default version of the specified engine or engine and major version combination is returned.</p>"""
    list_supported_character_sets: NotRequired[
        "aws_sdk_neptune.types.boolean_optional.BooleanOptional"
    ]
    """<p>If this parameter is specified and the requested engine supports the <code>CharacterSetName</code> parameter for <code>CreateDBInstance</code>, the response includes a list of supported character sets for each engine version.</p>"""
    list_supported_timezones: NotRequired[
        "aws_sdk_neptune.types.boolean_optional.BooleanOptional"
    ]
    """<p>If this parameter is specified and the requested engine supports the <code>TimeZone</code> parameter for <code>CreateDBInstance</code>, the response includes a list of supported time zones for each engine version.</p>"""


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
        import aws_sdk_neptune.types.filter_list

        aws_sdk_neptune.types.filter_list.serialize_query(
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
        import aws_sdk_neptune.types.filter_list

        out["filters"] = aws_sdk_neptune.types.filter_list.deserialize_query(
            child_filters
        )
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
    return out
