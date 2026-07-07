"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationForm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

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
    import aws_sdk_connect.types.evaluation_form_version_is_locked
    import aws_sdk_connect.types.evaluation_form_version_status
    import aws_sdk_connect.types.evaluation_review_configuration
    import aws_sdk_connect.types.resource_id
    import aws_sdk_connect.types.tag_map
    import aws_sdk_connect.types.timestamp
    import aws_sdk_connect.types.version_number


class EvaluationForm(TypedDict, closed=True):
    evaluation_form_id: "aws_sdk_connect.types.resource_id.ResourceId"
    """<p>The unique identifier for the evaluation form.</p>"""
    evaluation_form_version: "aws_sdk_connect.types.version_number.VersionNumber"
    """<p>A version of the evaluation form.</p>"""
    locked: "aws_sdk_connect.types.evaluation_form_version_is_locked.EvaluationFormVersionIsLocked"
    """<p>The flag indicating whether the evaluation form is locked for changes.</p>"""
    evaluation_form_arn: "aws_sdk_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) for the evaluation form resource.</p>"""
    title: "aws_sdk_connect.types.evaluation_form_title.EvaluationFormTitle"
    """<p>A title of the evaluation form.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.evaluation_form_description.EvaluationFormDescription"
    ]
    """<p>The description of the evaluation form.</p>"""
    status: "aws_sdk_connect.types.evaluation_form_version_status.EvaluationFormVersionStatus"
    """<p>The status of the evaluation form.</p>"""
    items: "aws_sdk_connect.types.evaluation_form_items_list.EvaluationFormItemsList"
    """<p>Items that are part of the evaluation form. The total number of sections and questions must not exceed 100 each. Questions must be contained in a section.</p>"""
    scoring_strategy: NotRequired[
        "aws_sdk_connect.types.evaluation_form_scoring_strategy.EvaluationFormScoringStrategy"
    ]
    """<p>A scoring strategy of the evaluation form.</p>"""
    created_time: "aws_sdk_connect.types.timestamp.Timestamp"
    """<p>The timestamp for when the evaluation form was created.</p>"""
    created_by: "aws_sdk_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the user who created the evaluation form.</p>"""
    last_modified_time: "aws_sdk_connect.types.timestamp.Timestamp"
    """<p>The timestamp for when the evaluation form was last updated.</p>"""
    last_modified_by: "aws_sdk_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the user who last updated the evaluation form.</p>"""
    auto_evaluation_configuration: NotRequired[
        "aws_sdk_connect.types.evaluation_form_auto_evaluation_configuration.EvaluationFormAutoEvaluationConfiguration"
    ]
    """<p>The automatic evaluation configuration of an evaluation form.</p>"""
    review_configuration: NotRequired[
        "aws_sdk_connect.types.evaluation_review_configuration.EvaluationReviewConfiguration"
    ]
    """<p>Configuration for evaluation review settings of this evaluation form.</p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    r"""<p>The tags used to organize, track, or control access for this resource. For example, { \"Tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""
    target_configuration: NotRequired[
        "aws_sdk_connect.types.evaluation_form_target_configuration.EvaluationFormTargetConfiguration"
    ]
    """<p>Configuration that specifies the target for this evaluation form.</p>"""
    language_configuration: NotRequired[
        "aws_sdk_connect.types.evaluation_form_language_configuration.EvaluationFormLanguageConfiguration"
    ]
    """<p>Configuration for language settings of this evaluation form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationForm) -> dict:
    out: dict = {}
    out["EvaluationFormId"] = value["evaluation_form_id"]
    out["EvaluationFormVersion"] = value.get("evaluation_form_version", 0)
    out["Locked"] = value.get("locked", False)
    out["EvaluationFormArn"] = value["evaluation_form_arn"]
    out["Title"] = value["title"]
    if "description" in value:
        out["Description"] = value["description"]
    import aws_sdk_connect.types.evaluation_form_version_status

    out["Status"] = aws_sdk_connect.types.evaluation_form_version_status.serialize_json(
        value["status"]
    )
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
    import aws_sdk_connect.types.timestamp

    out["CreatedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
        value["created_time"]
    )
    out["CreatedBy"] = value["created_by"]
    import aws_sdk_connect.types.timestamp

    out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
        value["last_modified_time"]
    )
    out["LastModifiedBy"] = value["last_modified_by"]
    if "auto_evaluation_configuration" in value:
        import aws_sdk_connect.types.evaluation_form_auto_evaluation_configuration

        out["AutoEvaluationConfiguration"] = (
            aws_sdk_connect.types.evaluation_form_auto_evaluation_configuration.serialize_json(
                value["auto_evaluation_configuration"]
            )
        )
    if "review_configuration" in value:
        import aws_sdk_connect.types.evaluation_review_configuration

        out["ReviewConfiguration"] = (
            aws_sdk_connect.types.evaluation_review_configuration.serialize_json(
                value["review_configuration"]
            )
        )
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
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
    return out


def deserialize_json(data: dict) -> EvaluationForm:
    out: EvaluationForm = {}  # type: ignore[typeddict-item]
    if "EvaluationFormId" in data:
        out["evaluation_form_id"] = data["EvaluationFormId"]
    else:
        raise DeserializationError("EvaluationForm.evaluation_form_id required")
    if "EvaluationFormVersion" in data:
        out["evaluation_form_version"] = data["EvaluationFormVersion"]
    else:
        out["evaluation_form_version"] = 0
    if "Locked" in data:
        out["locked"] = data["Locked"]
    else:
        out["locked"] = False
    if "EvaluationFormArn" in data:
        out["evaluation_form_arn"] = data["EvaluationFormArn"]
    else:
        raise DeserializationError("EvaluationForm.evaluation_form_arn required")
    if "Title" in data:
        out["title"] = data["Title"]
    else:
        raise DeserializationError("EvaluationForm.title required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Status" in data:
        import aws_sdk_connect.types.evaluation_form_version_status

        out["status"] = (
            aws_sdk_connect.types.evaluation_form_version_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("EvaluationForm.status required")
    if "Items" in data:
        import aws_sdk_connect.types.evaluation_form_items_list

        out["items"] = (
            aws_sdk_connect.types.evaluation_form_items_list.deserialize_json(
                data["Items"]
            )
        )
    else:
        raise DeserializationError("EvaluationForm.items required")
    if "ScoringStrategy" in data:
        import aws_sdk_connect.types.evaluation_form_scoring_strategy

        out["scoring_strategy"] = (
            aws_sdk_connect.types.evaluation_form_scoring_strategy.deserialize_json(
                data["ScoringStrategy"]
            )
        )
    if "CreatedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["created_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    else:
        raise DeserializationError("EvaluationForm.created_time required")
    if "CreatedBy" in data:
        out["created_by"] = data["CreatedBy"]
    else:
        raise DeserializationError("EvaluationForm.created_by required")
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    else:
        raise DeserializationError("EvaluationForm.last_modified_time required")
    if "LastModifiedBy" in data:
        out["last_modified_by"] = data["LastModifiedBy"]
    else:
        raise DeserializationError("EvaluationForm.last_modified_by required")
    if "AutoEvaluationConfiguration" in data:
        import aws_sdk_connect.types.evaluation_form_auto_evaluation_configuration

        out["auto_evaluation_configuration"] = (
            aws_sdk_connect.types.evaluation_form_auto_evaluation_configuration.deserialize_json(
                data["AutoEvaluationConfiguration"]
            )
        )
    if "ReviewConfiguration" in data:
        import aws_sdk_connect.types.evaluation_review_configuration

        out["review_configuration"] = (
            aws_sdk_connect.types.evaluation_review_configuration.deserialize_json(
                data["ReviewConfiguration"]
            )
        )
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
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
    return out
