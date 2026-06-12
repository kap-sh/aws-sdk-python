"""Generated from Smithy shape ``com.amazonaws.redshift#DescribeDefaultClusterParametersMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.integer_optional
    import aws_sdk_redshift.types.string


class DescribeDefaultClusterParametersMessage(TypedDict):
    parameter_group_family: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The name of the cluster parameter group family.</p>"""
    max_records: NotRequired["aws_sdk_redshift.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p> <p>Default: <code>100</code> </p> <p>Constraints: minimum 20, maximum 100.</p>"""
    marker: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <a>DescribeDefaultClusterParameters</a> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDefaultClusterParametersMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "parameter_group_family" in value:
        pairs.append(
            (f"{prefix}.ParameterGroupFamily", str(value["parameter_group_family"]))
        )
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeDefaultClusterParametersMessage:
    out: DescribeDefaultClusterParametersMessage = {}  # type: ignore[typeddict-item]
    child_parameter_group_family = el.find("ParameterGroupFamily")
    if child_parameter_group_family is not None:
        out["parameter_group_family"] = str(child_parameter_group_family.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
