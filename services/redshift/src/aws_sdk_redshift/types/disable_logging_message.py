"""Generated from Smithy shape ``com.amazonaws.redshift#DisableLoggingMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string


class DisableLoggingMessage(TypedDict, closed=True):
    cluster_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The identifier of the cluster on which logging is to be stopped.</p> <p>Example: <code>examplecluster</code> </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DisableLoggingMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cluster_identifier" in value:
        pairs.append((f"{prefix}.ClusterIdentifier", str(value["cluster_identifier"])))


def deserialize_query(el: Element) -> DisableLoggingMessage:
    out: DisableLoggingMessage = {}  # type: ignore[typeddict-item]
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    return out
