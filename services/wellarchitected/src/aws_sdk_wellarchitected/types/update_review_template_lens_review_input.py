"""Generated from Smithy shape ``com.amazonaws.wellarchitected#UpdateReviewTemplateLensReviewInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.lens_alias
    import aws_sdk_wellarchitected.types.notes
    import aws_sdk_wellarchitected.types.pillar_notes
    import aws_sdk_wellarchitected.types.template_arn


class UpdateReviewTemplateLensReviewInput(TypedDict, closed=True):
    template_arn: "aws_sdk_wellarchitected.types.template_arn.TemplateArn"
    """<p>The review template ARN.</p>"""
    lens_alias: "aws_sdk_wellarchitected.types.lens_alias.LensAlias"
    lens_notes: NotRequired["aws_sdk_wellarchitected.types.notes.Notes"]
    pillar_notes: NotRequired["aws_sdk_wellarchitected.types.pillar_notes.PillarNotes"]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateReviewTemplateLensReviewInput) -> dict:
    out: dict = {}
    if "lens_notes" in value:
        out["LensNotes"] = value["lens_notes"]
    if "pillar_notes" in value:
        import aws_sdk_wellarchitected.types.pillar_notes

        out["PillarNotes"] = aws_sdk_wellarchitected.types.pillar_notes.serialize_json(
            value["pillar_notes"]
        )
    return out


def deserialize_json(data: dict) -> UpdateReviewTemplateLensReviewInput:
    out: UpdateReviewTemplateLensReviewInput = {}  # type: ignore[typeddict-item]
    if "LensNotes" in data:
        out["lens_notes"] = data["LensNotes"]
    if "PillarNotes" in data:
        import aws_sdk_wellarchitected.types.pillar_notes

        out["pillar_notes"] = (
            aws_sdk_wellarchitected.types.pillar_notes.deserialize_json(
                data["PillarNotes"]
            )
        )
    return out
