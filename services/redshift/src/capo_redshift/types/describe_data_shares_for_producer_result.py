"""Generated from Smithy shape ``com.amazonaws.redshift#DescribeDataSharesForProducerResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.data_share_list
    import capo_redshift.types.string


class DescribeDataSharesForProducerResult(TypedDict, closed=True):
    data_shares: NotRequired["capo_redshift.types.data_share_list.DataShareList"]
    """<p>Shows the results of datashares available for producers.</p>"""
    marker: NotRequired["capo_redshift.types.string.String"]
    """<p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <a>DescribeDataSharesForProducer</a> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDataSharesForProducerResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "data_shares" in value:
        import capo_redshift.types.data_share_list

        capo_redshift.types.data_share_list.serialize_query(
            value["data_shares"], pairs, f"{prefix}.DataShares"
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeDataSharesForProducerResult:
    out: DescribeDataSharesForProducerResult = {}  # type: ignore[typeddict-item]
    child_data_shares = el.find("DataShares")
    if child_data_shares is not None:
        import capo_redshift.types.data_share_list

        out["data_shares"] = capo_redshift.types.data_share_list.deserialize_query(
            child_data_shares
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
