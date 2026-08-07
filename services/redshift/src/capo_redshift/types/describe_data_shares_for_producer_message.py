"""Generated from Smithy shape ``com.amazonaws.redshift#DescribeDataSharesForProducerMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.data_share_status_for_producer
    import capo_redshift.types.integer_optional
    import capo_redshift.types.string


class DescribeDataSharesForProducerMessage(TypedDict, closed=True):
    producer_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the producer namespace that returns in the list of datashares.</p>"""
    status: NotRequired[
        "capo_redshift.types.data_share_status_for_producer.DataShareStatusForProducer"
    ]
    """<p>An identifier giving the status of a datashare in the producer. If this field is specified, Amazon Redshift returns the list of datashares that have the specified status.</p>"""
    max_records: NotRequired["capo_redshift.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified <code>MaxRecords</code> value, a value is returned in a <code>marker</code> field of the response. You can retrieve the next set of records by retrying the command with the returned marker value. </p>"""
    marker: NotRequired["capo_redshift.types.string.String"]
    """<p>An optional parameter that specifies the starting point to return a set of response records. When the results of a <a>DescribeDataSharesForProducer</a> request exceed the value specified in <code>MaxRecords</code>, Amazon Web Services returns a value in the <code>Marker</code> field of the response. You can retrieve the next set of response records by providing the returned marker value in the <code>Marker</code> parameter and retrying the request. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDataSharesForProducerMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "producer_arn" in value:
        pairs.append((f"{key_prefix}ProducerArn", str(value["producer_arn"])))
    if "status" in value:
        import capo_redshift.types.data_share_status_for_producer

        capo_redshift.types.data_share_status_for_producer.serialize_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "max_records" in value:
        pairs.append((f"{key_prefix}MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeDataSharesForProducerMessage:
    out: DescribeDataSharesForProducerMessage = {}  # type: ignore[typeddict-item]
    child_producer_arn = el.find("ProducerArn")
    if child_producer_arn is not None:
        out["producer_arn"] = str(child_producer_arn.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import capo_redshift.types.data_share_status_for_producer

        out["status"] = (
            capo_redshift.types.data_share_status_for_producer.deserialize_query(
                child_status
            )
        )
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
