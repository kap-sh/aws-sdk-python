"""Generated from Smithy shape ``com.amazonaws.redshift#ProvisionedIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string


class ProvisionedIdentifier(TypedDict, closed=True):
    cluster_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The unique identifier for the provisioned cluster.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ProvisionedIdentifier, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}ClusterIdentifier", str(value["cluster_identifier"]))
        )


def deserialize_query(el: Element) -> ProvisionedIdentifier:
    out: ProvisionedIdentifier = {}  # type: ignore[typeddict-item]
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    return out
