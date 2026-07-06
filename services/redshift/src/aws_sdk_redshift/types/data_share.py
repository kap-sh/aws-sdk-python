"""Generated from Smithy shape ``com.amazonaws.redshift#DataShare``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.boolean
    import aws_sdk_redshift.types.data_share_association_list
    import aws_sdk_redshift.types.data_share_type
    import aws_sdk_redshift.types.string


class DataShare(TypedDict, closed=True):
    data_share_arn: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the datashare that the consumer is to use.</p>"""
    producer_arn: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the producer namespace.</p>"""
    allow_publicly_accessible_consumers: NotRequired[
        "aws_sdk_redshift.types.boolean.Boolean"
    ]
    """<p>A value that specifies whether the datashare can be shared to a publicly accessible cluster.</p>"""
    data_share_associations: NotRequired[
        "aws_sdk_redshift.types.data_share_association_list.DataShareAssociationList"
    ]
    """<p>A value that specifies when the datashare has an association between producer and data consumers.</p>"""
    managed_by: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The identifier of a datashare to show its managing entity.</p>"""
    data_share_type: NotRequired["aws_sdk_redshift.types.data_share_type.DataShareType"]
    """<p> The type of the datashare created by RegisterNamespace.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DataShare, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "data_share_arn" in value:
        pairs.append((f"{prefix}.DataShareArn", str(value["data_share_arn"])))
    if "producer_arn" in value:
        pairs.append((f"{prefix}.ProducerArn", str(value["producer_arn"])))
    if "allow_publicly_accessible_consumers" in value:
        pairs.append(
            (
                f"{prefix}.AllowPubliclyAccessibleConsumers",
                "true" if value["allow_publicly_accessible_consumers"] else "false",
            )
        )
    if "data_share_associations" in value:
        import aws_sdk_redshift.types.data_share_association_list

        aws_sdk_redshift.types.data_share_association_list.serialize_query(
            value["data_share_associations"], pairs, f"{prefix}.DataShareAssociations"
        )
    if "managed_by" in value:
        pairs.append((f"{prefix}.ManagedBy", str(value["managed_by"])))
    if "data_share_type" in value:
        import aws_sdk_redshift.types.data_share_type

        aws_sdk_redshift.types.data_share_type.serialize_query(
            value["data_share_type"], pairs, f"{prefix}.DataShareType"
        )


def deserialize_query(el: Element) -> DataShare:
    out: DataShare = {}  # type: ignore[typeddict-item]
    child_data_share_arn = el.find("DataShareArn")
    if child_data_share_arn is not None:
        out["data_share_arn"] = str(child_data_share_arn.text or "")
    child_producer_arn = el.find("ProducerArn")
    if child_producer_arn is not None:
        out["producer_arn"] = str(child_producer_arn.text or "")
    child_allow_publicly_accessible_consumers = el.find(
        "AllowPubliclyAccessibleConsumers"
    )
    if child_allow_publicly_accessible_consumers is not None:
        out["allow_publicly_accessible_consumers"] = (
            child_allow_publicly_accessible_consumers.text or ""
        ).lower() == "true"
    child_data_share_associations = el.find("DataShareAssociations")
    if child_data_share_associations is not None:
        import aws_sdk_redshift.types.data_share_association_list

        out["data_share_associations"] = (
            aws_sdk_redshift.types.data_share_association_list.deserialize_query(
                child_data_share_associations
            )
        )
    child_managed_by = el.find("ManagedBy")
    if child_managed_by is not None:
        out["managed_by"] = str(child_managed_by.text or "")
    child_data_share_type = el.find("DataShareType")
    if child_data_share_type is not None:
        import aws_sdk_redshift.types.data_share_type

        out["data_share_type"] = (
            aws_sdk_redshift.types.data_share_type.deserialize_query(
                child_data_share_type
            )
        )
    return out
