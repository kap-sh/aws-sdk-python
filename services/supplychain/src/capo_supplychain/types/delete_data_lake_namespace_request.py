"""Generated from Smithy shape ``com.amazonaws.supplychain#DeleteDataLakeNamespaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_supplychain.types.data_lake_namespace_name
    import capo_supplychain.types.uuid


class DeleteDataLakeNamespaceRequest(TypedDict, closed=True):
    instance_id: "capo_supplychain.types.uuid.UUID"
    """<p>The AWS Supply Chain instance identifier.</p>"""
    name: "capo_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName"
    """<p>The name of the namespace. Noted you cannot delete pre-defined namespace like <b>asc</b>, <b>default</b> which are only deleted through instance deletion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataLakeNamespaceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDataLakeNamespaceRequest:
    out: DeleteDataLakeNamespaceRequest = {}  # type: ignore[typeddict-item]
    return out
