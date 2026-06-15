"""Generated from Smithy shape ``com.amazonaws.servicediscovery#NamespaceSummary``."""

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


class NamespaceSummary(TypedDict):
    id: NotRequired["aws_sdk_servicediscovery.types.resource_id.ResourceId"]
    """<p>The ID of the namespace.</p>"""
    arn: NotRequired["aws_sdk_servicediscovery.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) that Cloud Map assigns to the namespace when you create it.</p>"""
    resource_owner: NotRequired[
        "aws_sdk_servicediscovery.types.aws_account_id.AWSAccountId"
    ]
    r"""<p>The ID of the Amazon Web Services account that created the namespace. If this isn't your account ID, it's the ID of the account that shared the namespace with your account. For more information about shared namespaces, see <a href=\"https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html\">Cross-account Cloud Map namespace sharing</a> in the <i>Cloud Map Developer Guide</i>.</p>"""
    name: NotRequired["aws_sdk_servicediscovery.types.namespace_name.NamespaceName"]
    """<p>The name of the namespace. When you create a namespace, Cloud Map automatically creates a Route 53 hosted zone that has the same name as the namespace.</p>"""
    type: NotRequired["aws_sdk_servicediscovery.types.namespace_type.NamespaceType"]
    """<p>The type of the namespace, either public or private.</p>"""
    description: NotRequired[
        "aws_sdk_servicediscovery.types.resource_description.ResourceDescription"
    ]
    """<p>A description for the namespace.</p>"""
    service_count: NotRequired[
        "aws_sdk_servicediscovery.types.resource_count.ResourceCount"
    ]
    """<p>The number of services that were created using the namespace.</p>"""
    properties: NotRequired[
        "aws_sdk_servicediscovery.types.namespace_properties.NamespaceProperties"
    ]
    """<p>The properties of the namespace.</p>"""
    create_date: NotRequired["aws_sdk_servicediscovery.types.timestamp.Timestamp"]
    """<p>The date and time that the namespace was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NamespaceSummary) -> dict:
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
    return out


def deserialize_aws_json_1_1(data: dict) -> NamespaceSummary:
    out: NamespaceSummary = {}  # type: ignore[typeddict-item]
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
    return out
