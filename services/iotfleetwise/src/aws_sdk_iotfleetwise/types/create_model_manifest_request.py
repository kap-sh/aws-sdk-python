"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#CreateModelManifestRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.arn
    import aws_sdk_iotfleetwise.types.description
    import aws_sdk_iotfleetwise.types.list_of_strings
    import aws_sdk_iotfleetwise.types.resource_name
    import aws_sdk_iotfleetwise.types.tag_list


class CreateModelManifestRequest(TypedDict):
    name: "aws_sdk_iotfleetwise.types.resource_name.resourceName"
    """<p> The name of the vehicle model to create.</p>"""
    description: NotRequired["aws_sdk_iotfleetwise.types.description.description"]
    """<p> A brief description of the vehicle model. </p>"""
    nodes: "aws_sdk_iotfleetwise.types.list_of_strings.listOfStrings"
    """<p> A list of nodes, which are a general abstraction of signals. </p>"""
    signal_catalog_arn: "aws_sdk_iotfleetwise.types.arn.arn"
    """<p> The Amazon Resource Name (ARN) of a signal catalog. </p>"""
    tags: NotRequired["aws_sdk_iotfleetwise.types.tag_list.TagList"]
    """<p>Metadata that can be used to manage the vehicle model.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateModelManifestRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_iotfleetwise.types.list_of_strings

    out["nodes"] = aws_sdk_iotfleetwise.types.list_of_strings.serialize_aws_json_1_0(
        value["nodes"]
    )
    out["signalCatalogArn"] = value["signal_catalog_arn"]
    if "tags" in value:
        import aws_sdk_iotfleetwise.types.tag_list

        out["tags"] = aws_sdk_iotfleetwise.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateModelManifestRequest:
    out: CreateModelManifestRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "nodes" in data:
        import aws_sdk_iotfleetwise.types.list_of_strings

        out["nodes"] = (
            aws_sdk_iotfleetwise.types.list_of_strings.deserialize_aws_json_1_0(
                data["nodes"]
            )
        )
    else:
        raise DeserializationError("CreateModelManifestRequest.nodes required")
    if "signalCatalogArn" in data:
        out["signal_catalog_arn"] = data["signalCatalogArn"]
    else:
        raise DeserializationError(
            "CreateModelManifestRequest.signal_catalog_arn required"
        )
    if "tags" in data:
        import aws_sdk_iotfleetwise.types.tag_list

        out["tags"] = aws_sdk_iotfleetwise.types.tag_list.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
