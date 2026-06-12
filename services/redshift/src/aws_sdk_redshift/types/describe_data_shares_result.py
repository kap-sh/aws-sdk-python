"""Generated from Smithy shape ``com.amazonaws.redshift#DescribeDataSharesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.data_share_list
    import aws_sdk_redshift.types.string


class DescribeDataSharesResult(TypedDict):
    data_shares: NotRequired["aws_sdk_redshift.types.data_share_list.DataShareList"]
    """<p>The results returned from describing datashares.</p>"""
    marker: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <a>DescribeDataShares</a> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDataSharesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "data_shares" in value:
        import aws_sdk_redshift.types.data_share_list

        aws_sdk_redshift.types.data_share_list.serialize_query(
            value["data_shares"], pairs, f"{prefix}.DataShares"
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeDataSharesResult:
    out: DescribeDataSharesResult = {}  # type: ignore[typeddict-item]
    child_data_shares = el.find("DataShares")
    if child_data_shares is not None:
        import aws_sdk_redshift.types.data_share_list

        out["data_shares"] = aws_sdk_redshift.types.data_share_list.deserialize_query(
            child_data_shares
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
