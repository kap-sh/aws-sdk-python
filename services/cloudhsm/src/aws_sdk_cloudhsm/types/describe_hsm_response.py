"""Generated from Smithy shape ``com.amazonaws.cloudhsm#DescribeHsmResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudhsm.types.az
    import aws_sdk_cloudhsm.types.eni_id
    import aws_sdk_cloudhsm.types.hsm_arn
    import aws_sdk_cloudhsm.types.hsm_serial_number
    import aws_sdk_cloudhsm.types.hsm_status
    import aws_sdk_cloudhsm.types.iam_role_arn
    import aws_sdk_cloudhsm.types.ip_address
    import aws_sdk_cloudhsm.types.partition_list
    import aws_sdk_cloudhsm.types.ssh_key
    import aws_sdk_cloudhsm.types.string
    import aws_sdk_cloudhsm.types.subnet_id
    import aws_sdk_cloudhsm.types.subscription_type
    import aws_sdk_cloudhsm.types.timestamp
    import aws_sdk_cloudhsm.types.vpc_id


class DescribeHsmResponse(TypedDict, closed=True):
    hsm_arn: NotRequired["aws_sdk_cloudhsm.types.hsm_arn.HsmArn"]
    """<p>The ARN of the HSM.</p>"""
    status: NotRequired["aws_sdk_cloudhsm.types.hsm_status.HsmStatus"]
    """<p>The status of the HSM.</p>"""
    status_details: NotRequired["aws_sdk_cloudhsm.types.string.String"]
    """<p>Contains additional information about the status of the HSM.</p>"""
    availability_zone: NotRequired["aws_sdk_cloudhsm.types.az.AZ"]
    """<p>The Availability Zone that the HSM is in.</p>"""
    eni_id: NotRequired["aws_sdk_cloudhsm.types.eni_id.EniId"]
    """<p>The identifier of the elastic network interface (ENI) attached to the HSM.</p>"""
    eni_ip: NotRequired["aws_sdk_cloudhsm.types.ip_address.IpAddress"]
    """<p>The IP address assigned to the HSM's ENI.</p>"""
    subscription_type: NotRequired[
        "aws_sdk_cloudhsm.types.subscription_type.SubscriptionType"
    ]
    subscription_start_date: NotRequired["aws_sdk_cloudhsm.types.timestamp.Timestamp"]
    """<p>The subscription start date.</p>"""
    subscription_end_date: NotRequired["aws_sdk_cloudhsm.types.timestamp.Timestamp"]
    """<p>The subscription end date.</p>"""
    vpc_id: NotRequired["aws_sdk_cloudhsm.types.vpc_id.VpcId"]
    """<p>The identifier of the VPC that the HSM is in.</p>"""
    subnet_id: NotRequired["aws_sdk_cloudhsm.types.subnet_id.SubnetId"]
    """<p>The identifier of the subnet that the HSM is in.</p>"""
    iam_role_arn: NotRequired["aws_sdk_cloudhsm.types.iam_role_arn.IamRoleArn"]
    """<p>The ARN of the IAM role assigned to the HSM.</p>"""
    serial_number: NotRequired[
        "aws_sdk_cloudhsm.types.hsm_serial_number.HsmSerialNumber"
    ]
    """<p>The serial number of the HSM.</p>"""
    vendor_name: NotRequired["aws_sdk_cloudhsm.types.string.String"]
    """<p>The name of the HSM vendor.</p>"""
    hsm_type: NotRequired["aws_sdk_cloudhsm.types.string.String"]
    """<p>The HSM model type.</p>"""
    software_version: NotRequired["aws_sdk_cloudhsm.types.string.String"]
    """<p>The HSM software version.</p>"""
    ssh_public_key: NotRequired["aws_sdk_cloudhsm.types.ssh_key.SshKey"]
    """<p>The public SSH key.</p>"""
    ssh_key_last_updated: NotRequired["aws_sdk_cloudhsm.types.timestamp.Timestamp"]
    """<p>The date and time that the SSH key was last updated.</p>"""
    server_cert_uri: NotRequired["aws_sdk_cloudhsm.types.string.String"]
    """<p>The URI of the certificate server.</p>"""
    server_cert_last_updated: NotRequired["aws_sdk_cloudhsm.types.timestamp.Timestamp"]
    """<p>The date and time that the server certificate was last updated.</p>"""
    partitions: NotRequired["aws_sdk_cloudhsm.types.partition_list.PartitionList"]
    """<p>The list of partitions on the HSM.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeHsmResponse) -> dict:
    out: dict = {}
    if "hsm_arn" in value:
        out["HsmArn"] = value["hsm_arn"]
    if "status" in value:
        import aws_sdk_cloudhsm.types.hsm_status

        out["Status"] = aws_sdk_cloudhsm.types.hsm_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "status_details" in value:
        out["StatusDetails"] = value["status_details"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "eni_id" in value:
        out["EniId"] = value["eni_id"]
    if "eni_ip" in value:
        out["EniIp"] = value["eni_ip"]
    if "subscription_type" in value:
        import aws_sdk_cloudhsm.types.subscription_type

        out["SubscriptionType"] = (
            aws_sdk_cloudhsm.types.subscription_type.serialize_aws_json_1_1(
                value["subscription_type"]
            )
        )
    if "subscription_start_date" in value:
        out["SubscriptionStartDate"] = value["subscription_start_date"]
    if "subscription_end_date" in value:
        out["SubscriptionEndDate"] = value["subscription_end_date"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "subnet_id" in value:
        out["SubnetId"] = value["subnet_id"]
    if "iam_role_arn" in value:
        out["IamRoleArn"] = value["iam_role_arn"]
    if "serial_number" in value:
        out["SerialNumber"] = value["serial_number"]
    if "vendor_name" in value:
        out["VendorName"] = value["vendor_name"]
    if "hsm_type" in value:
        out["HsmType"] = value["hsm_type"]
    if "software_version" in value:
        out["SoftwareVersion"] = value["software_version"]
    if "ssh_public_key" in value:
        out["SshPublicKey"] = value["ssh_public_key"]
    if "ssh_key_last_updated" in value:
        out["SshKeyLastUpdated"] = value["ssh_key_last_updated"]
    if "server_cert_uri" in value:
        out["ServerCertUri"] = value["server_cert_uri"]
    if "server_cert_last_updated" in value:
        out["ServerCertLastUpdated"] = value["server_cert_last_updated"]
    if "partitions" in value:
        import aws_sdk_cloudhsm.types.partition_list

        out["Partitions"] = (
            aws_sdk_cloudhsm.types.partition_list.serialize_aws_json_1_1(
                value["partitions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeHsmResponse:
    out: DescribeHsmResponse = {}  # type: ignore[typeddict-item]
    if "HsmArn" in data:
        out["hsm_arn"] = data["HsmArn"]
    if "Status" in data:
        import aws_sdk_cloudhsm.types.hsm_status

        out["status"] = aws_sdk_cloudhsm.types.hsm_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "StatusDetails" in data:
        out["status_details"] = data["StatusDetails"]
    if "AvailabilityZone" in data:
        out["availability_zone"] = data["AvailabilityZone"]
    if "EniId" in data:
        out["eni_id"] = data["EniId"]
    if "EniIp" in data:
        out["eni_ip"] = data["EniIp"]
    if "SubscriptionType" in data:
        import aws_sdk_cloudhsm.types.subscription_type

        out["subscription_type"] = (
            aws_sdk_cloudhsm.types.subscription_type.deserialize_aws_json_1_1(
                data["SubscriptionType"]
            )
        )
    if "SubscriptionStartDate" in data:
        out["subscription_start_date"] = data["SubscriptionStartDate"]
    if "SubscriptionEndDate" in data:
        out["subscription_end_date"] = data["SubscriptionEndDate"]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "SubnetId" in data:
        out["subnet_id"] = data["SubnetId"]
    if "IamRoleArn" in data:
        out["iam_role_arn"] = data["IamRoleArn"]
    if "SerialNumber" in data:
        out["serial_number"] = data["SerialNumber"]
    if "VendorName" in data:
        out["vendor_name"] = data["VendorName"]
    if "HsmType" in data:
        out["hsm_type"] = data["HsmType"]
    if "SoftwareVersion" in data:
        out["software_version"] = data["SoftwareVersion"]
    if "SshPublicKey" in data:
        out["ssh_public_key"] = data["SshPublicKey"]
    if "SshKeyLastUpdated" in data:
        out["ssh_key_last_updated"] = data["SshKeyLastUpdated"]
    if "ServerCertUri" in data:
        out["server_cert_uri"] = data["ServerCertUri"]
    if "ServerCertLastUpdated" in data:
        out["server_cert_last_updated"] = data["ServerCertLastUpdated"]
    if "Partitions" in data:
        import aws_sdk_cloudhsm.types.partition_list

        out["partitions"] = (
            aws_sdk_cloudhsm.types.partition_list.deserialize_aws_json_1_1(
                data["Partitions"]
            )
        )
    return out
