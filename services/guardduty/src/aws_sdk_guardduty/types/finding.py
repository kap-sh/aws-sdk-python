"""Generated from Smithy shape ``com.amazonaws.guardduty#Finding``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.double
    import aws_sdk_guardduty.types.finding_type
    import aws_sdk_guardduty.types.resource
    import aws_sdk_guardduty.types.service
    import aws_sdk_guardduty.types.string


class Finding(TypedDict):
    account_id: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The ID of the account in which the finding was generated.</p>"""
    arn: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The ARN of the finding.</p>"""
    confidence: NotRequired["aws_sdk_guardduty.types.double.Double"]
    """<p>The confidence score for the finding.</p>"""
    created_at: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The time and date when the finding was created.</p>"""
    description: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The description of the finding.</p>"""
    id: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The ID of the finding.</p>"""
    partition: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The partition associated with the finding.</p>"""
    region: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The Region where the finding was generated. For findings generated from <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-global-service-events\">Global Service Events</a>, the Region value in the finding might differ from the Region where GuardDuty identifies the potential threat. For more information, see <a href=\"https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_data-sources.html#cloudtrail_global\">How GuardDuty handles Amazon Web Services CloudTrail global events</a> in the <i>Amazon GuardDuty User Guide</i>.</p>"""
    resource: NotRequired["aws_sdk_guardduty.types.resource.Resource"]
    schema_version: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The version of the schema used for the finding.</p>"""
    service: NotRequired["aws_sdk_guardduty.types.service.Service"]
    severity: NotRequired["aws_sdk_guardduty.types.double.Double"]
    """<p>The severity of the finding.</p>"""
    title: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The title of the finding.</p>"""
    type: NotRequired["aws_sdk_guardduty.types.finding_type.FindingType"]
    """<p>The type of finding.</p>"""
    updated_at: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The time and date when the finding was last updated.</p>"""
    associated_attack_sequence_arn: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>Amazon Resource Name (ARN) associated with the attack sequence finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Finding) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "confidence" in value:
        out["confidence"] = value["confidence"]
    if "created_at" in value:
        out["createdAt"] = value["created_at"]
    if "description" in value:
        out["description"] = value["description"]
    if "id" in value:
        out["id"] = value["id"]
    if "partition" in value:
        out["partition"] = value["partition"]
    if "region" in value:
        out["region"] = value["region"]
    if "resource" in value:
        import aws_sdk_guardduty.types.resource

        out["resource"] = aws_sdk_guardduty.types.resource.serialize_json(
            value["resource"]
        )
    if "schema_version" in value:
        out["schemaVersion"] = value["schema_version"]
    if "service" in value:
        import aws_sdk_guardduty.types.service

        out["service"] = aws_sdk_guardduty.types.service.serialize_json(
            value["service"]
        )
    if "severity" in value:
        out["severity"] = value["severity"]
    if "title" in value:
        out["title"] = value["title"]
    if "type" in value:
        out["type"] = value["type"]
    if "updated_at" in value:
        out["updatedAt"] = value["updated_at"]
    if "associated_attack_sequence_arn" in value:
        out["associatedAttackSequenceArn"] = value["associated_attack_sequence_arn"]
    return out


def deserialize_json(data: dict) -> Finding:
    out: Finding = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "confidence" in data:
        out["confidence"] = data["confidence"]
    if "createdAt" in data:
        out["created_at"] = data["createdAt"]
    if "description" in data:
        out["description"] = data["description"]
    if "id" in data:
        out["id"] = data["id"]
    if "partition" in data:
        out["partition"] = data["partition"]
    if "region" in data:
        out["region"] = data["region"]
    if "resource" in data:
        import aws_sdk_guardduty.types.resource

        out["resource"] = aws_sdk_guardduty.types.resource.deserialize_json(
            data["resource"]
        )
    if "schemaVersion" in data:
        out["schema_version"] = data["schemaVersion"]
    if "service" in data:
        import aws_sdk_guardduty.types.service

        out["service"] = aws_sdk_guardduty.types.service.deserialize_json(
            data["service"]
        )
    if "severity" in data:
        out["severity"] = data["severity"]
    if "title" in data:
        out["title"] = data["title"]
    if "type" in data:
        out["type"] = data["type"]
    if "updatedAt" in data:
        out["updated_at"] = data["updatedAt"]
    if "associatedAttackSequenceArn" in data:
        out["associated_attack_sequence_arn"] = data["associatedAttackSequenceArn"]
    return out
