"""Generated from Smithy shape ``com.amazonaws.odb#ManagedServices``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.cross_region_s3_restore_sources_access_list
    import capo_odb.types.kms_access
    import capo_odb.types.managed_s3_backup_access
    import capo_odb.types.resource_arn
    import capo_odb.types.s3_access
    import capo_odb.types.service_network_endpoint
    import capo_odb.types.string_list
    import capo_odb.types.sts_access
    import capo_odb.types.zero_etl_access


class ManagedServices(TypedDict, closed=True):
    service_network_arn: NotRequired["capo_odb.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the service network.</p>"""
    resource_gateway_arn: NotRequired["capo_odb.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the resource gateway.</p>"""
    managed_services_ipv4_cidrs: NotRequired["capo_odb.types.string_list.StringList"]
    """<p>The IPv4 CIDR blocks for the managed services.</p>"""
    service_network_endpoint: NotRequired[
        "capo_odb.types.service_network_endpoint.ServiceNetworkEndpoint"
    ]
    """<p>The service network endpoint configuration.</p>"""
    managed_s3_backup_access: NotRequired[
        "capo_odb.types.managed_s3_backup_access.ManagedS3BackupAccess"
    ]
    """<p>The managed Amazon S3 backup access configuration.</p>"""
    zero_etl_access: NotRequired["capo_odb.types.zero_etl_access.ZeroEtlAccess"]
    """<p>The Zero-ETL access configuration.</p>"""
    s3_access: NotRequired["capo_odb.types.s3_access.S3Access"]
    """<p>The Amazon S3 access configuration.</p>"""
    sts_access: NotRequired["capo_odb.types.sts_access.StsAccess"]
    """<p>The Amazon Web Services Security Token Service (STS) access configuration.</p>"""
    kms_access: NotRequired["capo_odb.types.kms_access.KmsAccess"]
    """<p>The Amazon Web Services Key Management Service (KMS) access configuration.</p>"""
    cross_region_s3_restore_sources_access: NotRequired[
        "capo_odb.types.cross_region_s3_restore_sources_access_list.CrossRegionS3RestoreSourcesAccessList"
    ]
    """<p>The access configuration for the cross-Region Amazon S3 database restore source.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ManagedServices) -> dict:
    out: dict = {}
    if "service_network_arn" in value:
        out["serviceNetworkArn"] = value["service_network_arn"]
    if "resource_gateway_arn" in value:
        out["resourceGatewayArn"] = value["resource_gateway_arn"]
    if "managed_services_ipv4_cidrs" in value:
        import capo_odb.types.string_list

        out["managedServicesIpv4Cidrs"] = (
            capo_odb.types.string_list.serialize_aws_json_1_0(
                value["managed_services_ipv4_cidrs"]
            )
        )
    if "service_network_endpoint" in value:
        import capo_odb.types.service_network_endpoint

        out["serviceNetworkEndpoint"] = (
            capo_odb.types.service_network_endpoint.serialize_aws_json_1_0(
                value["service_network_endpoint"]
            )
        )
    if "managed_s3_backup_access" in value:
        import capo_odb.types.managed_s3_backup_access

        out["managedS3BackupAccess"] = (
            capo_odb.types.managed_s3_backup_access.serialize_aws_json_1_0(
                value["managed_s3_backup_access"]
            )
        )
    if "zero_etl_access" in value:
        import capo_odb.types.zero_etl_access

        out["zeroEtlAccess"] = capo_odb.types.zero_etl_access.serialize_aws_json_1_0(
            value["zero_etl_access"]
        )
    if "s3_access" in value:
        import capo_odb.types.s3_access

        out["s3Access"] = capo_odb.types.s3_access.serialize_aws_json_1_0(
            value["s3_access"]
        )
    if "sts_access" in value:
        import capo_odb.types.sts_access

        out["stsAccess"] = capo_odb.types.sts_access.serialize_aws_json_1_0(
            value["sts_access"]
        )
    if "kms_access" in value:
        import capo_odb.types.kms_access

        out["kmsAccess"] = capo_odb.types.kms_access.serialize_aws_json_1_0(
            value["kms_access"]
        )
    if "cross_region_s3_restore_sources_access" in value:
        import capo_odb.types.cross_region_s3_restore_sources_access_list

        out["crossRegionS3RestoreSourcesAccess"] = (
            capo_odb.types.cross_region_s3_restore_sources_access_list.serialize_aws_json_1_0(
                value["cross_region_s3_restore_sources_access"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ManagedServices:
    out: ManagedServices = {}  # type: ignore[typeddict-item]
    if "serviceNetworkArn" in data:
        out["service_network_arn"] = data["serviceNetworkArn"]
    if "resourceGatewayArn" in data:
        out["resource_gateway_arn"] = data["resourceGatewayArn"]
    if "managedServicesIpv4Cidrs" in data:
        import capo_odb.types.string_list

        out["managed_services_ipv4_cidrs"] = (
            capo_odb.types.string_list.deserialize_aws_json_1_0(
                data["managedServicesIpv4Cidrs"]
            )
        )
    if "serviceNetworkEndpoint" in data:
        import capo_odb.types.service_network_endpoint

        out["service_network_endpoint"] = (
            capo_odb.types.service_network_endpoint.deserialize_aws_json_1_0(
                data["serviceNetworkEndpoint"]
            )
        )
    if "managedS3BackupAccess" in data:
        import capo_odb.types.managed_s3_backup_access

        out["managed_s3_backup_access"] = (
            capo_odb.types.managed_s3_backup_access.deserialize_aws_json_1_0(
                data["managedS3BackupAccess"]
            )
        )
    if "zeroEtlAccess" in data:
        import capo_odb.types.zero_etl_access

        out["zero_etl_access"] = (
            capo_odb.types.zero_etl_access.deserialize_aws_json_1_0(
                data["zeroEtlAccess"]
            )
        )
    if "s3Access" in data:
        import capo_odb.types.s3_access

        out["s3_access"] = capo_odb.types.s3_access.deserialize_aws_json_1_0(
            data["s3Access"]
        )
    if "stsAccess" in data:
        import capo_odb.types.sts_access

        out["sts_access"] = capo_odb.types.sts_access.deserialize_aws_json_1_0(
            data["stsAccess"]
        )
    if "kmsAccess" in data:
        import capo_odb.types.kms_access

        out["kms_access"] = capo_odb.types.kms_access.deserialize_aws_json_1_0(
            data["kmsAccess"]
        )
    if "crossRegionS3RestoreSourcesAccess" in data:
        import capo_odb.types.cross_region_s3_restore_sources_access_list

        out["cross_region_s3_restore_sources_access"] = (
            capo_odb.types.cross_region_s3_restore_sources_access_list.deserialize_aws_json_1_0(
                data["crossRegionS3RestoreSourcesAccess"]
            )
        )
    return out
