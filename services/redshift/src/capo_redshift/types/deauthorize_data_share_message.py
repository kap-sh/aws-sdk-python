"""Generated from Smithy shape ``com.amazonaws.redshift#DeauthorizeDataShareMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string


class DeauthorizeDataShareMessage(TypedDict, closed=True):
    data_share_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The namespace Amazon Resource Name (ARN) of the datashare to remove authorization from.</p>"""
    consumer_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The identifier of the data consumer that is to have authorization removed from the datashare. This identifier is an Amazon Web Services account ID or a keyword, such as ADX.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeauthorizeDataShareMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "data_share_arn" in value:
        pairs.append((f"{prefix}.DataShareArn", str(value["data_share_arn"])))
    if "consumer_identifier" in value:
        pairs.append(
            (f"{prefix}.ConsumerIdentifier", str(value["consumer_identifier"]))
        )


def deserialize_query(el: Element) -> DeauthorizeDataShareMessage:
    out: DeauthorizeDataShareMessage = {}  # type: ignore[typeddict-item]
    child_data_share_arn = el.find("DataShareArn")
    if child_data_share_arn is not None:
        out["data_share_arn"] = str(child_data_share_arn.text or "")
    child_consumer_identifier = el.find("ConsumerIdentifier")
    if child_consumer_identifier is not None:
        out["consumer_identifier"] = str(child_consumer_identifier.text or "")
    return out
