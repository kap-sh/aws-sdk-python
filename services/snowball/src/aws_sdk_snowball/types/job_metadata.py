"""Generated from Smithy shape ``com.amazonaws.snowball#JobMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_snowball.types.address_id
    import aws_sdk_snowball.types.data_transfer
    import aws_sdk_snowball.types.device_configuration
    import aws_sdk_snowball.types.impact_level
    import aws_sdk_snowball.types.job_logs
    import aws_sdk_snowball.types.job_resource
    import aws_sdk_snowball.types.job_state
    import aws_sdk_snowball.types.job_type
    import aws_sdk_snowball.types.kms_key_arn
    import aws_sdk_snowball.types.long_term_pricing_id
    import aws_sdk_snowball.types.notification
    import aws_sdk_snowball.types.on_device_service_configuration
    import aws_sdk_snowball.types.pickup_details
    import aws_sdk_snowball.types.remote_management
    import aws_sdk_snowball.types.role_arn
    import aws_sdk_snowball.types.shipping_details
    import aws_sdk_snowball.types.snowball_capacity
    import aws_sdk_snowball.types.snowball_type
    import aws_sdk_snowball.types.string
    import aws_sdk_snowball.types.tax_documents
    import aws_sdk_snowball.types.timestamp


class JobMetadata(TypedDict):
    job_id: NotRequired["aws_sdk_snowball.types.string.String"]
    """<p>The automatically generated ID for a job, for example <code>JID123e4567-e89b-12d3-a456-426655440000</code>.</p>"""
    job_state: NotRequired["aws_sdk_snowball.types.job_state.JobState"]
    """<p>The current status of the jobs.</p>"""
    job_type: NotRequired["aws_sdk_snowball.types.job_type.JobType"]
    """<p>The type of job.</p>"""
    snowball_type: NotRequired["aws_sdk_snowball.types.snowball_type.SnowballType"]
    """<p>The type of device used with this job.</p>"""
    creation_date: NotRequired["aws_sdk_snowball.types.timestamp.Timestamp"]
    """<p>The creation date for this job.</p>"""
    resources: NotRequired["aws_sdk_snowball.types.job_resource.JobResource"]
    """<p>An array of <code>S3Resource</code> objects. Each <code>S3Resource</code> object represents an Amazon S3 bucket that your transferred data will be exported from or imported into.</p>"""
    description: NotRequired["aws_sdk_snowball.types.string.String"]
    """<p>The description of the job, provided at job creation.</p>"""
    kms_key_arn: NotRequired["aws_sdk_snowball.types.kms_key_arn.KmsKeyARN"]
    r"""<p>The Amazon Resource Name (ARN) for the Key Management Service (KMS) key associated with this job. This ARN was created using the <a href=\"https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html\">CreateKey</a> API action in KMS.</p>"""
    role_arn: NotRequired["aws_sdk_snowball.types.role_arn.RoleARN"]
    r"""<p>The role ARN associated with this job. This ARN was created using the <a href=\"https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateRole.html\">CreateRole</a> API action in Identity and Access Management.</p>"""
    address_id: NotRequired["aws_sdk_snowball.types.address_id.AddressId"]
    """<p>The ID for the address that you want the Snow device shipped to.</p>"""
    shipping_details: NotRequired[
        "aws_sdk_snowball.types.shipping_details.ShippingDetails"
    ]
    """<p>A job's shipping information, including inbound and outbound tracking numbers and shipping speed options.</p>"""
    snowball_capacity_preference: NotRequired[
        "aws_sdk_snowball.types.snowball_capacity.SnowballCapacity"
    ]
    r"""<p>The Snow device capacity preference for this job, specified at job creation. In US regions, you can choose between 50 TB and 80 TB Snowballs. All other regions use 80 TB capacity Snowballs.</p> <p>For more information, see \"https://docs.aws.amazon.com/snowball/latest/snowcone-guide/snow-device-types.html\" (Snow Family Devices and Capacity) in the <i>Snowcone User Guide</i> or \"https://docs.aws.amazon.com/snowball/latest/developer-guide/snow-device-types.html\" (Snow Family Devices and Capacity) in the <i>Snowcone User Guide</i>.</p>"""
    notification: NotRequired["aws_sdk_snowball.types.notification.Notification"]
    """<p>The Amazon Simple Notification Service (Amazon SNS) notification settings associated with a specific job. The <code>Notification</code> object is returned as a part of the response syntax of the <code>DescribeJob</code> action in the <code>JobMetadata</code> data type.</p>"""
    data_transfer_progress: NotRequired[
        "aws_sdk_snowball.types.data_transfer.DataTransfer"
    ]
    """<p>A value that defines the real-time status of a Snow device's data transfer while the device is at Amazon Web Services. This data is only available while a job has a <code>JobState</code> value of <code>InProgress</code>, for both import and export jobs.</p>"""
    job_log_info: NotRequired["aws_sdk_snowball.types.job_logs.JobLogs"]
    """<p>Links to Amazon S3 presigned URLs for the job report and logs. For import jobs, the PDF job report becomes available at the end of the import process. For export jobs, your job report typically becomes available while the Snow device for your job part is being delivered to you.</p>"""
    cluster_id: NotRequired["aws_sdk_snowball.types.string.String"]
    """<p>The 39-character ID for the cluster, for example <code>CID123e4567-e89b-12d3-a456-426655440000</code>.</p>"""
    forwarding_address_id: NotRequired["aws_sdk_snowball.types.address_id.AddressId"]
    """<p>The ID of the address that you want a job shipped to, after it will be shipped to its primary address. This field is not supported in most regions.</p>"""
    tax_documents: NotRequired["aws_sdk_snowball.types.tax_documents.TaxDocuments"]
    """<p>The metadata associated with the tax documents required in your Amazon Web Services Region.</p>"""
    device_configuration: NotRequired[
        "aws_sdk_snowball.types.device_configuration.DeviceConfiguration"
    ]
    remote_management: NotRequired[
        "aws_sdk_snowball.types.remote_management.RemoteManagement"
    ]
    """<p>Allows you to securely operate and manage Snowcone devices remotely from outside of your internal network. When set to <code>INSTALLED_AUTOSTART</code>, remote management will automatically be available when the device arrives at your location. Otherwise, you need to use the Snowball Client to manage the device.</p>"""
    long_term_pricing_id: NotRequired[
        "aws_sdk_snowball.types.long_term_pricing_id.LongTermPricingId"
    ]
    """<p>The ID of the long-term pricing type for the device.</p>"""
    on_device_service_configuration: NotRequired[
        "aws_sdk_snowball.types.on_device_service_configuration.OnDeviceServiceConfiguration"
    ]
    """<p>Represents metadata and configuration settings for services on an Amazon Web Services Snow Family device.</p>"""
    impact_level: NotRequired["aws_sdk_snowball.types.impact_level.ImpactLevel"]
    """<p>The highest impact level of data that will be stored or processed on the device, provided at job creation.</p>"""
    pickup_details: NotRequired["aws_sdk_snowball.types.pickup_details.PickupDetails"]
    """<p>Information identifying the person picking up the device.</p>"""
    snowball_id: NotRequired["aws_sdk_snowball.types.string.String"]
    """<p>Unique ID associated with a device.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobMetadata) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "job_state" in value:
        import aws_sdk_snowball.types.job_state

        out["JobState"] = aws_sdk_snowball.types.job_state.serialize_aws_json_1_1(
            value["job_state"]
        )
    if "job_type" in value:
        import aws_sdk_snowball.types.job_type

        out["JobType"] = aws_sdk_snowball.types.job_type.serialize_aws_json_1_1(
            value["job_type"]
        )
    if "snowball_type" in value:
        import aws_sdk_snowball.types.snowball_type

        out["SnowballType"] = (
            aws_sdk_snowball.types.snowball_type.serialize_aws_json_1_1(
                value["snowball_type"]
            )
        )
    if "creation_date" in value:
        import aws_sdk_snowball.types.timestamp

        out["CreationDate"] = aws_sdk_snowball.types.timestamp.serialize_aws_json_1_1(
            value["creation_date"]
        )
    if "resources" in value:
        import aws_sdk_snowball.types.job_resource

        out["Resources"] = aws_sdk_snowball.types.job_resource.serialize_aws_json_1_1(
            value["resources"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "kms_key_arn" in value:
        out["KmsKeyARN"] = value["kms_key_arn"]
    if "role_arn" in value:
        out["RoleARN"] = value["role_arn"]
    if "address_id" in value:
        out["AddressId"] = value["address_id"]
    if "shipping_details" in value:
        import aws_sdk_snowball.types.shipping_details

        out["ShippingDetails"] = (
            aws_sdk_snowball.types.shipping_details.serialize_aws_json_1_1(
                value["shipping_details"]
            )
        )
    if "snowball_capacity_preference" in value:
        import aws_sdk_snowball.types.snowball_capacity

        out["SnowballCapacityPreference"] = (
            aws_sdk_snowball.types.snowball_capacity.serialize_aws_json_1_1(
                value["snowball_capacity_preference"]
            )
        )
    if "notification" in value:
        import aws_sdk_snowball.types.notification

        out["Notification"] = (
            aws_sdk_snowball.types.notification.serialize_aws_json_1_1(
                value["notification"]
            )
        )
    if "data_transfer_progress" in value:
        import aws_sdk_snowball.types.data_transfer

        out["DataTransferProgress"] = (
            aws_sdk_snowball.types.data_transfer.serialize_aws_json_1_1(
                value["data_transfer_progress"]
            )
        )
    if "job_log_info" in value:
        import aws_sdk_snowball.types.job_logs

        out["JobLogInfo"] = aws_sdk_snowball.types.job_logs.serialize_aws_json_1_1(
            value["job_log_info"]
        )
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    if "forwarding_address_id" in value:
        out["ForwardingAddressId"] = value["forwarding_address_id"]
    if "tax_documents" in value:
        import aws_sdk_snowball.types.tax_documents

        out["TaxDocuments"] = (
            aws_sdk_snowball.types.tax_documents.serialize_aws_json_1_1(
                value["tax_documents"]
            )
        )
    if "device_configuration" in value:
        import aws_sdk_snowball.types.device_configuration

        out["DeviceConfiguration"] = (
            aws_sdk_snowball.types.device_configuration.serialize_aws_json_1_1(
                value["device_configuration"]
            )
        )
    if "remote_management" in value:
        import aws_sdk_snowball.types.remote_management

        out["RemoteManagement"] = (
            aws_sdk_snowball.types.remote_management.serialize_aws_json_1_1(
                value["remote_management"]
            )
        )
    if "long_term_pricing_id" in value:
        out["LongTermPricingId"] = value["long_term_pricing_id"]
    if "on_device_service_configuration" in value:
        import aws_sdk_snowball.types.on_device_service_configuration

        out["OnDeviceServiceConfiguration"] = (
            aws_sdk_snowball.types.on_device_service_configuration.serialize_aws_json_1_1(
                value["on_device_service_configuration"]
            )
        )
    if "impact_level" in value:
        import aws_sdk_snowball.types.impact_level

        out["ImpactLevel"] = aws_sdk_snowball.types.impact_level.serialize_aws_json_1_1(
            value["impact_level"]
        )
    if "pickup_details" in value:
        import aws_sdk_snowball.types.pickup_details

        out["PickupDetails"] = (
            aws_sdk_snowball.types.pickup_details.serialize_aws_json_1_1(
                value["pickup_details"]
            )
        )
    if "snowball_id" in value:
        out["SnowballId"] = value["snowball_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> JobMetadata:
    out: JobMetadata = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    if "JobState" in data:
        import aws_sdk_snowball.types.job_state

        out["job_state"] = aws_sdk_snowball.types.job_state.deserialize_aws_json_1_1(
            data["JobState"]
        )
    if "JobType" in data:
        import aws_sdk_snowball.types.job_type

        out["job_type"] = aws_sdk_snowball.types.job_type.deserialize_aws_json_1_1(
            data["JobType"]
        )
    if "SnowballType" in data:
        import aws_sdk_snowball.types.snowball_type

        out["snowball_type"] = (
            aws_sdk_snowball.types.snowball_type.deserialize_aws_json_1_1(
                data["SnowballType"]
            )
        )
    if "CreationDate" in data:
        import aws_sdk_snowball.types.timestamp

        out["creation_date"] = (
            aws_sdk_snowball.types.timestamp.deserialize_aws_json_1_1(
                data["CreationDate"]
            )
        )
    if "Resources" in data:
        import aws_sdk_snowball.types.job_resource

        out["resources"] = aws_sdk_snowball.types.job_resource.deserialize_aws_json_1_1(
            data["Resources"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "KmsKeyARN" in data:
        out["kms_key_arn"] = data["KmsKeyARN"]
    if "RoleARN" in data:
        out["role_arn"] = data["RoleARN"]
    if "AddressId" in data:
        out["address_id"] = data["AddressId"]
    if "ShippingDetails" in data:
        import aws_sdk_snowball.types.shipping_details

        out["shipping_details"] = (
            aws_sdk_snowball.types.shipping_details.deserialize_aws_json_1_1(
                data["ShippingDetails"]
            )
        )
    if "SnowballCapacityPreference" in data:
        import aws_sdk_snowball.types.snowball_capacity

        out["snowball_capacity_preference"] = (
            aws_sdk_snowball.types.snowball_capacity.deserialize_aws_json_1_1(
                data["SnowballCapacityPreference"]
            )
        )
    if "Notification" in data:
        import aws_sdk_snowball.types.notification

        out["notification"] = (
            aws_sdk_snowball.types.notification.deserialize_aws_json_1_1(
                data["Notification"]
            )
        )
    if "DataTransferProgress" in data:
        import aws_sdk_snowball.types.data_transfer

        out["data_transfer_progress"] = (
            aws_sdk_snowball.types.data_transfer.deserialize_aws_json_1_1(
                data["DataTransferProgress"]
            )
        )
    if "JobLogInfo" in data:
        import aws_sdk_snowball.types.job_logs

        out["job_log_info"] = aws_sdk_snowball.types.job_logs.deserialize_aws_json_1_1(
            data["JobLogInfo"]
        )
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    if "ForwardingAddressId" in data:
        out["forwarding_address_id"] = data["ForwardingAddressId"]
    if "TaxDocuments" in data:
        import aws_sdk_snowball.types.tax_documents

        out["tax_documents"] = (
            aws_sdk_snowball.types.tax_documents.deserialize_aws_json_1_1(
                data["TaxDocuments"]
            )
        )
    if "DeviceConfiguration" in data:
        import aws_sdk_snowball.types.device_configuration

        out["device_configuration"] = (
            aws_sdk_snowball.types.device_configuration.deserialize_aws_json_1_1(
                data["DeviceConfiguration"]
            )
        )
    if "RemoteManagement" in data:
        import aws_sdk_snowball.types.remote_management

        out["remote_management"] = (
            aws_sdk_snowball.types.remote_management.deserialize_aws_json_1_1(
                data["RemoteManagement"]
            )
        )
    if "LongTermPricingId" in data:
        out["long_term_pricing_id"] = data["LongTermPricingId"]
    if "OnDeviceServiceConfiguration" in data:
        import aws_sdk_snowball.types.on_device_service_configuration

        out["on_device_service_configuration"] = (
            aws_sdk_snowball.types.on_device_service_configuration.deserialize_aws_json_1_1(
                data["OnDeviceServiceConfiguration"]
            )
        )
    if "ImpactLevel" in data:
        import aws_sdk_snowball.types.impact_level

        out["impact_level"] = (
            aws_sdk_snowball.types.impact_level.deserialize_aws_json_1_1(
                data["ImpactLevel"]
            )
        )
    if "PickupDetails" in data:
        import aws_sdk_snowball.types.pickup_details

        out["pickup_details"] = (
            aws_sdk_snowball.types.pickup_details.deserialize_aws_json_1_1(
                data["PickupDetails"]
            )
        )
    if "SnowballId" in data:
        out["snowball_id"] = data["SnowballId"]
    return out
