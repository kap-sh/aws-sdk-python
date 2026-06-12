"""Generated from Smithy shape ``com.amazonaws.macie2#Finding``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__boolean
    import aws_sdk_macie2.types.__long
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.__timestamp_iso8601
    import aws_sdk_macie2.types.classification_details
    import aws_sdk_macie2.types.finding_category
    import aws_sdk_macie2.types.finding_type
    import aws_sdk_macie2.types.policy_details
    import aws_sdk_macie2.types.resources_affected
    import aws_sdk_macie2.types.severity


class Finding(TypedDict):
    account_id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The unique identifier for the Amazon Web Services account that the finding applies to. This is typically the account that owns the affected resource.</p>"""
    archived: NotRequired["aws_sdk_macie2.types.__boolean.__boolean"]
    """<p>Specifies whether the finding is archived (suppressed).</p>"""
    category: NotRequired["aws_sdk_macie2.types.finding_category.FindingCategory"]
    """<p>The category of the finding. Possible values are: CLASSIFICATION, for a sensitive data finding; and, POLICY, for a policy finding.</p>"""
    classification_details: NotRequired[
        "aws_sdk_macie2.types.classification_details.ClassificationDetails"
    ]
    """<p>The details of a sensitive data finding. This value is null for a policy finding.</p>"""
    count: NotRequired["aws_sdk_macie2.types.__long.__long"]
    """<p>The total number of occurrences of the finding. For sensitive data findings, this value is always 1. All sensitive data findings are considered unique.</p>"""
    created_at: NotRequired[
        "aws_sdk_macie2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The date and time, in UTC and extended ISO 8601 format, when Amazon Macie created the finding.</p>"""
    description: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The description of the finding.</p>"""
    id: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The unique identifier for the finding. This is a random string that Amazon Macie generates and assigns to a finding when it creates the finding.</p>"""
    partition: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The Amazon Web Services partition that Amazon Macie created the finding in.</p>"""
    policy_details: NotRequired["aws_sdk_macie2.types.policy_details.PolicyDetails"]
    """<p>The details of a policy finding. This value is null for a sensitive data finding.</p>"""
    region: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The Amazon Web Services Region that Amazon Macie created the finding in.</p>"""
    resources_affected: NotRequired[
        "aws_sdk_macie2.types.resources_affected.ResourcesAffected"
    ]
    """<p>The resources that the finding applies to.</p>"""
    sample: NotRequired["aws_sdk_macie2.types.__boolean.__boolean"]
    """<p>Specifies whether the finding is a sample finding. A <i>sample finding</i> is a finding that uses example data to demonstrate what a finding might contain.</p>"""
    schema_version: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The version of the schema that was used to define the data structures in the finding.</p>"""
    severity: NotRequired["aws_sdk_macie2.types.severity.Severity"]
    """<p>The severity level and score for the finding.</p>"""
    title: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The brief description of the finding.</p>"""
    type: NotRequired["aws_sdk_macie2.types.finding_type.FindingType"]
    """<p>The type of the finding.</p>"""
    updated_at: NotRequired[
        "aws_sdk_macie2.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The date and time, in UTC and extended ISO 8601 format, when Amazon Macie last updated the finding. For sensitive data findings, this value is the same as the value for the createdAt property. All sensitive data findings are considered new.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Finding) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "archived" in value:
        out["archived"] = value["archived"]
    if "category" in value:
        import aws_sdk_macie2.types.finding_category

        out["category"] = aws_sdk_macie2.types.finding_category.serialize_json(
            value["category"]
        )
    if "classification_details" in value:
        import aws_sdk_macie2.types.classification_details

        out["classificationDetails"] = (
            aws_sdk_macie2.types.classification_details.serialize_json(
                value["classification_details"]
            )
        )
    if "count" in value:
        out["count"] = value["count"]
    if "created_at" in value:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["createdAt"] = aws_sdk_macie2.types.__timestamp_iso8601.serialize_json(
            value["created_at"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "id" in value:
        out["id"] = value["id"]
    if "partition" in value:
        out["partition"] = value["partition"]
    if "policy_details" in value:
        import aws_sdk_macie2.types.policy_details

        out["policyDetails"] = aws_sdk_macie2.types.policy_details.serialize_json(
            value["policy_details"]
        )
    if "region" in value:
        out["region"] = value["region"]
    if "resources_affected" in value:
        import aws_sdk_macie2.types.resources_affected

        out["resourcesAffected"] = (
            aws_sdk_macie2.types.resources_affected.serialize_json(
                value["resources_affected"]
            )
        )
    if "sample" in value:
        out["sample"] = value["sample"]
    if "schema_version" in value:
        out["schemaVersion"] = value["schema_version"]
    if "severity" in value:
        import aws_sdk_macie2.types.severity

        out["severity"] = aws_sdk_macie2.types.severity.serialize_json(
            value["severity"]
        )
    if "title" in value:
        out["title"] = value["title"]
    if "type" in value:
        import aws_sdk_macie2.types.finding_type

        out["type"] = aws_sdk_macie2.types.finding_type.serialize_json(value["type"])
    if "updated_at" in value:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["updatedAt"] = aws_sdk_macie2.types.__timestamp_iso8601.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> Finding:
    out: Finding = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "archived" in data:
        out["archived"] = data["archived"]
    if "category" in data:
        import aws_sdk_macie2.types.finding_category

        out["category"] = aws_sdk_macie2.types.finding_category.deserialize_json(
            data["category"]
        )
    if "classificationDetails" in data:
        import aws_sdk_macie2.types.classification_details

        out["classification_details"] = (
            aws_sdk_macie2.types.classification_details.deserialize_json(
                data["classificationDetails"]
            )
        )
    if "count" in data:
        out["count"] = data["count"]
    if "createdAt" in data:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["created_at"] = aws_sdk_macie2.types.__timestamp_iso8601.deserialize_json(
            data["createdAt"]
        )
    if "description" in data:
        out["description"] = data["description"]
    if "id" in data:
        out["id"] = data["id"]
    if "partition" in data:
        out["partition"] = data["partition"]
    if "policyDetails" in data:
        import aws_sdk_macie2.types.policy_details

        out["policy_details"] = aws_sdk_macie2.types.policy_details.deserialize_json(
            data["policyDetails"]
        )
    if "region" in data:
        out["region"] = data["region"]
    if "resourcesAffected" in data:
        import aws_sdk_macie2.types.resources_affected

        out["resources_affected"] = (
            aws_sdk_macie2.types.resources_affected.deserialize_json(
                data["resourcesAffected"]
            )
        )
    if "sample" in data:
        out["sample"] = data["sample"]
    if "schemaVersion" in data:
        out["schema_version"] = data["schemaVersion"]
    if "severity" in data:
        import aws_sdk_macie2.types.severity

        out["severity"] = aws_sdk_macie2.types.severity.deserialize_json(
            data["severity"]
        )
    if "title" in data:
        out["title"] = data["title"]
    if "type" in data:
        import aws_sdk_macie2.types.finding_type

        out["type"] = aws_sdk_macie2.types.finding_type.deserialize_json(data["type"])
    if "updatedAt" in data:
        import aws_sdk_macie2.types.__timestamp_iso8601

        out["updated_at"] = aws_sdk_macie2.types.__timestamp_iso8601.deserialize_json(
            data["updatedAt"]
        )
    return out
