"""Generated from Smithy shape ``com.amazonaws.finspace#KxEnvironment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.availability_zone_ids
    import capo_finspace.types.custom_dns_configuration
    import capo_finspace.types.description
    import capo_finspace.types.dns_status
    import capo_finspace.types.environment_arn
    import capo_finspace.types.environment_error_message
    import capo_finspace.types.environment_status
    import capo_finspace.types.id_type
    import capo_finspace.types.kms_key_id
    import capo_finspace.types.kx_environment_name
    import capo_finspace.types.string_value_length1to255
    import capo_finspace.types.tgw_status
    import capo_finspace.types.timestamp
    import capo_finspace.types.transit_gateway_configuration


class KxEnvironment(TypedDict, closed=True):
    name: NotRequired["capo_finspace.types.kx_environment_name.KxEnvironmentName"]
    """<p>The name of the kdb environment.</p>"""
    environment_id: NotRequired["capo_finspace.types.id_type.IdType"]
    """<p>A unique identifier for the kdb environment.</p>"""
    aws_account_id: NotRequired["capo_finspace.types.id_type.IdType"]
    """<p>The unique identifier of the AWS account in which you create the kdb environment.</p>"""
    status: NotRequired["capo_finspace.types.environment_status.EnvironmentStatus"]
    """<p>The status of the environment creation. </p> <ul> <li> <p>CREATE_REQUESTED – Environment creation has been requested.</p> </li> <li> <p>CREATING – Environment is in the process of being created.</p> </li> <li> <p>FAILED_CREATION – Environment creation has failed.</p> </li> <li> <p>CREATED – Environment is successfully created and is currently active.</p> </li> <li> <p>DELETE REQUESTED – Environment deletion has been requested.</p> </li> <li> <p>DELETING – Environment is in the process of being deleted.</p> </li> <li> <p>RETRY_DELETION – Initial environment deletion failed, system is reattempting delete.</p> </li> <li> <p>DELETED – Environment has been deleted.</p> </li> <li> <p>FAILED_DELETION – Environment deletion has failed.</p> </li> </ul>"""
    tgw_status: NotRequired["capo_finspace.types.tgw_status.tgwStatus"]
    """<p>The status of the network configuration.</p>"""
    dns_status: NotRequired["capo_finspace.types.dns_status.dnsStatus"]
    """<p>The status of DNS configuration.</p>"""
    error_message: NotRequired[
        "capo_finspace.types.environment_error_message.EnvironmentErrorMessage"
    ]
    """<p>Specifies the error message that appears if a flow fails. </p>"""
    description: NotRequired["capo_finspace.types.description.Description"]
    """<p>A description of the kdb environment.</p>"""
    environment_arn: NotRequired["capo_finspace.types.environment_arn.EnvironmentArn"]
    """<p>The Amazon Resource Name (ARN) of your kdb environment.</p>"""
    kms_key_id: NotRequired["capo_finspace.types.kms_key_id.KmsKeyId"]
    """<p>The unique identifier of the KMS key.</p>"""
    dedicated_service_account_id: NotRequired["capo_finspace.types.id_type.IdType"]
    """<p>A unique identifier for the AWS environment infrastructure account.</p>"""
    transit_gateway_configuration: NotRequired[
        "capo_finspace.types.transit_gateway_configuration.TransitGatewayConfiguration"
    ]
    """<p>Specifies the transit gateway and network configuration to connect the kdb environment to an internal network.</p>"""
    custom_dns_configuration: NotRequired[
        "capo_finspace.types.custom_dns_configuration.CustomDNSConfiguration"
    ]
    """<p>A list of DNS server name and server IP. This is used to set up Route-53 outbound resolvers.</p>"""
    creation_timestamp: NotRequired["capo_finspace.types.timestamp.Timestamp"]
    """<p>The timestamp at which the kdb environment was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""
    update_timestamp: NotRequired["capo_finspace.types.timestamp.Timestamp"]
    """<p>The timestamp at which the kdb environment was modified in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""
    availability_zone_ids: NotRequired[
        "capo_finspace.types.availability_zone_ids.AvailabilityZoneIds"
    ]
    """<p>The identifier of the availability zones where subnets for the environment are created.</p>"""
    certificate_authority_arn: NotRequired[
        "capo_finspace.types.string_value_length1to255.stringValueLength1to255"
    ]
    """<p>The Amazon Resource Name (ARN) of the certificate authority:</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KxEnvironment) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    if "aws_account_id" in value:
        out["awsAccountId"] = value["aws_account_id"]
    if "status" in value:
        import capo_finspace.types.environment_status

        out["status"] = capo_finspace.types.environment_status.serialize_json(
            value["status"]
        )
    if "tgw_status" in value:
        import capo_finspace.types.tgw_status

        out["tgwStatus"] = capo_finspace.types.tgw_status.serialize_json(
            value["tgw_status"]
        )
    if "dns_status" in value:
        import capo_finspace.types.dns_status

        out["dnsStatus"] = capo_finspace.types.dns_status.serialize_json(
            value["dns_status"]
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "description" in value:
        out["description"] = value["description"]
    if "environment_arn" in value:
        out["environmentArn"] = value["environment_arn"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "dedicated_service_account_id" in value:
        out["dedicatedServiceAccountId"] = value["dedicated_service_account_id"]
    if "transit_gateway_configuration" in value:
        import capo_finspace.types.transit_gateway_configuration

        out["transitGatewayConfiguration"] = (
            capo_finspace.types.transit_gateway_configuration.serialize_json(
                value["transit_gateway_configuration"]
            )
        )
    if "custom_dns_configuration" in value:
        import capo_finspace.types.custom_dns_configuration

        out["customDNSConfiguration"] = (
            capo_finspace.types.custom_dns_configuration.serialize_json(
                value["custom_dns_configuration"]
            )
        )
    if "creation_timestamp" in value:
        import capo_finspace.types.timestamp

        out["creationTimestamp"] = capo_finspace.types.timestamp.serialize_json(
            value["creation_timestamp"]
        )
    if "update_timestamp" in value:
        import capo_finspace.types.timestamp

        out["updateTimestamp"] = capo_finspace.types.timestamp.serialize_json(
            value["update_timestamp"]
        )
    if "availability_zone_ids" in value:
        import capo_finspace.types.availability_zone_ids

        out["availabilityZoneIds"] = (
            capo_finspace.types.availability_zone_ids.serialize_json(
                value["availability_zone_ids"]
            )
        )
    if "certificate_authority_arn" in value:
        out["certificateAuthorityArn"] = value["certificate_authority_arn"]
    return out


def deserialize_json(data: dict) -> KxEnvironment:
    out: KxEnvironment = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    if "awsAccountId" in data:
        out["aws_account_id"] = data["awsAccountId"]
    if "status" in data:
        import capo_finspace.types.environment_status

        out["status"] = capo_finspace.types.environment_status.deserialize_json(
            data["status"]
        )
    if "tgwStatus" in data:
        import capo_finspace.types.tgw_status

        out["tgw_status"] = capo_finspace.types.tgw_status.deserialize_json(
            data["tgwStatus"]
        )
    if "dnsStatus" in data:
        import capo_finspace.types.dns_status

        out["dns_status"] = capo_finspace.types.dns_status.deserialize_json(
            data["dnsStatus"]
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    if "description" in data:
        out["description"] = data["description"]
    if "environmentArn" in data:
        out["environment_arn"] = data["environmentArn"]
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "dedicatedServiceAccountId" in data:
        out["dedicated_service_account_id"] = data["dedicatedServiceAccountId"]
    if "transitGatewayConfiguration" in data:
        import capo_finspace.types.transit_gateway_configuration

        out["transit_gateway_configuration"] = (
            capo_finspace.types.transit_gateway_configuration.deserialize_json(
                data["transitGatewayConfiguration"]
            )
        )
    if "customDNSConfiguration" in data:
        import capo_finspace.types.custom_dns_configuration

        out["custom_dns_configuration"] = (
            capo_finspace.types.custom_dns_configuration.deserialize_json(
                data["customDNSConfiguration"]
            )
        )
    if "creationTimestamp" in data:
        import capo_finspace.types.timestamp

        out["creation_timestamp"] = capo_finspace.types.timestamp.deserialize_json(
            data["creationTimestamp"]
        )
    if "updateTimestamp" in data:
        import capo_finspace.types.timestamp

        out["update_timestamp"] = capo_finspace.types.timestamp.deserialize_json(
            data["updateTimestamp"]
        )
    if "availabilityZoneIds" in data:
        import capo_finspace.types.availability_zone_ids

        out["availability_zone_ids"] = (
            capo_finspace.types.availability_zone_ids.deserialize_json(
                data["availabilityZoneIds"]
            )
        )
    if "certificateAuthorityArn" in data:
        out["certificate_authority_arn"] = data["certificateAuthorityArn"]
    return out
