"""Generated from Smithy shape ``com.amazonaws.redshift#GetIdentityCenterAuthTokenRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.cluster_identifier_list


class GetIdentityCenterAuthTokenRequest(TypedDict, closed=True):
    cluster_ids: NotRequired[
        "capo_redshift.types.cluster_identifier_list.ClusterIdentifierList"
    ]
    """<p>A list of cluster identifiers that the generated token can be used with. The token will be scoped to only allow authentication to the specified clusters.</p> <p>Constraints:</p> <ul> <li> <p> <code>ClusterIds</code> must contain at least 1 cluster identifier.</p> </li> <li> <p> <code>ClusterIds</code> can hold a maximum of 20 cluster identifiers.</p> </li> <li> <p>Cluster identifiers must be 1 to 63 characters in length.</p> </li> <li> <p>The characters accepted for cluster identifiers are the following:</p> <ul> <li> <p>Alphanumeric characters</p> </li> <li> <p>Hyphens</p> </li> </ul> </li> <li> <p>Cluster identifiers must start with a letter.</p> </li> <li> <p>Cluster identifiers can't end with a hyphen or contain two consecutive hyphens.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetIdentityCenterAuthTokenRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cluster_ids" in value:
        import capo_redshift.types.cluster_identifier_list

        capo_redshift.types.cluster_identifier_list.serialize_query(
            value["cluster_ids"], pairs, f"{key_prefix}ClusterIds"
        )


def deserialize_query(el: Element) -> GetIdentityCenterAuthTokenRequest:
    out: GetIdentityCenterAuthTokenRequest = {}  # type: ignore[typeddict-item]
    child_cluster_ids = el.find("ClusterIds")
    if child_cluster_ids is not None:
        import capo_redshift.types.cluster_identifier_list

        out["cluster_ids"] = (
            capo_redshift.types.cluster_identifier_list.deserialize_query(
                child_cluster_ids
            )
        )
    return out
