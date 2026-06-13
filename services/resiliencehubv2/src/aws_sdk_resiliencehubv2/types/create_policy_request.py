"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#CreatePolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.availability_slo
    import aws_sdk_resiliencehubv2.types.client_token
    import aws_sdk_resiliencehubv2.types.data_recovery_targets
    import aws_sdk_resiliencehubv2.types.entity_name
    import aws_sdk_resiliencehubv2.types.kms_key_id
    import aws_sdk_resiliencehubv2.types.long_description
    import aws_sdk_resiliencehubv2.types.multi_az_targets
    import aws_sdk_resiliencehubv2.types.multi_region_targets
    import aws_sdk_resiliencehubv2.types.tag_map


class CreatePolicyRequest(TypedDict):
    name: "aws_sdk_resiliencehubv2.types.entity_name.EntityName"
    description: NotRequired[
        "aws_sdk_resiliencehubv2.types.long_description.LongDescription"
    ]
    availability_slo: NotRequired[
        "aws_sdk_resiliencehubv2.types.availability_slo.AvailabilitySlo"
    ]
    """<p>The availability SLO for the resilience policy.</p>"""
    multi_az: NotRequired[
        "aws_sdk_resiliencehubv2.types.multi_az_targets.MultiAzTargets"
    ]
    """<p>The multi-AZ disaster recovery targets for the resilience policy.</p>"""
    multi_region: NotRequired[
        "aws_sdk_resiliencehubv2.types.multi_region_targets.MultiRegionTargets"
    ]
    """<p>The multi-Region disaster recovery targets for the resilience policy.</p>"""
    data_recovery: NotRequired[
        "aws_sdk_resiliencehubv2.types.data_recovery_targets.DataRecoveryTargets"
    ]
    """<p>The data recovery targets for the resilience policy.</p>"""
    kms_key_id: NotRequired["aws_sdk_resiliencehubv2.types.kms_key_id.KmsKeyId"]
    tags: NotRequired["aws_sdk_resiliencehubv2.types.tag_map.TagMap"]
    client_token: NotRequired["aws_sdk_resiliencehubv2.types.client_token.ClientToken"]


# --- restJson1 ser/de ---
def serialize_json(value: CreatePolicyRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "availability_slo" in value:
        import aws_sdk_resiliencehubv2.types.availability_slo

        out["availabilitySlo"] = (
            aws_sdk_resiliencehubv2.types.availability_slo.serialize_json(
                value["availability_slo"]
            )
        )
    if "multi_az" in value:
        import aws_sdk_resiliencehubv2.types.multi_az_targets

        out["multiAz"] = aws_sdk_resiliencehubv2.types.multi_az_targets.serialize_json(
            value["multi_az"]
        )
    if "multi_region" in value:
        import aws_sdk_resiliencehubv2.types.multi_region_targets

        out["multiRegion"] = (
            aws_sdk_resiliencehubv2.types.multi_region_targets.serialize_json(
                value["multi_region"]
            )
        )
    if "data_recovery" in value:
        import aws_sdk_resiliencehubv2.types.data_recovery_targets

        out["dataRecovery"] = (
            aws_sdk_resiliencehubv2.types.data_recovery_targets.serialize_json(
                value["data_recovery"]
            )
        )
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "tags" in value:
        import aws_sdk_resiliencehubv2.types.tag_map

        out["tags"] = aws_sdk_resiliencehubv2.types.tag_map.serialize_json(
            value["tags"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreatePolicyRequest:
    out: CreatePolicyRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreatePolicyRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "availabilitySlo" in data:
        import aws_sdk_resiliencehubv2.types.availability_slo

        out["availability_slo"] = (
            aws_sdk_resiliencehubv2.types.availability_slo.deserialize_json(
                data["availabilitySlo"]
            )
        )
    if "multiAz" in data:
        import aws_sdk_resiliencehubv2.types.multi_az_targets

        out["multi_az"] = (
            aws_sdk_resiliencehubv2.types.multi_az_targets.deserialize_json(
                data["multiAz"]
            )
        )
    if "multiRegion" in data:
        import aws_sdk_resiliencehubv2.types.multi_region_targets

        out["multi_region"] = (
            aws_sdk_resiliencehubv2.types.multi_region_targets.deserialize_json(
                data["multiRegion"]
            )
        )
    if "dataRecovery" in data:
        import aws_sdk_resiliencehubv2.types.data_recovery_targets

        out["data_recovery"] = (
            aws_sdk_resiliencehubv2.types.data_recovery_targets.deserialize_json(
                data["dataRecovery"]
            )
        )
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "tags" in data:
        import aws_sdk_resiliencehubv2.types.tag_map

        out["tags"] = aws_sdk_resiliencehubv2.types.tag_map.deserialize_json(
            data["tags"]
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
