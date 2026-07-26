"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CheckDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.aws_account_id
    import capo_wellarchitected.types.check_description
    import capo_wellarchitected.types.check_failure_reason
    import capo_wellarchitected.types.check_id
    import capo_wellarchitected.types.check_name
    import capo_wellarchitected.types.check_provider
    import capo_wellarchitected.types.check_status
    import capo_wellarchitected.types.choice_id
    import capo_wellarchitected.types.flagged_resources
    import capo_wellarchitected.types.lens_arn
    import capo_wellarchitected.types.pillar_id
    import capo_wellarchitected.types.question_id
    import capo_wellarchitected.types.timestamp


class CheckDetail(TypedDict, closed=True):
    id: NotRequired["capo_wellarchitected.types.check_id.CheckId"]
    """<p>Trusted Advisor check ID.</p>"""
    name: NotRequired["capo_wellarchitected.types.check_name.CheckName"]
    """<p>Trusted Advisor check name.</p>"""
    description: NotRequired[
        "capo_wellarchitected.types.check_description.CheckDescription"
    ]
    """<p>Trusted Advisor check description.</p>"""
    provider: NotRequired["capo_wellarchitected.types.check_provider.CheckProvider"]
    """<p>Provider of the check related to the best practice.</p>"""
    lens_arn: NotRequired["capo_wellarchitected.types.lens_arn.LensArn"]
    """<p>Well-Architected Lens ARN associated to the check.</p>"""
    pillar_id: NotRequired["capo_wellarchitected.types.pillar_id.PillarId"]
    question_id: NotRequired["capo_wellarchitected.types.question_id.QuestionId"]
    choice_id: NotRequired["capo_wellarchitected.types.choice_id.ChoiceId"]
    status: NotRequired["capo_wellarchitected.types.check_status.CheckStatus"]
    """<p>Status associated to the check.</p>"""
    account_id: NotRequired["capo_wellarchitected.types.aws_account_id.AwsAccountId"]
    flagged_resources: NotRequired[
        "capo_wellarchitected.types.flagged_resources.FlaggedResources"
    ]
    """<p>Count of flagged resources associated to the check.</p>"""
    reason: NotRequired[
        "capo_wellarchitected.types.check_failure_reason.CheckFailureReason"
    ]
    """<p>Reason associated to the check.</p>"""
    updated_at: NotRequired["capo_wellarchitected.types.timestamp.Timestamp"]


# --- restJson1 ser/de ---
def serialize_json(value: CheckDetail) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "provider" in value:
        import capo_wellarchitected.types.check_provider

        out["Provider"] = capo_wellarchitected.types.check_provider.serialize_json(
            value["provider"]
        )
    if "lens_arn" in value:
        out["LensArn"] = value["lens_arn"]
    if "pillar_id" in value:
        out["PillarId"] = value["pillar_id"]
    if "question_id" in value:
        out["QuestionId"] = value["question_id"]
    if "choice_id" in value:
        out["ChoiceId"] = value["choice_id"]
    if "status" in value:
        import capo_wellarchitected.types.check_status

        out["Status"] = capo_wellarchitected.types.check_status.serialize_json(
            value["status"]
        )
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "flagged_resources" in value:
        out["FlaggedResources"] = value["flagged_resources"]
    if "reason" in value:
        import capo_wellarchitected.types.check_failure_reason

        out["Reason"] = capo_wellarchitected.types.check_failure_reason.serialize_json(
            value["reason"]
        )
    if "updated_at" in value:
        import capo_wellarchitected.types.timestamp

        out["UpdatedAt"] = capo_wellarchitected.types.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> CheckDetail:
    out: CheckDetail = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Provider" in data:
        import capo_wellarchitected.types.check_provider

        out["provider"] = capo_wellarchitected.types.check_provider.deserialize_json(
            data["Provider"]
        )
    if "LensArn" in data:
        out["lens_arn"] = data["LensArn"]
    if "PillarId" in data:
        out["pillar_id"] = data["PillarId"]
    if "QuestionId" in data:
        out["question_id"] = data["QuestionId"]
    if "ChoiceId" in data:
        out["choice_id"] = data["ChoiceId"]
    if "Status" in data:
        import capo_wellarchitected.types.check_status

        out["status"] = capo_wellarchitected.types.check_status.deserialize_json(
            data["Status"]
        )
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "FlaggedResources" in data:
        out["flagged_resources"] = data["FlaggedResources"]
    if "Reason" in data:
        import capo_wellarchitected.types.check_failure_reason

        out["reason"] = (
            capo_wellarchitected.types.check_failure_reason.deserialize_json(
                data["Reason"]
            )
        )
    if "UpdatedAt" in data:
        import capo_wellarchitected.types.timestamp

        out["updated_at"] = capo_wellarchitected.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    return out
