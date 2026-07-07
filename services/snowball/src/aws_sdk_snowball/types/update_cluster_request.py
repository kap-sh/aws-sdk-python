"""Generated from Smithy shape ``com.amazonaws.snowball#UpdateClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_snowball.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_snowball.types.address_id
    import aws_sdk_snowball.types.cluster_id
    import aws_sdk_snowball.types.job_resource
    import aws_sdk_snowball.types.notification
    import aws_sdk_snowball.types.on_device_service_configuration
    import aws_sdk_snowball.types.role_arn
    import aws_sdk_snowball.types.shipping_option
    import aws_sdk_snowball.types.string


class UpdateClusterRequest(TypedDict, closed=True):
    cluster_id: "aws_sdk_snowball.types.cluster_id.ClusterId"
    """<p>The cluster ID of the cluster that you want to update, for example <code>CID123e4567-e89b-12d3-a456-426655440000</code>.</p>"""
    role_arn: NotRequired["aws_sdk_snowball.types.role_arn.RoleARN"]
    r"""<p>The new role Amazon Resource Name (ARN) that you want to associate with this cluster. To create a role ARN, use the <a href=\"https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html\">CreateRole</a> API action in Identity and Access Management (IAM).</p>"""
    description: NotRequired["aws_sdk_snowball.types.string.String"]
    """<p>The updated description of this cluster.</p>"""
    resources: NotRequired["aws_sdk_snowball.types.job_resource.JobResource"]
    """<p>The updated arrays of <a>JobResource</a> objects that can include updated <a>S3Resource</a> objects or <a>LambdaResource</a> objects.</p>"""
    on_device_service_configuration: NotRequired[
        "aws_sdk_snowball.types.on_device_service_configuration.OnDeviceServiceConfiguration"
    ]
    """<p>Specifies the service or services on the Snow Family device that your transferred data will be exported from or imported into. Amazon Web Services Snow Family device clusters support Amazon S3 and NFS (Network File System).</p>"""
    address_id: NotRequired["aws_sdk_snowball.types.address_id.AddressId"]
    """<p>The ID of the updated <a>Address</a> object.</p>"""
    shipping_option: NotRequired[
        "aws_sdk_snowball.types.shipping_option.ShippingOption"
    ]
    """<p>The updated shipping option value of this cluster's <a>ShippingDetails</a> object.</p>"""
    notification: NotRequired["aws_sdk_snowball.types.notification.Notification"]
    """<p>The new or updated <a>Notification</a> object.</p>"""
    forwarding_address_id: NotRequired["aws_sdk_snowball.types.address_id.AddressId"]
    """<p>The updated ID for the forwarding address for a cluster. This field is not supported in most regions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateClusterRequest) -> dict:
    out: dict = {}
    out["ClusterId"] = value["cluster_id"]
    if "role_arn" in value:
        out["RoleARN"] = value["role_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "resources" in value:
        import aws_sdk_snowball.types.job_resource

        out["Resources"] = aws_sdk_snowball.types.job_resource.serialize_aws_json_1_1(
            value["resources"]
        )
    if "on_device_service_configuration" in value:
        import aws_sdk_snowball.types.on_device_service_configuration

        out["OnDeviceServiceConfiguration"] = (
            aws_sdk_snowball.types.on_device_service_configuration.serialize_aws_json_1_1(
                value["on_device_service_configuration"]
            )
        )
    if "address_id" in value:
        out["AddressId"] = value["address_id"]
    if "shipping_option" in value:
        import aws_sdk_snowball.types.shipping_option

        out["ShippingOption"] = (
            aws_sdk_snowball.types.shipping_option.serialize_aws_json_1_1(
                value["shipping_option"]
            )
        )
    if "notification" in value:
        import aws_sdk_snowball.types.notification

        out["Notification"] = (
            aws_sdk_snowball.types.notification.serialize_aws_json_1_1(
                value["notification"]
            )
        )
    if "forwarding_address_id" in value:
        out["ForwardingAddressId"] = value["forwarding_address_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateClusterRequest:
    out: UpdateClusterRequest = {}  # type: ignore[typeddict-item]
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    else:
        raise DeserializationError("UpdateClusterRequest.cluster_id required")
    if "RoleARN" in data:
        out["role_arn"] = data["RoleARN"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Resources" in data:
        import aws_sdk_snowball.types.job_resource

        out["resources"] = aws_sdk_snowball.types.job_resource.deserialize_aws_json_1_1(
            data["Resources"]
        )
    if "OnDeviceServiceConfiguration" in data:
        import aws_sdk_snowball.types.on_device_service_configuration

        out["on_device_service_configuration"] = (
            aws_sdk_snowball.types.on_device_service_configuration.deserialize_aws_json_1_1(
                data["OnDeviceServiceConfiguration"]
            )
        )
    if "AddressId" in data:
        out["address_id"] = data["AddressId"]
    if "ShippingOption" in data:
        import aws_sdk_snowball.types.shipping_option

        out["shipping_option"] = (
            aws_sdk_snowball.types.shipping_option.deserialize_aws_json_1_1(
                data["ShippingOption"]
            )
        )
    if "Notification" in data:
        import aws_sdk_snowball.types.notification

        out["notification"] = (
            aws_sdk_snowball.types.notification.deserialize_aws_json_1_1(
                data["Notification"]
            )
        )
    if "ForwardingAddressId" in data:
        out["forwarding_address_id"] = data["ForwardingAddressId"]
    return out
