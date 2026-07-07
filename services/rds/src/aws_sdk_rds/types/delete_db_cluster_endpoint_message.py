"""Generated from Smithy shape ``com.amazonaws.rds#DeleteDBClusterEndpointMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.string


class DeleteDBClusterEndpointMessage(TypedDict, closed=True):
    db_cluster_endpoint_identifier: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The identifier associated with the custom endpoint. This parameter is stored as a lowercase string.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteDBClusterEndpointMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_cluster_endpoint_identifier" in value:
        pairs.append(
            (
                f"{prefix}.DBClusterEndpointIdentifier",
                str(value["db_cluster_endpoint_identifier"]),
            )
        )


def deserialize_query(el: Element) -> DeleteDBClusterEndpointMessage:
    out: DeleteDBClusterEndpointMessage = {}  # type: ignore[typeddict-item]
    child_db_cluster_endpoint_identifier = el.find("DBClusterEndpointIdentifier")
    if child_db_cluster_endpoint_identifier is not None:
        out["db_cluster_endpoint_identifier"] = str(
            child_db_cluster_endpoint_identifier.text or ""
        )
    return out
