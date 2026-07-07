"""Generated from Smithy shape ``com.amazonaws.redshift#DataShareAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.boolean_optional
    import aws_sdk_redshift.types.data_share_status
    import aws_sdk_redshift.types.string
    import aws_sdk_redshift.types.t_stamp


class DataShareAssociation(TypedDict, closed=True):
    consumer_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The name of the consumer accounts that have an association with a producer datashare.</p>"""
    status: NotRequired["aws_sdk_redshift.types.data_share_status.DataShareStatus"]
    """<p>The status of the datashare that is associated.</p>"""
    consumer_region: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The Amazon Web Services Region of the consumer accounts that have an association with a producer datashare.</p>"""
    created_date: NotRequired["aws_sdk_redshift.types.t_stamp.TStamp"]
    """<p>The creation date of the datashare that is associated.</p>"""
    status_change_date: NotRequired["aws_sdk_redshift.types.t_stamp.TStamp"]
    """<p>The status change data of the datashare that is associated.</p>"""
    producer_allowed_writes: NotRequired[
        "aws_sdk_redshift.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether write operations were allowed during data share authorization.</p>"""
    consumer_accepted_writes: NotRequired[
        "aws_sdk_redshift.types.boolean_optional.BooleanOptional"
    ]
    """<p>Specifies whether write operations were allowed during data share association.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DataShareAssociation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "consumer_identifier" in value:
        pairs.append(
            (f"{prefix}.ConsumerIdentifier", str(value["consumer_identifier"]))
        )
    if "status" in value:
        import aws_sdk_redshift.types.data_share_status

        aws_sdk_redshift.types.data_share_status.serialize_query(
            value["status"], pairs, f"{prefix}.Status"
        )
    if "consumer_region" in value:
        pairs.append((f"{prefix}.ConsumerRegion", str(value["consumer_region"])))
    if "created_date" in value:
        import aws_sdk_redshift.types.t_stamp

        aws_sdk_redshift.types.t_stamp.serialize_query(
            value["created_date"], pairs, f"{prefix}.CreatedDate"
        )
    if "status_change_date" in value:
        import aws_sdk_redshift.types.t_stamp

        aws_sdk_redshift.types.t_stamp.serialize_query(
            value["status_change_date"], pairs, f"{prefix}.StatusChangeDate"
        )
    if "producer_allowed_writes" in value:
        pairs.append(
            (
                f"{prefix}.ProducerAllowedWrites",
                "true" if value["producer_allowed_writes"] else "false",
            )
        )
    if "consumer_accepted_writes" in value:
        pairs.append(
            (
                f"{prefix}.ConsumerAcceptedWrites",
                "true" if value["consumer_accepted_writes"] else "false",
            )
        )


def deserialize_query(el: Element) -> DataShareAssociation:
    out: DataShareAssociation = {}  # type: ignore[typeddict-item]
    child_consumer_identifier = el.find("ConsumerIdentifier")
    if child_consumer_identifier is not None:
        out["consumer_identifier"] = str(child_consumer_identifier.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_redshift.types.data_share_status

        out["status"] = aws_sdk_redshift.types.data_share_status.deserialize_query(
            child_status
        )
    child_consumer_region = el.find("ConsumerRegion")
    if child_consumer_region is not None:
        out["consumer_region"] = str(child_consumer_region.text or "")
    child_created_date = el.find("CreatedDate")
    if child_created_date is not None:
        import aws_sdk_redshift.types.t_stamp

        out["created_date"] = aws_sdk_redshift.types.t_stamp.deserialize_query(
            child_created_date
        )
    child_status_change_date = el.find("StatusChangeDate")
    if child_status_change_date is not None:
        import aws_sdk_redshift.types.t_stamp

        out["status_change_date"] = aws_sdk_redshift.types.t_stamp.deserialize_query(
            child_status_change_date
        )
    child_producer_allowed_writes = el.find("ProducerAllowedWrites")
    if child_producer_allowed_writes is not None:
        out["producer_allowed_writes"] = (
            child_producer_allowed_writes.text or ""
        ).lower() == "true"
    child_consumer_accepted_writes = el.find("ConsumerAcceptedWrites")
    if child_consumer_accepted_writes is not None:
        out["consumer_accepted_writes"] = (
            child_consumer_accepted_writes.text or ""
        ).lower() == "true"
    return out
