"""Generated from Smithy shape ``com.amazonaws.redshift#DeleteEndpointAccessMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string


class DeleteEndpointAccessMessage(TypedDict, closed=True):
    endpoint_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The Redshift-managed VPC endpoint to delete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteEndpointAccessMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "endpoint_name" in value:
        pairs.append((f"{key_prefix}EndpointName", str(value["endpoint_name"])))


def deserialize_query(el: Element) -> DeleteEndpointAccessMessage:
    out: DeleteEndpointAccessMessage = {}  # type: ignore[typeddict-item]
    child_endpoint_name = el.find("EndpointName")
    if child_endpoint_name is not None:
        out["endpoint_name"] = str(child_endpoint_name.text or "")
    return out
