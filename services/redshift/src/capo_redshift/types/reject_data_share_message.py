"""Generated from Smithy shape ``com.amazonaws.redshift#RejectDataShareMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string


class RejectDataShareMessage(TypedDict, closed=True):
    data_share_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the datashare to reject.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RejectDataShareMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "data_share_arn" in value:
        pairs.append((f"{key_prefix}DataShareArn", str(value["data_share_arn"])))


def deserialize_query(el: Element) -> RejectDataShareMessage:
    out: RejectDataShareMessage = {}  # type: ignore[typeddict-item]
    child_data_share_arn = el.find("DataShareArn")
    if child_data_share_arn is not None:
        out["data_share_arn"] = str(child_data_share_arn.text or "")
    return out
