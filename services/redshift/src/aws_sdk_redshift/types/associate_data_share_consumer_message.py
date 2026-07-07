"""Generated from Smithy shape ``com.amazonaws.redshift#AssociateDataShareConsumerMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.boolean_optional
    import aws_sdk_redshift.types.string


class AssociateDataShareConsumerMessage(TypedDict, closed=True):
    data_share_arn: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the datashare that the consumer is to use.</p>"""
    associate_entire_account: NotRequired[
        "aws_sdk_redshift.types.boolean_optional.BooleanOptional"
    ]
    """<p>A value that specifies whether the datashare is associated with the entire account.</p>"""
    consumer_arn: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the consumer namespace associated with the datashare.</p>"""
    consumer_region: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>From a datashare consumer account, associates a datashare with all existing and future namespaces in the specified Amazon Web Services Region.</p>"""
    allow_writes: NotRequired["aws_sdk_redshift.types.boolean_optional.BooleanOptional"]
    """<p>If set to true, allows write operations for a datashare.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AssociateDataShareConsumerMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "data_share_arn" in value:
        pairs.append((f"{prefix}.DataShareArn", str(value["data_share_arn"])))
    if "associate_entire_account" in value:
        pairs.append(
            (
                f"{prefix}.AssociateEntireAccount",
                "true" if value["associate_entire_account"] else "false",
            )
        )
    if "consumer_arn" in value:
        pairs.append((f"{prefix}.ConsumerArn", str(value["consumer_arn"])))
    if "consumer_region" in value:
        pairs.append((f"{prefix}.ConsumerRegion", str(value["consumer_region"])))
    if "allow_writes" in value:
        pairs.append(
            (f"{prefix}.AllowWrites", "true" if value["allow_writes"] else "false")
        )


def deserialize_query(el: Element) -> AssociateDataShareConsumerMessage:
    out: AssociateDataShareConsumerMessage = {}  # type: ignore[typeddict-item]
    child_data_share_arn = el.find("DataShareArn")
    if child_data_share_arn is not None:
        out["data_share_arn"] = str(child_data_share_arn.text or "")
    child_associate_entire_account = el.find("AssociateEntireAccount")
    if child_associate_entire_account is not None:
        out["associate_entire_account"] = (
            child_associate_entire_account.text or ""
        ).lower() == "true"
    child_consumer_arn = el.find("ConsumerArn")
    if child_consumer_arn is not None:
        out["consumer_arn"] = str(child_consumer_arn.text or "")
    child_consumer_region = el.find("ConsumerRegion")
    if child_consumer_region is not None:
        out["consumer_region"] = str(child_consumer_region.text or "")
    child_allow_writes = el.find("AllowWrites")
    if child_allow_writes is not None:
        out["allow_writes"] = (child_allow_writes.text or "").lower() == "true"
    return out
