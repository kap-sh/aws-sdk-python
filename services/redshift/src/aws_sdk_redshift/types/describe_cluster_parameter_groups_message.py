"""Generated from Smithy shape ``com.amazonaws.redshift#DescribeClusterParameterGroupsMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.integer_optional
    import aws_sdk_redshift.types.string
    import aws_sdk_redshift.types.tag_key_list
    import aws_sdk_redshift.types.tag_value_list


class DescribeClusterParameterGroupsMessage(TypedDict):
    parameter_group_name: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The name of a specific parameter group for which to return details. By default, details about all parameter groups and the default parameter group are returned.</p>"""
    max_records: NotRequired["aws_sdk_redshift.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p> <p>Default: <code>100</code> </p> <p>Constraints: minimum 20, maximum 100.</p>"""
    marker: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <a>DescribeClusterParameterGroups</a> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>"""
    tag_keys: NotRequired["aws_sdk_redshift.types.tag_key_list.TagKeyList"]
    """<p>A tag key or keys for which you want to return all matching cluster parameter groups that are associated with the specified key or keys. For example, suppose that you have parameter groups that are tagged with keys called <code>owner</code> and <code>environment</code>. If you specify both of these tag keys in the request, Amazon Redshift returns a response with the parameter groups that have either or both of these tag keys associated with them.</p>"""
    tag_values: NotRequired["aws_sdk_redshift.types.tag_value_list.TagValueList"]
    """<p>A tag value or values for which you want to return all matching cluster parameter groups that are associated with the specified tag value or values. For example, suppose that you have parameter groups that are tagged with values called <code>admin</code> and <code>test</code>. If you specify both of these tag values in the request, Amazon Redshift returns a response with the parameter groups that have either or both of these tag values associated with them.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeClusterParameterGroupsMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "parameter_group_name" in value:
        pairs.append(
            (f"{prefix}.ParameterGroupName", str(value["parameter_group_name"]))
        )
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "tag_keys" in value:
        import aws_sdk_redshift.types.tag_key_list

        aws_sdk_redshift.types.tag_key_list.serialize_query(
            value["tag_keys"], pairs, f"{prefix}.TagKeys"
        )
    if "tag_values" in value:
        import aws_sdk_redshift.types.tag_value_list

        aws_sdk_redshift.types.tag_value_list.serialize_query(
            value["tag_values"], pairs, f"{prefix}.TagValues"
        )


def deserialize_query(el: Element) -> DescribeClusterParameterGroupsMessage:
    out: DescribeClusterParameterGroupsMessage = {}  # type: ignore[typeddict-item]
    child_parameter_group_name = el.find("ParameterGroupName")
    if child_parameter_group_name is not None:
        out["parameter_group_name"] = str(child_parameter_group_name.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_tag_keys = el.find("TagKeys")
    if child_tag_keys is not None:
        import aws_sdk_redshift.types.tag_key_list

        out["tag_keys"] = aws_sdk_redshift.types.tag_key_list.deserialize_query(
            child_tag_keys
        )
    child_tag_values = el.find("TagValues")
    if child_tag_values is not None:
        import aws_sdk_redshift.types.tag_value_list

        out["tag_values"] = aws_sdk_redshift.types.tag_value_list.deserialize_query(
            child_tag_values
        )
    return out
