"""Generated from Smithy shape ``com.amazonaws.servicediscovery#Namespace``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.arn
    import aws_sdk_servicediscovery.types.aws_account_id
    import aws_sdk_servicediscovery.types.namespace_name
    import aws_sdk_servicediscovery.types.namespace_properties
    import aws_sdk_servicediscovery.types.namespace_type
    import aws_sdk_servicediscovery.types.resource_count
    import aws_sdk_servicediscovery.types.resource_description
    import aws_sdk_servicediscovery.types.resource_id
    import aws_sdk_servicediscovery.types.timestamp


class Namespace(TypedDict):
    id: NotRequired["aws_sdk_servicediscovery.types.resource_id.ResourceId"]
    """<p>The ID of a namespace.</p>"""
    arn: NotRequired["aws_sdk_servicediscovery.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) that Cloud Map assigns to the namespace when you create it.</p>"""
    resource_owner: NotRequired[
        "aws_sdk_servicediscovery.types.aws_account_id.AWSAccountId"
    ]
    r"""<p>The ID of the Amazon Web Services account that created the namespace. If this isn't your account ID, it's the ID of the account that shared the namespace with your account. For more information about shared namespaces, see <a href=\"https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html\">Cross-account Cloud Map namespace sharing</a> in the <i>Cloud Map Developer Guide</i>.</p>"""
    name: NotRequired["aws_sdk_servicediscovery.types.namespace_name.NamespaceName"]
    """<p>The name of the namespace, such as <code>example.com</code>.</p>"""
    type: NotRequired["aws_sdk_servicediscovery.types.namespace_type.NamespaceType"]
    """<p>The type of the namespace. The methods for discovering instances depends on the value that you specify:</p> <dl> <dt>HTTP</dt> <dd> <p>Instances can be discovered only programmatically, using the Cloud Map <code>DiscoverInstances</code> API.</p> </dd> <dt>DNS_PUBLIC</dt> <dd> <p>Instances can be discovered using public DNS queries and using the <code>DiscoverInstances</code> API.</p> </dd> <dt>DNS_PRIVATE</dt> <dd> <p>Instances can be discovered using DNS queries in VPCs and using the <code>DiscoverInstances</code> API.</p> </dd> </dl>"""
    description: NotRequired[
        "aws_sdk_servicediscovery.types.resource_description.ResourceDescription"
    ]
    """<p>The description that you specify for the namespace when you create it.</p>"""
    service_count: NotRequired[
        "aws_sdk_servicediscovery.types.resource_count.ResourceCount"
    ]
    """<p>The number of services that are associated with the namespace.</p>"""
    properties: NotRequired[
        "aws_sdk_servicediscovery.types.namespace_properties.NamespaceProperties"
    ]
    """<p>A complex type that contains information that's specific to the type of the namespace.</p>"""
    create_date: NotRequired["aws_sdk_servicediscovery.types.timestamp.Timestamp"]
    """<p>The date that the namespace was created, in Unix date/time format and Coordinated Universal Time (UTC). The value of <code>CreateDate</code> is accurate to milliseconds. For example, the value <code>1516925490.087</code> represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""
    creator_request_id: NotRequired[
        "aws_sdk_servicediscovery.types.resource_id.ResourceId"
    ]
    """<p>A unique string that identifies the request and that allows failed requests to be retried without the risk of running an operation twice. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Namespace) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "resource_owner" in value:
        out["ResourceOwner"] = value["resource_owner"]
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import aws_sdk_servicediscovery.types.namespace_type

        out["Type"] = (
            aws_sdk_servicediscovery.types.namespace_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "service_count" in value:
        out["ServiceCount"] = value["service_count"]
    if "properties" in value:
        import aws_sdk_servicediscovery.types.namespace_properties

        out["Properties"] = (
            aws_sdk_servicediscovery.types.namespace_properties.serialize_aws_json_1_1(
                value["properties"]
            )
        )
    if "create_date" in value:
        import aws_sdk_servicediscovery.types.timestamp

        out["CreateDate"] = (
            aws_sdk_servicediscovery.types.timestamp.serialize_aws_json_1_1(
                value["create_date"]
            )
        )
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Namespace:
    out: Namespace = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "ResourceOwner" in data:
        out["resource_owner"] = data["ResourceOwner"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        import aws_sdk_servicediscovery.types.namespace_type

        out["type"] = (
            aws_sdk_servicediscovery.types.namespace_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "ServiceCount" in data:
        out["service_count"] = data["ServiceCount"]
    if "Properties" in data:
        import aws_sdk_servicediscovery.types.namespace_properties

        out["properties"] = (
            aws_sdk_servicediscovery.types.namespace_properties.deserialize_aws_json_1_1(
                data["Properties"]
            )
        )
    if "CreateDate" in data:
        import aws_sdk_servicediscovery.types.timestamp

        out["create_date"] = (
            aws_sdk_servicediscovery.types.timestamp.deserialize_aws_json_1_1(
                data["CreateDate"]
            )
        )
    if "CreatorRequestId" in data:
        out["creator_request_id"] = data["CreatorRequestId"]
    return out
