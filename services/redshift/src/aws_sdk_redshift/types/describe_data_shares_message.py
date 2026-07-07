"""Generated from Smithy shape ``com.amazonaws.redshift#DescribeDataSharesMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.integer_optional
    import aws_sdk_redshift.types.string


class DescribeDataSharesMessage(TypedDict, closed=True):
    data_share_arn: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The Amazon resource name (ARN) of the datashare to describe details of.</p>"""
    max_records: NotRequired["aws_sdk_redshift.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p>"""
    marker: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <a>DescribeDataShares</a> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDataSharesMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "data_share_arn" in value:
        pairs.append((f"{prefix}.DataShareArn", str(value["data_share_arn"])))
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeDataSharesMessage:
    out: DescribeDataSharesMessage = {}  # type: ignore[typeddict-item]
    child_data_share_arn = el.find("DataShareArn")
    if child_data_share_arn is not None:
        out["data_share_arn"] = str(child_data_share_arn.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
