"""Generated from Smithy shape ``com.amazonaws.supplychain#CreateDataLakeNamespaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.data_lake_namespace_description
    import aws_sdk_supplychain.types.data_lake_namespace_name
    import aws_sdk_supplychain.types.tag_map
    import aws_sdk_supplychain.types.uuid


class CreateDataLakeNamespaceRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_supplychain.types.uuid.UUID"
    """<p>The Amazon Web Services Supply Chain instance identifier.</p>"""
    name: "aws_sdk_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName"
    """<p>The name of the namespace. Noted you cannot create namespace with name starting with <b>asc</b>, <b>default</b>, <b>scn</b>, <b>aws</b>, <b>amazon</b>, <b>amzn</b> </p>"""
    description: NotRequired[
        "aws_sdk_supplychain.types.data_lake_namespace_description.DataLakeNamespaceDescription"
    ]
    """<p>The description of the namespace.</p>"""
    tags: NotRequired["aws_sdk_supplychain.types.tag_map.TagMap"]
    """<p>The tags of the namespace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataLakeNamespaceRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import aws_sdk_supplychain.types.tag_map

        out["tags"] = aws_sdk_supplychain.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateDataLakeNamespaceRequest:
    out: CreateDataLakeNamespaceRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import aws_sdk_supplychain.types.tag_map

        out["tags"] = aws_sdk_supplychain.types.tag_map.deserialize_json(data["tags"])
    return out
