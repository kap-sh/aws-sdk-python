"""Generated from Smithy shape ``com.amazonaws.deadline#GetLicenseEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.dns_name
    import capo_deadline.types.license_endpoint_id
    import capo_deadline.types.license_endpoint_status
    import capo_deadline.types.security_group_id_list
    import capo_deadline.types.status_message
    import capo_deadline.types.subnet_id_list
    import capo_deadline.types.vpc_id


class GetLicenseEndpointResponse(TypedDict, closed=True):
    license_endpoint_id: "capo_deadline.types.license_endpoint_id.LicenseEndpointId"
    """<p>The license endpoint ID.</p>"""
    status: "capo_deadline.types.license_endpoint_status.LicenseEndpointStatus"
    """<p>The status of the license endpoint.</p>"""
    status_message: "capo_deadline.types.status_message.StatusMessage"
    """<p>The status message of the license endpoint.</p>"""
    vpc_id: NotRequired["capo_deadline.types.vpc_id.VpcId"]
    """<p>The VPC (virtual private cloud) ID associated with the license endpoint.</p>"""
    dns_name: NotRequired["capo_deadline.types.dns_name.DnsName"]
    """<p>The DNS name.</p>"""
    subnet_ids: NotRequired["capo_deadline.types.subnet_id_list.SubnetIdList"]
    """<p>The subnet IDs.</p>"""
    security_group_ids: NotRequired[
        "capo_deadline.types.security_group_id_list.SecurityGroupIdList"
    ]
    """<p>The security group IDs for the license endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLicenseEndpointResponse) -> dict:
    out: dict = {}
    out["licenseEndpointId"] = value["license_endpoint_id"]
    import capo_deadline.types.license_endpoint_status

    out["status"] = capo_deadline.types.license_endpoint_status.serialize_json(
        value["status"]
    )
    out["statusMessage"] = value["status_message"]
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    if "dns_name" in value:
        out["dnsName"] = value["dns_name"]
    if "subnet_ids" in value:
        import capo_deadline.types.subnet_id_list

        out["subnetIds"] = capo_deadline.types.subnet_id_list.serialize_json(
            value["subnet_ids"]
        )
    if "security_group_ids" in value:
        import capo_deadline.types.security_group_id_list

        out["securityGroupIds"] = (
            capo_deadline.types.security_group_id_list.serialize_json(
                value["security_group_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetLicenseEndpointResponse:
    out: GetLicenseEndpointResponse = {}  # type: ignore[typeddict-item]
    if "licenseEndpointId" in data:
        out["license_endpoint_id"] = data["licenseEndpointId"]
    else:
        raise DeserializationError(
            "GetLicenseEndpointResponse.license_endpoint_id required"
        )
    if "status" in data:
        import capo_deadline.types.license_endpoint_status

        out["status"] = capo_deadline.types.license_endpoint_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GetLicenseEndpointResponse.status required")
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    else:
        raise DeserializationError("GetLicenseEndpointResponse.status_message required")
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    if "dnsName" in data:
        out["dns_name"] = data["dnsName"]
    if "subnetIds" in data:
        import capo_deadline.types.subnet_id_list

        out["subnet_ids"] = capo_deadline.types.subnet_id_list.deserialize_json(
            data["subnetIds"]
        )
    if "securityGroupIds" in data:
        import capo_deadline.types.security_group_id_list

        out["security_group_ids"] = (
            capo_deadline.types.security_group_id_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    return out
