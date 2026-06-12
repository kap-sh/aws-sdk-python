"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormContent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.evaluation_form_auto_evaluation_configuration
    import aws_sdk_connect.types.evaluation_form_description
    import aws_sdk_connect.types.evaluation_form_items_list
    import aws_sdk_connect.types.evaluation_form_language_configuration
    import aws_sdk_connect.types.evaluation_form_scoring_strategy
    import aws_sdk_connect.types.evaluation_form_target_configuration
    import aws_sdk_connect.types.evaluation_form_title
    import aws_sdk_connect.types.evaluation_review_configuration
    import aws_sdk_connect.types.resource_id
    import aws_sdk_connect.types.version_number


class EvaluationFormContent(TypedDict):
    evaluation_form_version: "aws_sdk_connect.types.version_number.VersionNumber"
    """<p>A version of the evaluation form.</p>"""
    evaluation_form_id: "aws_sdk_connect.types.resource_id.ResourceId"
    """<p>The unique identifier for the evaluation form.</p>"""
    evaluation_form_arn: "aws_sdk_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) for the evaluation form resource.</p>"""
    title: "aws_sdk_connect.types.evaluation_form_title.EvaluationFormTitle"
    """<p>A title of the evaluation form.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.evaluation_form_description.EvaluationFormDescription"
    ]
    """<p>The description of the evaluation form.</p>"""
    items: "aws_sdk_connect.types.evaluation_form_items_list.EvaluationFormItemsList"
    """<p>Items that are part of the evaluation form. The total number of sections and questions must not exceed 100 each. Questions must be contained in a section.</p>"""
    scoring_strategy: NotRequired[
        "aws_sdk_connect.types.evaluation_form_scoring_strategy.EvaluationFormScoringStrategy"
    ]
    """<p>A scoring strategy of the evaluation form.</p>"""
    auto_evaluation_configuration: NotRequired[
        "aws_sdk_connect.types.evaluation_form_auto_evaluation_configuration.EvaluationFormAutoEvaluationConfiguration"
    ]
    """<p>The configuration of the automated evaluation.</p>"""
    target_configuration: NotRequired[
        "aws_sdk_connect.types.evaluation_form_target_configuration.EvaluationFormTargetConfiguration"
    ]
    """<p>Configuration that specifies the target for this evaluation form content.</p>"""
    language_configuration: NotRequired[
        "aws_sdk_connect.types.evaluation_form_language_configuration.EvaluationFormLanguageConfiguration"
    ]
    """<p>Configuration for language settings of this evaluation form content.</p>"""
    review_configuration: NotRequired[
        "aws_sdk_connect.types.evaluation_review_configuration.EvaluationReviewConfiguration"
    ]
    """<p>Configuration for evaluation review settings of this evaluation form content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormContent) -> dict:
    out: dict = {}
    out["EvaluationFormVersion"] = value.get("evaluation_form_version", 0)
    out["EvaluationFormId"] = value["evaluation_form_id"]
    out["EvaluationFormArn"] = value["evaluation_form_arn"]
    out["Title"] = value["title"]
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_connect.types.evaluation_form_items_list

    out["Items"] = aws_sdk_connect.types.evaluation_form_items_list.serialize_json(
        value["items"]
    )
    if "scoring_strategy" in value:
        import aws_sdk_connect.types.evaluation_form_scoring_strategy

        out["ScoringStrategy"] = (
            aws_sdk_connect.types.evaluation_form_scoring_strategy.serialize_json(
                value["scoring_strategy"]
            )
        )
    if "auto_evaluation_configuration" in value:
        import aws_sdk_connect.types.evaluation_form_auto_evaluation_configuration

        out["AutoEvaluationConfiguration"] = (
            aws_sdk_connect.types.evaluation_form_auto_evaluation_configuration.serialize_json(
                value["auto_evaluation_configuration"]
            )
        )
    if "target_configuration" in value:
        import aws_sdk_connect.types.evaluation_form_target_configuration

        out["TargetConfiguration"] = (
            aws_sdk_connect.types.evaluation_form_target_configuration.serialize_json(
                value["target_configuration"]
            )
        )
    if "language_configuration" in value:
        import aws_sdk_connect.types.evaluation_form_language_configuration

        out["LanguageConfiguration"] = (
            aws_sdk_connect.types.evaluation_form_language_configuration.serialize_json(
                value["language_configuration"]
            )
        )
    if "review_configuration" in value:
        import aws_sdk_connect.types.evaluation_review_configuration

        out["ReviewConfiguration"] = (
            aws_sdk_connect.types.evaluation_review_configuration.serialize_json(
                value["review_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationFormContent:
    out: EvaluationFormContent = {}  # type: ignore[typeddict-item]
    if "EvaluationFormVersion" in data:
        out["evaluation_form_version"] = data["EvaluationFormVersion"]
    else:
        out["evaluation_form_version"] = 0
    if "EvaluationFormId" in data:
        out["evaluation_form_id"] = data["EvaluationFormId"]
    else:
        raise DeserializationError("EvaluationFormContent.evaluation_form_id required")
    if "EvaluationFormArn" in data:
        out["evaluation_form_arn"] = data["EvaluationFormArn"]
    else:
        raise DeserializationError("EvaluationFormContent.evaluation_form_arn required")
    if "Title" in data:
        out["title"] = data["Title"]
    else:
        raise DeserializationError("EvaluationFormContent.title required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Items" in data:
        import aws_sdk_connect.types.evaluation_form_items_list

        out["items"] = (
            aws_sdk_connect.types.evaluation_form_items_list.deserialize_json(
                data["Items"]
            )
        )
    else:
        raise DeserializationError("EvaluationFormContent.items required")
    if "ScoringStrategy" in data:
        import aws_sdk_connect.types.evaluation_form_scoring_strategy

        out["scoring_strategy"] = (
            aws_sdk_connect.types.evaluation_form_scoring_strategy.deserialize_json(
                data["ScoringStrategy"]
            )
        )
    if "AutoEvaluationConfiguration" in data:
        import aws_sdk_connect.types.evaluation_form_auto_evaluation_configuration

        out["auto_evaluation_configuration"] = (
            aws_sdk_connect.types.evaluation_form_auto_evaluation_configuration.deserialize_json(
                data["AutoEvaluationConfiguration"]
            )
        )
    if "TargetConfiguration" in data:
        import aws_sdk_connect.types.evaluation_form_target_configuration

        out["target_configuration"] = (
            aws_sdk_connect.types.evaluation_form_target_configuration.deserialize_json(
                data["TargetConfiguration"]
            )
        )
    if "LanguageConfiguration" in data:
        import aws_sdk_connect.types.evaluation_form_language_configuration

        out["language_configuration"] = (
            aws_sdk_connect.types.evaluation_form_language_configuration.deserialize_json(
                data["LanguageConfiguration"]
            )
        )
    if "ReviewConfiguration" in data:
        import aws_sdk_connect.types.evaluation_review_configuration

        out["review_configuration"] = (
            aws_sdk_connect.types.evaluation_review_configuration.deserialize_json(
                data["ReviewConfiguration"]
            )
        )
    return out
