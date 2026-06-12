"""Generated from Smithy shape ``com.amazonaws.redshift#CancelResizeMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string


class CancelResizeMessage(TypedDict):
    cluster_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The unique identifier for the cluster that you want to cancel a resize operation for.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CancelResizeMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cluster_identifier" in value:
        pairs.append((f"{prefix}.ClusterIdentifier", str(value["cluster_identifier"])))


def deserialize_query(el: Element) -> CancelResizeMessage:
    out: CancelResizeMessage = {}  # type: ignore[typeddict-item]
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    return out
