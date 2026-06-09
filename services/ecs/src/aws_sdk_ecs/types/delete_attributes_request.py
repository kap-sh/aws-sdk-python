"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteAttributesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.attributes
    import aws_sdk_ecs.types.string


class DeleteAttributesRequest(TypedDict):
    cluster: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that contains the resource to delete attributes. If you do not specify a cluster, the default cluster is assumed.</p>"""
    attributes: "aws_sdk_ecs.types.attributes.Attributes"
    """<p>The attributes to delete from your resource. You can specify up to 10 attributes for each request. For custom attributes, specify the attribute name and target ID, but don't specify the value. If you specify the target ID using the short form, you must also specify the target type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAttributesRequest) -> dict:
    out: dict = {}
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    import aws_sdk_ecs.types.attributes

    out["attributes"] = aws_sdk_ecs.types.attributes.serialize_aws_json_1_1(
        value["attributes"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAttributesRequest:
    out: DeleteAttributesRequest = {}  # type: ignore[typeddict-item]
    if "cluster" in data:
        out["cluster"] = data["cluster"]
    if "attributes" in data:
        import aws_sdk_ecs.types.attributes

        out["attributes"] = aws_sdk_ecs.types.attributes.deserialize_aws_json_1_1(
            data["attributes"]
        )
    else:
        raise DeserializationError("DeleteAttributesRequest.attributes required")
    return out
