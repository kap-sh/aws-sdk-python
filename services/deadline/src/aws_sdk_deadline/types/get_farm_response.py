"""Generated from Smithy shape ``com.amazonaws.deadline#GetFarmResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_deadline.types.cost_scale_factor
    import aws_sdk_deadline.types.created_at
    import aws_sdk_deadline.types.created_by
    import aws_sdk_deadline.types.description
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.kms_key_arn
    import aws_sdk_deadline.types.resource_name
    import aws_sdk_deadline.types.updated_at
    import aws_sdk_deadline.types.updated_by


class GetFarmResponse(TypedDict, closed=True):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID of the farm to get.</p>"""
    display_name: "aws_sdk_deadline.types.resource_name.ResourceName"
    """<p>The display name of the farm.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    kms_key_arn: NotRequired["aws_sdk_deadline.types.kms_key_arn.KmsKeyArn"]
    """<p>The ARN of the KMS key used on the farm.</p>"""
    created_at: "aws_sdk_deadline.types.created_at.CreatedAt"
    """<p>The date and time the resource was created.</p>"""
    created_by: "aws_sdk_deadline.types.created_by.CreatedBy"
    """<p>The user or system that created this resource.</p>"""
    updated_at: NotRequired["aws_sdk_deadline.types.updated_at.UpdatedAt"]
    """<p>The date and time the resource was updated.</p>"""
    updated_by: NotRequired["aws_sdk_deadline.types.updated_by.UpdatedBy"]
    """<p>The user or system that updated this resource.</p>"""
    description: NotRequired["aws_sdk_deadline.types.description.Description"]
    """<p>The description of the farm.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    cost_scale_factor: "aws_sdk_deadline.types.cost_scale_factor.CostScaleFactor"
    """<p>A multiplier applied to the farm's calculated costs for usage data and budget tracking. A value less than 1 represents a discount, a value greater than 1 represents a premium, and a value of 1 represents no adjustment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFarmResponse) -> dict:
    out: dict = {}
    out["farmId"] = value["farm_id"]
    out["displayName"] = value["display_name"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    import aws_sdk_deadline.types.created_at

    out["createdAt"] = aws_sdk_deadline.types.created_at.serialize_json(
        value["created_at"]
    )
    out["createdBy"] = value["created_by"]
    if "updated_at" in value:
        import aws_sdk_deadline.types.updated_at

        out["updatedAt"] = aws_sdk_deadline.types.updated_at.serialize_json(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["updatedBy"] = value["updated_by"]
    if "description" in value:
        out["description"] = value["description"]
    out["costScaleFactor"] = value.get("cost_scale_factor", 1)
    return out


def deserialize_json(data: dict) -> GetFarmResponse:
    out: GetFarmResponse = {}  # type: ignore[typeddict-item]
    if "farmId" in data:
        out["farm_id"] = data["farmId"]
    else:
        raise DeserializationError("GetFarmResponse.farm_id required")
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("GetFarmResponse.display_name required")
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if "createdAt" in data:
        import aws_sdk_deadline.types.created_at

        out["created_at"] = aws_sdk_deadline.types.created_at.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GetFarmResponse.created_at required")
    if "createdBy" in data:
        out["created_by"] = data["createdBy"]
    else:
        raise DeserializationError("GetFarmResponse.created_by required")
    if "updatedAt" in data:
        import aws_sdk_deadline.types.updated_at

        out["updated_at"] = aws_sdk_deadline.types.updated_at.deserialize_json(
            data["updatedAt"]
        )
    if "updatedBy" in data:
        out["updated_by"] = data["updatedBy"]
    if "description" in data:
        out["description"] = data["description"]
    if "costScaleFactor" in data:
        out["cost_scale_factor"] = data["costScaleFactor"]
    else:
        out["cost_scale_factor"] = 1
    return out
