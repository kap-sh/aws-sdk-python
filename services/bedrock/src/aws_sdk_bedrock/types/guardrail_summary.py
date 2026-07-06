"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.guardrail_arn
    import aws_sdk_bedrock.types.guardrail_cross_region_details
    import aws_sdk_bedrock.types.guardrail_description
    import aws_sdk_bedrock.types.guardrail_id
    import aws_sdk_bedrock.types.guardrail_name
    import aws_sdk_bedrock.types.guardrail_status
    import aws_sdk_bedrock.types.guardrail_version
    import aws_sdk_bedrock.types.timestamp


class GuardrailSummary(TypedDict, closed=True):
    id: "aws_sdk_bedrock.types.guardrail_id.GuardrailId"
    """<p>The unique identifier of the guardrail.</p>"""
    arn: "aws_sdk_bedrock.types.guardrail_arn.GuardrailArn"
    """<p>The ARN of the guardrail.</p>"""
    status: "aws_sdk_bedrock.types.guardrail_status.GuardrailStatus"
    """<p>The status of the guardrail.</p>"""
    name: "aws_sdk_bedrock.types.guardrail_name.GuardrailName"
    """<p>The name of the guardrail.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock.types.guardrail_description.GuardrailDescription"
    ]
    """<p>A description of the guardrail.</p>"""
    version: "aws_sdk_bedrock.types.guardrail_version.GuardrailVersion"
    """<p>The version of the guardrail.</p>"""
    created_at: "aws_sdk_bedrock.types.timestamp.Timestamp"
    """<p>The date and time at which the guardrail was created.</p>"""
    updated_at: "aws_sdk_bedrock.types.timestamp.Timestamp"
    """<p>The date and time at which the guardrail was last updated.</p>"""
    cross_region_details: NotRequired[
        "aws_sdk_bedrock.types.guardrail_cross_region_details.GuardrailCrossRegionDetails"
    ]
    """<p>Details about the system-defined guardrail profile that you're using with your guardrail, including the guardrail profile ID and Amazon Resource Name (ARN).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    import aws_sdk_bedrock.types.guardrail_status

    out["status"] = aws_sdk_bedrock.types.guardrail_status.serialize_json(
        value["status"]
    )
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["version"] = value["version"]
    import aws_sdk_bedrock.types.timestamp

    out["createdAt"] = aws_sdk_bedrock.types.timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_bedrock.types.timestamp

    out["updatedAt"] = aws_sdk_bedrock.types.timestamp.serialize_json(
        value["updated_at"]
    )
    if "cross_region_details" in value:
        import aws_sdk_bedrock.types.guardrail_cross_region_details

        out["crossRegionDetails"] = (
            aws_sdk_bedrock.types.guardrail_cross_region_details.serialize_json(
                value["cross_region_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> GuardrailSummary:
    out: GuardrailSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GuardrailSummary.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GuardrailSummary.arn required")
    if "status" in data:
        import aws_sdk_bedrock.types.guardrail_status

        out["status"] = aws_sdk_bedrock.types.guardrail_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("GuardrailSummary.status required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GuardrailSummary.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("GuardrailSummary.version required")
    if "createdAt" in data:
        import aws_sdk_bedrock.types.timestamp

        out["created_at"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GuardrailSummary.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bedrock.types.timestamp

        out["updated_at"] = aws_sdk_bedrock.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("GuardrailSummary.updated_at required")
    if "crossRegionDetails" in data:
        import aws_sdk_bedrock.types.guardrail_cross_region_details

        out["cross_region_details"] = (
            aws_sdk_bedrock.types.guardrail_cross_region_details.deserialize_json(
                data["crossRegionDetails"]
            )
        )
    return out
