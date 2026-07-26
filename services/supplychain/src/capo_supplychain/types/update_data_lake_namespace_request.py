"""Generated from Smithy shape ``com.amazonaws.supplychain#UpdateDataLakeNamespaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_supplychain.types.data_lake_namespace_description
    import capo_supplychain.types.data_lake_namespace_name
    import capo_supplychain.types.uuid


class UpdateDataLakeNamespaceRequest(TypedDict, closed=True):
    instance_id: "capo_supplychain.types.uuid.UUID"
    """<p>The Amazon Web Services Chain instance identifier.</p>"""
    name: "capo_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName"
    """<p>The name of the namespace. Noted you cannot update namespace with name starting with <b>asc</b>, <b>default</b>, <b>scn</b>, <b>aws</b>, <b>amazon</b>, <b>amzn</b> </p>"""
    description: NotRequired[
        "capo_supplychain.types.data_lake_namespace_description.DataLakeNamespaceDescription"
    ]
    """<p>The updated description of the data lake namespace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataLakeNamespaceRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateDataLakeNamespaceRequest:
    out: UpdateDataLakeNamespaceRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    return out
