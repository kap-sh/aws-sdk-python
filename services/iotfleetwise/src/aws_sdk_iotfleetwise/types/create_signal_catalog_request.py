"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#CreateSignalCatalogRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.description
    import aws_sdk_iotfleetwise.types.nodes
    import aws_sdk_iotfleetwise.types.resource_name
    import aws_sdk_iotfleetwise.types.tag_list


class CreateSignalCatalogRequest(TypedDict):
    name: "aws_sdk_iotfleetwise.types.resource_name.resourceName"
    """<p> The name of the signal catalog to create. </p>"""
    description: NotRequired["aws_sdk_iotfleetwise.types.description.description"]
    """<p>A brief description of the signal catalog.</p>"""
    nodes: NotRequired["aws_sdk_iotfleetwise.types.nodes.Nodes"]
    """<p> A list of information about nodes, which are a general abstraction of signals. For more information, see the API data type.</p>"""
    tags: NotRequired["aws_sdk_iotfleetwise.types.tag_list.TagList"]
    """<p>Metadata that can be used to manage the signal catalog.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateSignalCatalogRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "nodes" in value:
        import aws_sdk_iotfleetwise.types.nodes

        out["nodes"] = aws_sdk_iotfleetwise.types.nodes.serialize_aws_json_1_0(
            value["nodes"]
        )
    if "tags" in value:
        import aws_sdk_iotfleetwise.types.tag_list

        out["tags"] = aws_sdk_iotfleetwise.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateSignalCatalogRequest:
    out: CreateSignalCatalogRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "nodes" in data:
        import aws_sdk_iotfleetwise.types.nodes

        out["nodes"] = aws_sdk_iotfleetwise.types.nodes.deserialize_aws_json_1_0(
            data["nodes"]
        )
    if "tags" in data:
        import aws_sdk_iotfleetwise.types.tag_list

        out["tags"] = aws_sdk_iotfleetwise.types.tag_list.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
