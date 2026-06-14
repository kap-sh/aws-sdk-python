"""Generated from Smithy shape ``com.amazonaws.connect#CreateEvaluationFormRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.boxed_boolean
    import aws_sdk_connect.types.client_token
    import aws_sdk_connect.types.evaluation_form_auto_evaluation_configuration
    import aws_sdk_connect.types.evaluation_form_description
    import aws_sdk_connect.types.evaluation_form_items_list
    import aws_sdk_connect.types.evaluation_form_language_configuration
    import aws_sdk_connect.types.evaluation_form_scoring_strategy
    import aws_sdk_connect.types.evaluation_form_target_configuration
    import aws_sdk_connect.types.evaluation_form_title
    import aws_sdk_connect.types.evaluation_review_configuration
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.tag_map


class CreateEvaluationFormRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
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
    """<p>Configuration information about automated evaluations.</p>"""
    client_token: NotRequired["aws_sdk_connect.types.client_token.ClientToken"]
    r"""<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>"""
    as_draft: "aws_sdk_connect.types.boxed_boolean.BoxedBoolean"
    """<p>A boolean flag indicating whether to create evaluation form in draft state.</p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    r"""<p>The tags used to organize, track, or control access for this resource. For example, { \"Tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""
    review_configuration: NotRequired[
        "aws_sdk_connect.types.evaluation_review_configuration.EvaluationReviewConfiguration"
    ]
    """<p>Configuration information about evaluation reviews.</p>"""
    target_configuration: NotRequired[
        "aws_sdk_connect.types.evaluation_form_target_configuration.EvaluationFormTargetConfiguration"
    ]
    """<p>Configuration that specifies the target for the evaluation form.</p>"""
    language_configuration: NotRequired[
        "aws_sdk_connect.types.evaluation_form_language_configuration.EvaluationFormLanguageConfiguration"
    ]
    """<p>Configuration for language settings of the evaluation form.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEvaluationFormRequest) -> dict:
    out: dict = {}
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
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["AsDraft"] = value.get("as_draft", False)
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    if "review_configuration" in value:
        import aws_sdk_connect.types.evaluation_review_configuration

        out["ReviewConfiguration"] = (
            aws_sdk_connect.types.evaluation_review_configuration.serialize_json(
                value["review_configuration"]
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
    return out


def deserialize_json(data: dict) -> CreateEvaluationFormRequest:
    out: CreateEvaluationFormRequest = {}  # type: ignore[typeddict-item]
    if "Title" in data:
        out["title"] = data["Title"]
    else:
        raise DeserializationError("CreateEvaluationFormRequest.title required")
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
        raise DeserializationError("CreateEvaluationFormRequest.items required")
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
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "AsDraft" in data:
        out["as_draft"] = data["AsDraft"]
    else:
        out["as_draft"] = False
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    if "ReviewConfiguration" in data:
        import aws_sdk_connect.types.evaluation_review_configuration

        out["review_configuration"] = (
            aws_sdk_connect.types.evaluation_review_configuration.deserialize_json(
                data["ReviewConfiguration"]
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
    return out
