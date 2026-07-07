"""Generated from Smithy shape ``com.amazonaws.finspace#UpdateKxEnvironmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace.types.availability_zone_ids
    import aws_sdk_finspace.types.custom_dns_configuration
    import aws_sdk_finspace.types.description
    import aws_sdk_finspace.types.dns_status
    import aws_sdk_finspace.types.environment_arn
    import aws_sdk_finspace.types.environment_error_message
    import aws_sdk_finspace.types.environment_status
    import aws_sdk_finspace.types.id_type
    import aws_sdk_finspace.types.kms_key_id
    import aws_sdk_finspace.types.kx_environment_name
    import aws_sdk_finspace.types.tgw_status
    import aws_sdk_finspace.types.timestamp
    import aws_sdk_finspace.types.transit_gateway_configuration


class UpdateKxEnvironmentResponse(TypedDict, closed=True):
    name: NotRequired["aws_sdk_finspace.types.kx_environment_name.KxEnvironmentName"]
    """<p>The name of the kdb environment.</p>"""
    environment_id: NotRequired["aws_sdk_finspace.types.id_type.IdType"]
    """<p>A unique identifier for the kdb environment.</p>"""
    aws_account_id: NotRequired["aws_sdk_finspace.types.id_type.IdType"]
    """<p>The unique identifier of the AWS account that is used to create the kdb environment.</p>"""
    status: NotRequired["aws_sdk_finspace.types.environment_status.EnvironmentStatus"]
    """<p>The status of the kdb environment.</p>"""
    tgw_status: NotRequired["aws_sdk_finspace.types.tgw_status.tgwStatus"]
    """<p>The status of the network configuration.</p>"""
    dns_status: NotRequired["aws_sdk_finspace.types.dns_status.dnsStatus"]
    """<p>The status of DNS configuration.</p>"""
    error_message: NotRequired[
        "aws_sdk_finspace.types.environment_error_message.EnvironmentErrorMessage"
    ]
    """<p>Specifies the error message that appears if a flow fails.</p>"""
    description: NotRequired["aws_sdk_finspace.types.description.Description"]
    """<p>The description of the environment.</p>"""
    environment_arn: NotRequired[
        "aws_sdk_finspace.types.environment_arn.EnvironmentArn"
    ]
    """<p>The ARN identifier of the environment.</p>"""
    kms_key_id: NotRequired["aws_sdk_finspace.types.kms_key_id.KmsKeyId"]
    """<p>The KMS key ID to encrypt your data in the FinSpace environment.</p>"""
    dedicated_service_account_id: NotRequired["aws_sdk_finspace.types.id_type.IdType"]
    """<p>A unique identifier for the AWS environment infrastructure account.</p>"""
    transit_gateway_configuration: NotRequired[
        "aws_sdk_finspace.types.transit_gateway_configuration.TransitGatewayConfiguration"
    ]
    custom_dns_configuration: NotRequired[
        "aws_sdk_finspace.types.custom_dns_configuration.CustomDNSConfiguration"
    ]
    """<p>A list of DNS server name and server IP. This is used to set up Route-53 outbound resolvers.</p>"""
    creation_timestamp: NotRequired["aws_sdk_finspace.types.timestamp.Timestamp"]
    """<p>The timestamp at which the kdb environment was created in FinSpace. </p>"""
    update_timestamp: NotRequired["aws_sdk_finspace.types.timestamp.Timestamp"]
    """<p>The timestamp at which the kdb environment was updated. </p>"""
    availability_zone_ids: NotRequired[
        "aws_sdk_finspace.types.availability_zone_ids.AvailabilityZoneIds"
    ]
    """<p>The identifier of the availability zones where subnets for the environment are created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateKxEnvironmentResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    if "aws_account_id" in value:
        out["awsAccountId"] = value["aws_account_id"]
    if "status" in value:
        import aws_sdk_finspace.types.environment_status

        out["status"] = aws_sdk_finspace.types.environment_status.serialize_json(
            value["status"]
        )
    if "tgw_status" in value:
        import aws_sdk_finspace.types.tgw_status

        out["tgwStatus"] = aws_sdk_finspace.types.tgw_status.serialize_json(
            value["tgw_status"]
        )
    if "dns_status" in value:
        import aws_sdk_finspace.types.dns_status

        out["dnsStatus"] = aws_sdk_finspace.types.dns_status.serialize_json(
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
        import aws_sdk_finspace.types.transit_gateway_configuration

        out["transitGatewayConfiguration"] = (
            aws_sdk_finspace.types.transit_gateway_configuration.serialize_json(
                value["transit_gateway_configuration"]
            )
        )
    if "custom_dns_configuration" in value:
        import aws_sdk_finspace.types.custom_dns_configuration

        out["customDNSConfiguration"] = (
            aws_sdk_finspace.types.custom_dns_configuration.serialize_json(
                value["custom_dns_configuration"]
            )
        )
    if "creation_timestamp" in value:
        import aws_sdk_finspace.types.timestamp

        out["creationTimestamp"] = aws_sdk_finspace.types.timestamp.serialize_json(
            value["creation_timestamp"]
        )
    if "update_timestamp" in value:
        import aws_sdk_finspace.types.timestamp

        out["updateTimestamp"] = aws_sdk_finspace.types.timestamp.serialize_json(
            value["update_timestamp"]
        )
    if "availability_zone_ids" in value:
        import aws_sdk_finspace.types.availability_zone_ids

        out["availabilityZoneIds"] = (
            aws_sdk_finspace.types.availability_zone_ids.serialize_json(
                value["availability_zone_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateKxEnvironmentResponse:
    out: UpdateKxEnvironmentResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    if "awsAccountId" in data:
        out["aws_account_id"] = data["awsAccountId"]
    if "status" in data:
        import aws_sdk_finspace.types.environment_status

        out["status"] = aws_sdk_finspace.types.environment_status.deserialize_json(
            data["status"]
        )
    if "tgwStatus" in data:
        import aws_sdk_finspace.types.tgw_status

        out["tgw_status"] = aws_sdk_finspace.types.tgw_status.deserialize_json(
            data["tgwStatus"]
        )
    if "dnsStatus" in data:
        import aws_sdk_finspace.types.dns_status

        out["dns_status"] = aws_sdk_finspace.types.dns_status.deserialize_json(
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
        import aws_sdk_finspace.types.transit_gateway_configuration

        out["transit_gateway_configuration"] = (
            aws_sdk_finspace.types.transit_gateway_configuration.deserialize_json(
                data["transitGatewayConfiguration"]
            )
        )
    if "customDNSConfiguration" in data:
        import aws_sdk_finspace.types.custom_dns_configuration

        out["custom_dns_configuration"] = (
            aws_sdk_finspace.types.custom_dns_configuration.deserialize_json(
                data["customDNSConfiguration"]
            )
        )
    if "creationTimestamp" in data:
        import aws_sdk_finspace.types.timestamp

        out["creation_timestamp"] = aws_sdk_finspace.types.timestamp.deserialize_json(
            data["creationTimestamp"]
        )
    if "updateTimestamp" in data:
        import aws_sdk_finspace.types.timestamp

        out["update_timestamp"] = aws_sdk_finspace.types.timestamp.deserialize_json(
            data["updateTimestamp"]
        )
    if "availabilityZoneIds" in data:
        import aws_sdk_finspace.types.availability_zone_ids

        out["availability_zone_ids"] = (
            aws_sdk_finspace.types.availability_zone_ids.deserialize_json(
                data["availabilityZoneIds"]
            )
        )
    return out
