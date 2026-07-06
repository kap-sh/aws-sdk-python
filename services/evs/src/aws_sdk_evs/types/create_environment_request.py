"""Generated from Smithy shape ``com.amazonaws.evs#CreateEnvironmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_evs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_evs.types.client_token
    import aws_sdk_evs.types.connectivity_info
    import aws_sdk_evs.types.environment_name
    import aws_sdk_evs.types.host_info_for_create_list
    import aws_sdk_evs.types.initial_vlans
    import aws_sdk_evs.types.license_info_list
    import aws_sdk_evs.types.request_tag_map
    import aws_sdk_evs.types.service_access_security_groups
    import aws_sdk_evs.types.subnet_id
    import aws_sdk_evs.types.vcf_hostnames
    import aws_sdk_evs.types.vcf_version
    import aws_sdk_evs.types.vpc_id


class CreateEnvironmentRequest(TypedDict, closed=True):
    client_token: NotRequired["aws_sdk_evs.types.client_token.ClientToken"]
    """<note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the environment creation request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>"""
    environment_name: NotRequired["aws_sdk_evs.types.environment_name.EnvironmentName"]
    """<p>The name to give to your environment. The name can contain only alphanumeric characters (case-sensitive), hyphens, and underscores. It must start with an alphanumeric character, and can't be longer than 100 characters. The name must be unique within the Amazon Web Services Region and Amazon Web Services account that you're creating the environment in.</p>"""
    kms_key_id: NotRequired["str"]
    """<p>A unique ID for the customer-managed KMS key that is used to encrypt the VCF credential pairs for SDDC Manager, NSX Manager, and vCenter appliances. These credentials are stored in Amazon Web Services Secrets Manager.</p>"""
    tags: NotRequired["aws_sdk_evs.types.request_tag_map.RequestTagMap"]
    """<p>Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or Amazon Web Services resources.</p>"""
    service_access_security_groups: NotRequired[
        "aws_sdk_evs.types.service_access_security_groups.ServiceAccessSecurityGroups"
    ]
    """<p>The security group that controls communication between the Amazon EVS control plane and VPC. The default security group is used if a custom security group isn't specified.</p> <p>The security group should allow access to the following.</p> <ul> <li> <p>TCP/UDP access to the DNS servers</p> </li> <li> <p>HTTPS/SSH access to the host management VLAN subnet</p> </li> <li> <p>HTTPS/SSH access to the Management VM VLAN subnet</p> </li> </ul> <p>You should avoid modifying the security group rules after deployment, as this can break the persistent connection between the Amazon EVS control plane and VPC. This can cause future environment actions like adding or removing hosts to fail.</p>"""
    vpc_id: "aws_sdk_evs.types.vpc_id.VpcId"
    """<p>A unique ID for the VPC that the environment is deployed inside.</p> <p>Amazon EVS requires that all VPC subnets exist in a single Availability Zone in a Region where the service is available.</p> <p>The VPC that you specify must have a valid DHCP option set with domain name, at least two DNS servers, and an NTP server. These settings are used to configure your VCF appliances and hosts. The VPC cannot be used with any other deployed Amazon EVS environment. Amazon EVS does not provide multi-VPC support for environments at this time.</p> <p>Amazon EVS does not support the following Amazon Web Services networking options for NSX overlay connectivity: cross-Region VPC peering, Amazon S3 gateway endpoints, or Amazon Web Services Direct Connect virtual private gateway associations.</p> <note> <p>Ensure that you specify a VPC that is adequately sized to accommodate the Amazon EVS subnets.</p> </note>"""
    service_access_subnet_id: "aws_sdk_evs.types.subnet_id.SubnetId"
    """<p>The subnet that is used to establish connectivity between the Amazon EVS control plane and VPC. Amazon EVS uses this subnet to validate mandatory DNS records for your VCF appliances and hosts and create the environment.</p>"""
    vcf_version: "aws_sdk_evs.types.vcf_version.VcfVersion"
    """<p> The VCF version to use for the environment.</p>"""
    terms_accepted: "bool"
    """<p>Customer confirmation that the customer has purchased and will continue to maintain the required number of VCF software licenses to cover all physical processor cores in the Amazon EVS environment. Information about your VCF software in Amazon EVS will be shared with Broadcom to verify license compliance. Amazon EVS does not validate license keys. To validate license keys, visit the Broadcom support portal.</p>"""
    license_info: "aws_sdk_evs.types.license_info_list.LicenseInfoList"
    r"""<p>The license information that Amazon EVS requires to create an environment. Amazon EVS requires two license keys: a VCF solution key and a vSAN license key. The VCF solution key must meet minimum core requirements, and the vSAN license key must meet minimum capacity requirements for your selected instance type.</p> <p>For information about minimum license requirements, see <a href=\"https://docs.aws.amazon.com/evs/latest/userguide/vcf-license-mgmt.html\">the VCF subscriptions section</a> in the <i>Amazon EVS User Guide</i>.</p> <p>VCF licenses can be used for only one Amazon EVS environment. Amazon EVS does not support reuse of VCF licenses for multiple environments.</p> <p>VCF license information can be retrieved from the Broadcom portal.</p>"""
    initial_vlans: "aws_sdk_evs.types.initial_vlans.InitialVlans"
    """<p>The initial VLAN subnets for the Amazon EVS environment.</p> <note> <p>For each Amazon EVS VLAN subnet, you must specify a non-overlapping CIDR block. Amazon EVS VLAN subnets have a minimum CIDR block size of /28 and a maximum size of /24.</p> </note>"""
    hosts: "aws_sdk_evs.types.host_info_for_create_list.HostInfoForCreateList"
    """<p>The ESX hosts to add to the environment. Amazon EVS requires that you provide details for a minimum of 4 hosts during environment creation.</p> <p>For each host, you must provide the desired hostname, EC2 SSH keypair name, and EC2 instance type. Optionally, you can also provide a partition or cluster placement group to use, or use Amazon EC2 Dedicated Hosts.</p>"""
    connectivity_info: "aws_sdk_evs.types.connectivity_info.ConnectivityInfo"
    """<p> The connectivity configuration for the environment. Amazon EVS requires that you specify two route server peer IDs. During environment creation, the route server endpoints peer with the NSX edges over the NSX uplink subnet, providing BGP-based dynamic routing for overlay networks.</p>"""
    vcf_hostnames: "aws_sdk_evs.types.vcf_hostnames.VcfHostnames"
    """<p>The DNS hostnames for the virtual machines that host the VCF management appliances. Amazon EVS requires that you provide DNS hostnames for the following appliances: vCenter, NSX Manager, SDDC Manager, and Cloud Builder.</p>"""
    site_id: "str"
    """<p>The Broadcom Site ID that is allocated to you as part of your electronic software delivery. This ID allows customer access to the Broadcom portal, and is provided to you by Broadcom at the close of your software contract or contract renewal. Amazon EVS uses the Broadcom Site ID that you provide to meet Broadcom VCF license usage reporting requirements for Amazon EVS.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateEnvironmentRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "environment_name" in value:
        out["environmentName"] = value["environment_name"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "tags" in value:
        import aws_sdk_evs.types.request_tag_map

        out["tags"] = aws_sdk_evs.types.request_tag_map.serialize_aws_json_1_0(
            value["tags"]
        )
    if "service_access_security_groups" in value:
        import aws_sdk_evs.types.service_access_security_groups

        out["serviceAccessSecurityGroups"] = (
            aws_sdk_evs.types.service_access_security_groups.serialize_aws_json_1_0(
                value["service_access_security_groups"]
            )
        )
    out["vpcId"] = value["vpc_id"]
    out["serviceAccessSubnetId"] = value["service_access_subnet_id"]
    import aws_sdk_evs.types.vcf_version

    out["vcfVersion"] = aws_sdk_evs.types.vcf_version.serialize_aws_json_1_0(
        value["vcf_version"]
    )
    out["termsAccepted"] = value["terms_accepted"]
    import aws_sdk_evs.types.license_info_list

    out["licenseInfo"] = aws_sdk_evs.types.license_info_list.serialize_aws_json_1_0(
        value["license_info"]
    )
    import aws_sdk_evs.types.initial_vlans

    out["initialVlans"] = aws_sdk_evs.types.initial_vlans.serialize_aws_json_1_0(
        value["initial_vlans"]
    )
    import aws_sdk_evs.types.host_info_for_create_list

    out["hosts"] = aws_sdk_evs.types.host_info_for_create_list.serialize_aws_json_1_0(
        value["hosts"]
    )
    import aws_sdk_evs.types.connectivity_info

    out["connectivityInfo"] = (
        aws_sdk_evs.types.connectivity_info.serialize_aws_json_1_0(
            value["connectivity_info"]
        )
    )
    import aws_sdk_evs.types.vcf_hostnames

    out["vcfHostnames"] = aws_sdk_evs.types.vcf_hostnames.serialize_aws_json_1_0(
        value["vcf_hostnames"]
    )
    out["siteId"] = value["site_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateEnvironmentRequest:
    out: CreateEnvironmentRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "environmentName" in data:
        out["environment_name"] = data["environmentName"]
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "tags" in data:
        import aws_sdk_evs.types.request_tag_map

        out["tags"] = aws_sdk_evs.types.request_tag_map.deserialize_aws_json_1_0(
            data["tags"]
        )
    if "serviceAccessSecurityGroups" in data:
        import aws_sdk_evs.types.service_access_security_groups

        out["service_access_security_groups"] = (
            aws_sdk_evs.types.service_access_security_groups.deserialize_aws_json_1_0(
                data["serviceAccessSecurityGroups"]
            )
        )
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    else:
        raise DeserializationError("CreateEnvironmentRequest.vpc_id required")
    if "serviceAccessSubnetId" in data:
        out["service_access_subnet_id"] = data["serviceAccessSubnetId"]
    else:
        raise DeserializationError(
            "CreateEnvironmentRequest.service_access_subnet_id required"
        )
    if "vcfVersion" in data:
        import aws_sdk_evs.types.vcf_version

        out["vcf_version"] = aws_sdk_evs.types.vcf_version.deserialize_aws_json_1_0(
            data["vcfVersion"]
        )
    else:
        raise DeserializationError("CreateEnvironmentRequest.vcf_version required")
    if "termsAccepted" in data:
        out["terms_accepted"] = data["termsAccepted"]
    else:
        raise DeserializationError("CreateEnvironmentRequest.terms_accepted required")
    if "licenseInfo" in data:
        import aws_sdk_evs.types.license_info_list

        out["license_info"] = (
            aws_sdk_evs.types.license_info_list.deserialize_aws_json_1_0(
                data["licenseInfo"]
            )
        )
    else:
        raise DeserializationError("CreateEnvironmentRequest.license_info required")
    if "initialVlans" in data:
        import aws_sdk_evs.types.initial_vlans

        out["initial_vlans"] = aws_sdk_evs.types.initial_vlans.deserialize_aws_json_1_0(
            data["initialVlans"]
        )
    else:
        raise DeserializationError("CreateEnvironmentRequest.initial_vlans required")
    if "hosts" in data:
        import aws_sdk_evs.types.host_info_for_create_list

        out["hosts"] = (
            aws_sdk_evs.types.host_info_for_create_list.deserialize_aws_json_1_0(
                data["hosts"]
            )
        )
    else:
        raise DeserializationError("CreateEnvironmentRequest.hosts required")
    if "connectivityInfo" in data:
        import aws_sdk_evs.types.connectivity_info

        out["connectivity_info"] = (
            aws_sdk_evs.types.connectivity_info.deserialize_aws_json_1_0(
                data["connectivityInfo"]
            )
        )
    else:
        raise DeserializationError(
            "CreateEnvironmentRequest.connectivity_info required"
        )
    if "vcfHostnames" in data:
        import aws_sdk_evs.types.vcf_hostnames

        out["vcf_hostnames"] = aws_sdk_evs.types.vcf_hostnames.deserialize_aws_json_1_0(
            data["vcfHostnames"]
        )
    else:
        raise DeserializationError("CreateEnvironmentRequest.vcf_hostnames required")
    if "siteId" in data:
        out["site_id"] = data["siteId"]
    else:
        raise DeserializationError("CreateEnvironmentRequest.site_id required")
    return out
