"""Generated from Smithy shape ``com.amazonaws.odb#UpdateOdbNetworkInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_odb.types.access
    import aws_sdk_odb.types.policy_document
    import aws_sdk_odb.types.resource_display_name
    import aws_sdk_odb.types.resource_id_or_arn
    import aws_sdk_odb.types.string_list


class UpdateOdbNetworkInput(TypedDict, closed=True):
    odb_network_id: "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the ODB network to update.</p>"""
    display_name: NotRequired[
        "aws_sdk_odb.types.resource_display_name.ResourceDisplayName"
    ]
    """<p>The new user-friendly name of the ODB network.</p>"""
    peered_cidrs_to_be_added: NotRequired["aws_sdk_odb.types.string_list.StringList"]
    """<p>The list of CIDR ranges from the peered VPC that allow access to the ODB network.</p>"""
    peered_cidrs_to_be_removed: NotRequired["aws_sdk_odb.types.string_list.StringList"]
    """<p>The list of CIDR ranges from the peered VPC to remove from the ODB network.</p>"""
    s3_access: NotRequired["aws_sdk_odb.types.access.Access"]
    """<p>Specifies the updated configuration for Amazon S3 access from the ODB network.</p>"""
    zero_etl_access: NotRequired["aws_sdk_odb.types.access.Access"]
    """<p>Specifies the updated configuration for Zero-ETL access from the ODB network.</p>"""
    sts_access: NotRequired["aws_sdk_odb.types.access.Access"]
    """<p>The Amazon Web Services Security Token Service (STS) access configuration for the ODB network.</p>"""
    kms_access: NotRequired["aws_sdk_odb.types.access.Access"]
    """<p>The Amazon Web Services Key Management Service (KMS) access configuration for the ODB network.</p>"""
    s3_policy_document: NotRequired["aws_sdk_odb.types.policy_document.PolicyDocument"]
    """<p>Specifies the updated endpoint policy for Amazon S3 access from the ODB network.</p>"""
    sts_policy_document: NotRequired["aws_sdk_odb.types.policy_document.PolicyDocument"]
    """<p>The Amazon Web Services Security Token Service (STS) policy document that defines permissions for token service usage within the ODB network.</p>"""
    kms_policy_document: NotRequired["aws_sdk_odb.types.policy_document.PolicyDocument"]
    """<p>The Amazon Web Services Key Management Service (KMS) policy document that defines permissions for key usage within the ODB network.</p>"""
    cross_region_s3_restore_sources_to_enable: NotRequired[
        "aws_sdk_odb.types.string_list.StringList"
    ]
    """<p>The cross-Region Amazon S3 restore sources to enable for the ODB network.</p>"""
    cross_region_s3_restore_sources_to_disable: NotRequired[
        "aws_sdk_odb.types.string_list.StringList"
    ]
    """<p>The cross-Region Amazon S3 restore sources to disable for the ODB network.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateOdbNetworkInput) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "peered_cidrs_to_be_added" in value:
        import aws_sdk_odb.types.string_list

        out["peeredCidrsToBeAdded"] = (
            aws_sdk_odb.types.string_list.serialize_aws_json_1_0(
                value["peered_cidrs_to_be_added"]
            )
        )
    if "peered_cidrs_to_be_removed" in value:
        import aws_sdk_odb.types.string_list

        out["peeredCidrsToBeRemoved"] = (
            aws_sdk_odb.types.string_list.serialize_aws_json_1_0(
                value["peered_cidrs_to_be_removed"]
            )
        )
    if "s3_access" in value:
        import aws_sdk_odb.types.access

        out["s3Access"] = aws_sdk_odb.types.access.serialize_aws_json_1_0(
            value["s3_access"]
        )
    if "zero_etl_access" in value:
        import aws_sdk_odb.types.access

        out["zeroEtlAccess"] = aws_sdk_odb.types.access.serialize_aws_json_1_0(
            value["zero_etl_access"]
        )
    if "sts_access" in value:
        import aws_sdk_odb.types.access

        out["stsAccess"] = aws_sdk_odb.types.access.serialize_aws_json_1_0(
            value["sts_access"]
        )
    if "kms_access" in value:
        import aws_sdk_odb.types.access

        out["kmsAccess"] = aws_sdk_odb.types.access.serialize_aws_json_1_0(
            value["kms_access"]
        )
    if "s3_policy_document" in value:
        out["s3PolicyDocument"] = value["s3_policy_document"]
    if "sts_policy_document" in value:
        out["stsPolicyDocument"] = value["sts_policy_document"]
    if "kms_policy_document" in value:
        out["kmsPolicyDocument"] = value["kms_policy_document"]
    if "cross_region_s3_restore_sources_to_enable" in value:
        import aws_sdk_odb.types.string_list

        out["crossRegionS3RestoreSourcesToEnable"] = (
            aws_sdk_odb.types.string_list.serialize_aws_json_1_0(
                value["cross_region_s3_restore_sources_to_enable"]
            )
        )
    if "cross_region_s3_restore_sources_to_disable" in value:
        import aws_sdk_odb.types.string_list

        out["crossRegionS3RestoreSourcesToDisable"] = (
            aws_sdk_odb.types.string_list.serialize_aws_json_1_0(
                value["cross_region_s3_restore_sources_to_disable"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateOdbNetworkInput:
    out: UpdateOdbNetworkInput = {}  # type: ignore[typeddict-item]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "peeredCidrsToBeAdded" in data:
        import aws_sdk_odb.types.string_list

        out["peered_cidrs_to_be_added"] = (
            aws_sdk_odb.types.string_list.deserialize_aws_json_1_0(
                data["peeredCidrsToBeAdded"]
            )
        )
    if "peeredCidrsToBeRemoved" in data:
        import aws_sdk_odb.types.string_list

        out["peered_cidrs_to_be_removed"] = (
            aws_sdk_odb.types.string_list.deserialize_aws_json_1_0(
                data["peeredCidrsToBeRemoved"]
            )
        )
    if "s3Access" in data:
        import aws_sdk_odb.types.access

        out["s3_access"] = aws_sdk_odb.types.access.deserialize_aws_json_1_0(
            data["s3Access"]
        )
    if "zeroEtlAccess" in data:
        import aws_sdk_odb.types.access

        out["zero_etl_access"] = aws_sdk_odb.types.access.deserialize_aws_json_1_0(
            data["zeroEtlAccess"]
        )
    if "stsAccess" in data:
        import aws_sdk_odb.types.access

        out["sts_access"] = aws_sdk_odb.types.access.deserialize_aws_json_1_0(
            data["stsAccess"]
        )
    if "kmsAccess" in data:
        import aws_sdk_odb.types.access

        out["kms_access"] = aws_sdk_odb.types.access.deserialize_aws_json_1_0(
            data["kmsAccess"]
        )
    if "s3PolicyDocument" in data:
        out["s3_policy_document"] = data["s3PolicyDocument"]
    if "stsPolicyDocument" in data:
        out["sts_policy_document"] = data["stsPolicyDocument"]
    if "kmsPolicyDocument" in data:
        out["kms_policy_document"] = data["kmsPolicyDocument"]
    if "crossRegionS3RestoreSourcesToEnable" in data:
        import aws_sdk_odb.types.string_list

        out["cross_region_s3_restore_sources_to_enable"] = (
            aws_sdk_odb.types.string_list.deserialize_aws_json_1_0(
                data["crossRegionS3RestoreSourcesToEnable"]
            )
        )
    if "crossRegionS3RestoreSourcesToDisable" in data:
        import aws_sdk_odb.types.string_list

        out["cross_region_s3_restore_sources_to_disable"] = (
            aws_sdk_odb.types.string_list.deserialize_aws_json_1_0(
                data["crossRegionS3RestoreSourcesToDisable"]
            )
        )
    return out
