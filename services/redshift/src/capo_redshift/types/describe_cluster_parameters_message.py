"""Generated from Smithy shape ``com.amazonaws.redshift#DescribeClusterParametersMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.integer_optional
    import capo_redshift.types.string


class DescribeClusterParametersMessage(TypedDict, closed=True):
    parameter_group_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of a cluster parameter group for which to return details.</p>"""
    source: NotRequired["capo_redshift.types.string.String"]
    """<p>The parameter types to return. Specify <code>user</code> to show parameters that are different form the default. Similarly, specify <code>engine-default</code> to show parameters that are the same as the default parameter group. </p> <p>Default: All parameter types returned.</p> <p>Valid Values: <code>user</code> | <code>engine-default</code> </p>"""
    max_records: NotRequired["capo_redshift.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p> <p>Default: <code>100</code> </p> <p>Constraints: minimum 20, maximum 100.</p>"""
    marker: NotRequired["capo_redshift.types.string.String"]
    """<p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <a>DescribeClusterParameters</a> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeClusterParametersMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "parameter_group_name" in value:
        pairs.append(
            (f"{key_prefix}ParameterGroupName", str(value["parameter_group_name"]))
        )
    if "source" in value:
        pairs.append((f"{key_prefix}Source", str(value["source"])))
    if "max_records" in value:
        pairs.append((f"{key_prefix}MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeClusterParametersMessage:
    out: DescribeClusterParametersMessage = {}  # type: ignore[typeddict-item]
    child_parameter_group_name = el.find("ParameterGroupName")
    if child_parameter_group_name is not None:
        out["parameter_group_name"] = str(child_parameter_group_name.text or "")
    child_source = el.find("Source")
    if child_source is not None:
        out["source"] = str(child_source.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
