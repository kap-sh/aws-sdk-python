"""Generated from Smithy shape ``com.amazonaws.redshift#RejectDataShareMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string


class RejectDataShareMessage(TypedDict, closed=True):
    data_share_arn: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the datashare to reject.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RejectDataShareMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "data_share_arn" in value:
        pairs.append((f"{prefix}.DataShareArn", str(value["data_share_arn"])))


def deserialize_query(el: Element) -> RejectDataShareMessage:
    out: RejectDataShareMessage = {}  # type: ignore[typeddict-item]
    child_data_share_arn = el.find("DataShareArn")
    if child_data_share_arn is not None:
        out["data_share_arn"] = str(child_data_share_arn.text or "")
    return out
