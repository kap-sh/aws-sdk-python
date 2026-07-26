"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CheckSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.account_summary
    import capo_wellarchitected.types.check_description
    import capo_wellarchitected.types.check_id
    import capo_wellarchitected.types.check_name
    import capo_wellarchitected.types.check_provider
    import capo_wellarchitected.types.check_status
    import capo_wellarchitected.types.choice_id
    import capo_wellarchitected.types.lens_arn
    import capo_wellarchitected.types.pillar_id
    import capo_wellarchitected.types.question_id
    import capo_wellarchitected.types.timestamp


class CheckSummary(TypedDict, closed=True):
    id: NotRequired["capo_wellarchitected.types.check_id.CheckId"]
    """<p>Trusted Advisor check ID.</p>"""
    name: NotRequired["capo_wellarchitected.types.check_name.CheckName"]
    """<p>Trusted Advisor check name.</p>"""
    provider: NotRequired["capo_wellarchitected.types.check_provider.CheckProvider"]
    """<p>Provider of the check related to the best practice.</p>"""
    description: NotRequired[
        "capo_wellarchitected.types.check_description.CheckDescription"
    ]
    """<p>Trusted Advisor check description.</p>"""
    updated_at: NotRequired["capo_wellarchitected.types.timestamp.Timestamp"]
    lens_arn: NotRequired["capo_wellarchitected.types.lens_arn.LensArn"]
    """<p>Well-Architected Lens ARN associated to the check.</p>"""
    pillar_id: NotRequired["capo_wellarchitected.types.pillar_id.PillarId"]
    question_id: NotRequired["capo_wellarchitected.types.question_id.QuestionId"]
    choice_id: NotRequired["capo_wellarchitected.types.choice_id.ChoiceId"]
    status: NotRequired["capo_wellarchitected.types.check_status.CheckStatus"]
    """<p>Status associated to the check.</p>"""
    account_summary: NotRequired[
        "capo_wellarchitected.types.account_summary.AccountSummary"
    ]
    """<p>Account summary associated to the check.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CheckSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "provider" in value:
        import capo_wellarchitected.types.check_provider

        out["Provider"] = capo_wellarchitected.types.check_provider.serialize_json(
            value["provider"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "updated_at" in value:
        import capo_wellarchitected.types.timestamp

        out["UpdatedAt"] = capo_wellarchitected.types.timestamp.serialize_json(
            value["updated_at"]
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
    if "account_summary" in value:
        import capo_wellarchitected.types.account_summary

        out["AccountSummary"] = (
            capo_wellarchitected.types.account_summary.serialize_json(
                value["account_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> CheckSummary:
    out: CheckSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Provider" in data:
        import capo_wellarchitected.types.check_provider

        out["provider"] = capo_wellarchitected.types.check_provider.deserialize_json(
            data["Provider"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "UpdatedAt" in data:
        import capo_wellarchitected.types.timestamp

        out["updated_at"] = capo_wellarchitected.types.timestamp.deserialize_json(
            data["UpdatedAt"]
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
    if "AccountSummary" in data:
        import capo_wellarchitected.types.account_summary

        out["account_summary"] = (
            capo_wellarchitected.types.account_summary.deserialize_json(
                data["AccountSummary"]
            )
        )
    return out
