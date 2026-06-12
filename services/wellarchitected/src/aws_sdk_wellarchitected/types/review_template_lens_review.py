"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ReviewTemplateLensReview``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.lens_alias
    import aws_sdk_wellarchitected.types.lens_arn
    import aws_sdk_wellarchitected.types.lens_name
    import aws_sdk_wellarchitected.types.lens_status
    import aws_sdk_wellarchitected.types.lens_version
    import aws_sdk_wellarchitected.types.next_token
    import aws_sdk_wellarchitected.types.notes
    import aws_sdk_wellarchitected.types.question_counts
    import aws_sdk_wellarchitected.types.review_template_pillar_review_summaries
    import aws_sdk_wellarchitected.types.timestamp


class ReviewTemplateLensReview(TypedDict):
    lens_alias: NotRequired["aws_sdk_wellarchitected.types.lens_alias.LensAlias"]
    lens_arn: NotRequired["aws_sdk_wellarchitected.types.lens_arn.LensArn"]
    """<p>The lens ARN.</p>"""
    lens_version: NotRequired["aws_sdk_wellarchitected.types.lens_version.LensVersion"]
    """<p>The version of the lens.</p>"""
    lens_name: NotRequired["aws_sdk_wellarchitected.types.lens_name.LensName"]
    lens_status: NotRequired["aws_sdk_wellarchitected.types.lens_status.LensStatus"]
    """<p>The status of the lens.</p>"""
    pillar_review_summaries: NotRequired[
        "aws_sdk_wellarchitected.types.review_template_pillar_review_summaries.ReviewTemplatePillarReviewSummaries"
    ]
    """<p>Pillar review summaries of a lens review.</p>"""
    updated_at: NotRequired["aws_sdk_wellarchitected.types.timestamp.Timestamp"]
    notes: NotRequired["aws_sdk_wellarchitected.types.notes.Notes"]
    question_counts: NotRequired[
        "aws_sdk_wellarchitected.types.question_counts.QuestionCounts"
    ]
    """<p>A count of how many questions are answered and unanswered in the lens review.</p>"""
    next_token: NotRequired["aws_sdk_wellarchitected.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ReviewTemplateLensReview) -> dict:
    out: dict = {}
    if "lens_alias" in value:
        out["LensAlias"] = value["lens_alias"]
    if "lens_arn" in value:
        out["LensArn"] = value["lens_arn"]
    if "lens_version" in value:
        out["LensVersion"] = value["lens_version"]
    if "lens_name" in value:
        out["LensName"] = value["lens_name"]
    if "lens_status" in value:
        import aws_sdk_wellarchitected.types.lens_status

        out["LensStatus"] = aws_sdk_wellarchitected.types.lens_status.serialize_json(
            value["lens_status"]
        )
    if "pillar_review_summaries" in value:
        import aws_sdk_wellarchitected.types.review_template_pillar_review_summaries

        out["PillarReviewSummaries"] = (
            aws_sdk_wellarchitected.types.review_template_pillar_review_summaries.serialize_json(
                value["pillar_review_summaries"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_wellarchitected.types.timestamp

        out["UpdatedAt"] = aws_sdk_wellarchitected.types.timestamp.serialize_json(
            value["updated_at"]
        )
    if "notes" in value:
        out["Notes"] = value["notes"]
    if "question_counts" in value:
        import aws_sdk_wellarchitected.types.question_counts

        out["QuestionCounts"] = (
            aws_sdk_wellarchitected.types.question_counts.serialize_json(
                value["question_counts"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ReviewTemplateLensReview:
    out: ReviewTemplateLensReview = {}  # type: ignore[typeddict-item]
    if "LensAlias" in data:
        out["lens_alias"] = data["LensAlias"]
    if "LensArn" in data:
        out["lens_arn"] = data["LensArn"]
    if "LensVersion" in data:
        out["lens_version"] = data["LensVersion"]
    if "LensName" in data:
        out["lens_name"] = data["LensName"]
    if "LensStatus" in data:
        import aws_sdk_wellarchitected.types.lens_status

        out["lens_status"] = aws_sdk_wellarchitected.types.lens_status.deserialize_json(
            data["LensStatus"]
        )
    if "PillarReviewSummaries" in data:
        import aws_sdk_wellarchitected.types.review_template_pillar_review_summaries

        out["pillar_review_summaries"] = (
            aws_sdk_wellarchitected.types.review_template_pillar_review_summaries.deserialize_json(
                data["PillarReviewSummaries"]
            )
        )
    if "UpdatedAt" in data:
        import aws_sdk_wellarchitected.types.timestamp

        out["updated_at"] = aws_sdk_wellarchitected.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    if "Notes" in data:
        out["notes"] = data["Notes"]
    if "QuestionCounts" in data:
        import aws_sdk_wellarchitected.types.question_counts

        out["question_counts"] = (
            aws_sdk_wellarchitected.types.question_counts.deserialize_json(
                data["QuestionCounts"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
