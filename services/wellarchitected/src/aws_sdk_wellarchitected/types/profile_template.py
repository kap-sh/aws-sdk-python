"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ProfileTemplate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.profile_name
    import aws_sdk_wellarchitected.types.template_questions
    import aws_sdk_wellarchitected.types.timestamp


class ProfileTemplate(TypedDict, closed=True):
    template_name: NotRequired["aws_sdk_wellarchitected.types.profile_name.ProfileName"]
    """<p>The name of the profile template.</p>"""
    template_questions: NotRequired[
        "aws_sdk_wellarchitected.types.template_questions.TemplateQuestions"
    ]
    """<p>Profile template questions.</p>"""
    created_at: NotRequired["aws_sdk_wellarchitected.types.timestamp.Timestamp"]
    updated_at: NotRequired["aws_sdk_wellarchitected.types.timestamp.Timestamp"]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileTemplate) -> dict:
    out: dict = {}
    if "template_name" in value:
        out["TemplateName"] = value["template_name"]
    if "template_questions" in value:
        import aws_sdk_wellarchitected.types.template_questions

        out["TemplateQuestions"] = (
            aws_sdk_wellarchitected.types.template_questions.serialize_json(
                value["template_questions"]
            )
        )
    if "created_at" in value:
        import aws_sdk_wellarchitected.types.timestamp

        out["CreatedAt"] = aws_sdk_wellarchitected.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import aws_sdk_wellarchitected.types.timestamp

        out["UpdatedAt"] = aws_sdk_wellarchitected.types.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> ProfileTemplate:
    out: ProfileTemplate = {}  # type: ignore[typeddict-item]
    if "TemplateName" in data:
        out["template_name"] = data["TemplateName"]
    if "TemplateQuestions" in data:
        import aws_sdk_wellarchitected.types.template_questions

        out["template_questions"] = (
            aws_sdk_wellarchitected.types.template_questions.deserialize_json(
                data["TemplateQuestions"]
            )
        )
    if "CreatedAt" in data:
        import aws_sdk_wellarchitected.types.timestamp

        out["created_at"] = aws_sdk_wellarchitected.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if "UpdatedAt" in data:
        import aws_sdk_wellarchitected.types.timestamp

        out["updated_at"] = aws_sdk_wellarchitected.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    return out
