"""Generated from Smithy shape ``com.amazonaws.servicediscovery#CreatePrivateDnsNamespaceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.namespace_name_private
    import aws_sdk_servicediscovery.types.private_dns_namespace_properties
    import aws_sdk_servicediscovery.types.resource_description
    import aws_sdk_servicediscovery.types.resource_id
    import aws_sdk_servicediscovery.types.tag_list


class CreatePrivateDnsNamespaceRequest(TypedDict):
    name: "aws_sdk_servicediscovery.types.namespace_name_private.NamespaceNamePrivate"
    """<p>The name that you want to assign to this namespace. When you create a private DNS namespace, Cloud Map automatically creates an Amazon Route 53 private hosted zone that has the same name as the namespace.</p>"""
    creator_request_id: NotRequired[
        "aws_sdk_servicediscovery.types.resource_id.ResourceId"
    ]
    """<p>A unique string that identifies the request and that allows failed <code>CreatePrivateDnsNamespace</code> requests to be retried without the risk of running the operation twice. <code>CreatorRequestId</code> can be any unique string (for example, a date/timestamp).</p>"""
    description: NotRequired[
        "aws_sdk_servicediscovery.types.resource_description.ResourceDescription"
    ]
    """<p>A description for the namespace.</p>"""
    vpc: "aws_sdk_servicediscovery.types.resource_id.ResourceId"
    """<p>The ID of the Amazon VPC that you want to associate the namespace with.</p>"""
    tags: NotRequired["aws_sdk_servicediscovery.types.tag_list.TagList"]
    """<p>The tags to add to the namespace. Each tag consists of a key and an optional value that you define. Tags keys can be up to 128 characters in length, and tag values can be up to 256 characters in length.</p>"""
    properties: NotRequired[
        "aws_sdk_servicediscovery.types.private_dns_namespace_properties.PrivateDnsNamespaceProperties"
    ]
    """<p>Properties for the private DNS namespace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatePrivateDnsNamespaceRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    if "description" in value:
        out["Description"] = value["description"]
    out["Vpc"] = value["vpc"]
    if "tags" in value:
        import aws_sdk_servicediscovery.types.tag_list

        out["Tags"] = aws_sdk_servicediscovery.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "properties" in value:
        import aws_sdk_servicediscovery.types.private_dns_namespace_properties

        out["Properties"] = (
            aws_sdk_servicediscovery.types.private_dns_namespace_properties.serialize_aws_json_1_1(
                value["properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatePrivateDnsNamespaceRequest:
    out: CreatePrivateDnsNamespaceRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreatePrivateDnsNamespaceRequest.name required")
    if "CreatorRequestId" in data:
        out["creator_request_id"] = data["CreatorRequestId"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Vpc" in data:
        out["vpc"] = data["Vpc"]
    else:
        raise DeserializationError("CreatePrivateDnsNamespaceRequest.vpc required")
    if "Tags" in data:
        import aws_sdk_servicediscovery.types.tag_list

        out["tags"] = aws_sdk_servicediscovery.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "Properties" in data:
        import aws_sdk_servicediscovery.types.private_dns_namespace_properties

        out["properties"] = (
            aws_sdk_servicediscovery.types.private_dns_namespace_properties.deserialize_aws_json_1_1(
                data["Properties"]
            )
        )
    return out
