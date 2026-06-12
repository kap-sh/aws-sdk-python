"""Generated from Smithy shape ``com.amazonaws.snowball#UpdateJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_snowball.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_snowball.types.address_id
    import aws_sdk_snowball.types.job_id
    import aws_sdk_snowball.types.job_resource
    import aws_sdk_snowball.types.notification
    import aws_sdk_snowball.types.on_device_service_configuration
    import aws_sdk_snowball.types.pickup_details
    import aws_sdk_snowball.types.role_arn
    import aws_sdk_snowball.types.shipping_option
    import aws_sdk_snowball.types.snowball_capacity
    import aws_sdk_snowball.types.string


class UpdateJobRequest(TypedDict):
    job_id: "aws_sdk_snowball.types.job_id.JobId"
    """<p>The job ID of the job that you want to update, for example <code>JID123e4567-e89b-12d3-a456-426655440000</code>.</p>"""
    role_arn: NotRequired["aws_sdk_snowball.types.role_arn.RoleARN"]
    """<p>The new role Amazon Resource Name (ARN) that you want to associate with this job. To create a role ARN, use the <a href=\"https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html\">CreateRole</a>Identity and Access Management (IAM) API action.</p>"""
    notification: NotRequired["aws_sdk_snowball.types.notification.Notification"]
    """<p>The new or updated <a>Notification</a> object.</p>"""
    resources: NotRequired["aws_sdk_snowball.types.job_resource.JobResource"]
    """<p>The updated <code>JobResource</code> object, or the updated <a>JobResource</a> object. </p>"""
    on_device_service_configuration: NotRequired[
        "aws_sdk_snowball.types.on_device_service_configuration.OnDeviceServiceConfiguration"
    ]
    """<p>Specifies the service or services on the Snow Family device that your transferred data will be exported from or imported into. Amazon Web Services Snow Family supports Amazon S3 and NFS (Network File System) and the Amazon Web Services Storage Gateway service Tape Gateway type.</p>"""
    address_id: NotRequired["aws_sdk_snowball.types.address_id.AddressId"]
    """<p>The ID of the updated <a>Address</a> object.</p>"""
    shipping_option: NotRequired[
        "aws_sdk_snowball.types.shipping_option.ShippingOption"
    ]
    """<p>The updated shipping option value of this job's <a>ShippingDetails</a> object.</p>"""
    description: NotRequired["aws_sdk_snowball.types.string.String"]
    """<p>The updated description of this job's <a>JobMetadata</a> object.</p>"""
    snowball_capacity_preference: NotRequired[
        "aws_sdk_snowball.types.snowball_capacity.SnowballCapacity"
    ]
    """<p>The updated <code>SnowballCapacityPreference</code> of this job's <a>JobMetadata</a> object. The 50 TB Snowballs are only available in the US regions.</p> <p>For more information, see \"https://docs.aws.amazon.com/snowball/latest/snowcone-guide/snow-device-types.html\" (Snow Family Devices and Capacity) in the <i>Snowcone User Guide</i> or \"https://docs.aws.amazon.com/snowball/latest/developer-guide/snow-device-types.html\" (Snow Family Devices and Capacity) in the <i>Snowcone User Guide</i>.</p>"""
    forwarding_address_id: NotRequired["aws_sdk_snowball.types.address_id.AddressId"]
    """<p>The updated ID for the forwarding address for a job. This field is not supported in most regions.</p>"""
    pickup_details: NotRequired["aws_sdk_snowball.types.pickup_details.PickupDetails"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateJobRequest) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    if "role_arn" in value:
        out["RoleARN"] = value["role_arn"]
    if "notification" in value:
        import aws_sdk_snowball.types.notification

        out["Notification"] = (
            aws_sdk_snowball.types.notification.serialize_aws_json_1_1(
                value["notification"]
            )
        )
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
    if "description" in value:
        out["Description"] = value["description"]
    if "snowball_capacity_preference" in value:
        import aws_sdk_snowball.types.snowball_capacity

        out["SnowballCapacityPreference"] = (
            aws_sdk_snowball.types.snowball_capacity.serialize_aws_json_1_1(
                value["snowball_capacity_preference"]
            )
        )
    if "forwarding_address_id" in value:
        out["ForwardingAddressId"] = value["forwarding_address_id"]
    if "pickup_details" in value:
        import aws_sdk_snowball.types.pickup_details

        out["PickupDetails"] = (
            aws_sdk_snowball.types.pickup_details.serialize_aws_json_1_1(
                value["pickup_details"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateJobRequest:
    out: UpdateJobRequest = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    else:
        raise DeserializationError("UpdateJobRequest.job_id required")
    if "RoleARN" in data:
        out["role_arn"] = data["RoleARN"]
    if "Notification" in data:
        import aws_sdk_snowball.types.notification

        out["notification"] = (
            aws_sdk_snowball.types.notification.deserialize_aws_json_1_1(
                data["Notification"]
            )
        )
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
    if "Description" in data:
        out["description"] = data["Description"]
    if "SnowballCapacityPreference" in data:
        import aws_sdk_snowball.types.snowball_capacity

        out["snowball_capacity_preference"] = (
            aws_sdk_snowball.types.snowball_capacity.deserialize_aws_json_1_1(
                data["SnowballCapacityPreference"]
            )
        )
    if "ForwardingAddressId" in data:
        out["forwarding_address_id"] = data["ForwardingAddressId"]
    if "PickupDetails" in data:
        import aws_sdk_snowball.types.pickup_details

        out["pickup_details"] = (
            aws_sdk_snowball.types.pickup_details.deserialize_aws_json_1_1(
                data["PickupDetails"]
            )
        )
    return out
