"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ImportPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.availability_slo
    import aws_sdk_resiliencehubv2.types.client_token
    import aws_sdk_resiliencehubv2.types.kms_key_id
    import aws_sdk_resiliencehubv2.types.multi_az_disaster_recovery_approach
    import aws_sdk_resiliencehubv2.types.multi_region_disaster_recovery_approach
    import aws_sdk_resiliencehubv2.types.tag_map


class ImportPolicyRequest(TypedDict, closed=True):
    v1_policy_arn: "aws_sdk_resiliencehubv2.types.arn.Arn"
    kms_key_id: NotRequired["aws_sdk_resiliencehubv2.types.kms_key_id.KmsKeyId"]
    availability_slo: NotRequired[
        "aws_sdk_resiliencehubv2.types.availability_slo.AvailabilitySlo"
    ]
    """<p>The availability SLO to set on the imported policy.</p>"""
    multi_az_disaster_recovery_approach: NotRequired[
        "aws_sdk_resiliencehubv2.types.multi_az_disaster_recovery_approach.MultiAzDisasterRecoveryApproach"
    ]
    """<p>The multi-AZ disaster recovery approach for the imported policy.</p>"""
    multi_region_disaster_recovery_approach: NotRequired[
        "aws_sdk_resiliencehubv2.types.multi_region_disaster_recovery_approach.MultiRegionDisasterRecoveryApproach"
    ]
    """<p>The multi-Region disaster recovery approach for the imported policy.</p>"""
    tags: NotRequired["aws_sdk_resiliencehubv2.types.tag_map.TagMap"]
    client_token: NotRequired["aws_sdk_resiliencehubv2.types.client_token.ClientToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ImportPolicyRequest) -> dict:
    out: dict = {}
    out["v1PolicyArn"] = value["v1_policy_arn"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "availability_slo" in value:
        import aws_sdk_resiliencehubv2.types.availability_slo

        out["availabilitySlo"] = (
            aws_sdk_resiliencehubv2.types.availability_slo.serialize_json(
                value["availability_slo"]
            )
        )
    if "multi_az_disaster_recovery_approach" in value:
        import aws_sdk_resiliencehubv2.types.multi_az_disaster_recovery_approach

        out["multiAzDisasterRecoveryApproach"] = (
            aws_sdk_resiliencehubv2.types.multi_az_disaster_recovery_approach.serialize_json(
                value["multi_az_disaster_recovery_approach"]
            )
        )
    if "multi_region_disaster_recovery_approach" in value:
        import aws_sdk_resiliencehubv2.types.multi_region_disaster_recovery_approach

        out["multiRegionDisasterRecoveryApproach"] = (
            aws_sdk_resiliencehubv2.types.multi_region_disaster_recovery_approach.serialize_json(
                value["multi_region_disaster_recovery_approach"]
            )
        )
    if "tags" in value:
        import aws_sdk_resiliencehubv2.types.tag_map

        out["tags"] = aws_sdk_resiliencehubv2.types.tag_map.serialize_json(
            value["tags"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> ImportPolicyRequest:
    out: ImportPolicyRequest = {}  # type: ignore[typeddict-item]
    if "v1PolicyArn" in data:
        out["v1_policy_arn"] = data["v1PolicyArn"]
    else:
        raise DeserializationError("ImportPolicyRequest.v1_policy_arn required")
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "availabilitySlo" in data:
        import aws_sdk_resiliencehubv2.types.availability_slo

        out["availability_slo"] = (
            aws_sdk_resiliencehubv2.types.availability_slo.deserialize_json(
                data["availabilitySlo"]
            )
        )
    if "multiAzDisasterRecoveryApproach" in data:
        import aws_sdk_resiliencehubv2.types.multi_az_disaster_recovery_approach

        out["multi_az_disaster_recovery_approach"] = (
            aws_sdk_resiliencehubv2.types.multi_az_disaster_recovery_approach.deserialize_json(
                data["multiAzDisasterRecoveryApproach"]
            )
        )
    if "multiRegionDisasterRecoveryApproach" in data:
        import aws_sdk_resiliencehubv2.types.multi_region_disaster_recovery_approach

        out["multi_region_disaster_recovery_approach"] = (
            aws_sdk_resiliencehubv2.types.multi_region_disaster_recovery_approach.deserialize_json(
                data["multiRegionDisasterRecoveryApproach"]
            )
        )
    if "tags" in data:
        import aws_sdk_resiliencehubv2.types.tag_map

        out["tags"] = aws_sdk_resiliencehubv2.types.tag_map.deserialize_json(
            data["tags"]
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
