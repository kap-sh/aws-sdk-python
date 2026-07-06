"""Generated from Smithy shape ``com.amazonaws.redshift#DisassociateDataShareConsumerMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.boolean_optional
    import aws_sdk_redshift.types.string


class DisassociateDataShareConsumerMessage(TypedDict, closed=True):
    data_share_arn: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the datashare to remove association for.</p>"""
    disassociate_entire_account: NotRequired[
        "aws_sdk_redshift.types.boolean_optional.BooleanOptional"
    ]
    """<p>A value that specifies whether association for the datashare is removed from the entire account.</p>"""
    consumer_arn: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the consumer namespace that association for the datashare is removed from.</p>"""
    consumer_region: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>From a datashare consumer account, removes association of a datashare from all the existing and future namespaces in the specified Amazon Web Services Region.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DisassociateDataShareConsumerMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "data_share_arn" in value:
        pairs.append((f"{prefix}.DataShareArn", str(value["data_share_arn"])))
    if "disassociate_entire_account" in value:
        pairs.append(
            (
                f"{prefix}.DisassociateEntireAccount",
                "true" if value["disassociate_entire_account"] else "false",
            )
        )
    if "consumer_arn" in value:
        pairs.append((f"{prefix}.ConsumerArn", str(value["consumer_arn"])))
    if "consumer_region" in value:
        pairs.append((f"{prefix}.ConsumerRegion", str(value["consumer_region"])))


def deserialize_query(el: Element) -> DisassociateDataShareConsumerMessage:
    out: DisassociateDataShareConsumerMessage = {}  # type: ignore[typeddict-item]
    child_data_share_arn = el.find("DataShareArn")
    if child_data_share_arn is not None:
        out["data_share_arn"] = str(child_data_share_arn.text or "")
    child_disassociate_entire_account = el.find("DisassociateEntireAccount")
    if child_disassociate_entire_account is not None:
        out["disassociate_entire_account"] = (
            child_disassociate_entire_account.text or ""
        ).lower() == "true"
    child_consumer_arn = el.find("ConsumerArn")
    if child_consumer_arn is not None:
        out["consumer_arn"] = str(child_consumer_arn.text or "")
    child_consumer_region = el.find("ConsumerRegion")
    if child_consumer_region is not None:
        out["consumer_region"] = str(child_consumer_region.text or "")
    return out
