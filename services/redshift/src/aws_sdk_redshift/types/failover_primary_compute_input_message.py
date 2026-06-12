"""Generated from Smithy shape ``com.amazonaws.redshift#FailoverPrimaryComputeInputMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string


class FailoverPrimaryComputeInputMessage(TypedDict):
    cluster_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The unique identifier of the cluster for which the primary compute unit will be failed over to another Availability Zone.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: FailoverPrimaryComputeInputMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cluster_identifier" in value:
        pairs.append((f"{prefix}.ClusterIdentifier", str(value["cluster_identifier"])))


def deserialize_query(el: Element) -> FailoverPrimaryComputeInputMessage:
    out: FailoverPrimaryComputeInputMessage = {}  # type: ignore[typeddict-item]
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    return out
