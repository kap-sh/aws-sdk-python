"""Generated from Smithy shape ``com.amazonaws.resiliencehub#RecommendationTemplate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.arn
    import aws_sdk_resiliencehub.types.boolean_optional
    import aws_sdk_resiliencehub.types.entity_name
    import aws_sdk_resiliencehub.types.recommendation_id_list
    import aws_sdk_resiliencehub.types.recommendation_template_status
    import aws_sdk_resiliencehub.types.render_recommendation_type_list
    import aws_sdk_resiliencehub.types.s3_location
    import aws_sdk_resiliencehub.types.string500
    import aws_sdk_resiliencehub.types.tag_map
    import aws_sdk_resiliencehub.types.template_format
    import aws_sdk_resiliencehub.types.time_stamp


class RecommendationTemplate(TypedDict, closed=True):
    templates_location: NotRequired[
        "aws_sdk_resiliencehub.types.s3_location.S3Location"
    ]
    """<p>The file location of the template.</p>"""
    assessment_arn: "aws_sdk_resiliencehub.types.arn.Arn"
    r"""<p>Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app-assessment/<code>app-id</code>. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    app_arn: NotRequired["aws_sdk_resiliencehub.types.arn.Arn"]
    r"""<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    recommendation_ids: NotRequired[
        "aws_sdk_resiliencehub.types.recommendation_id_list.RecommendationIdList"
    ]
    """<p>Identifiers for the recommendations used in the recommendation template.</p>"""
    recommendation_types: "aws_sdk_resiliencehub.types.render_recommendation_type_list.RenderRecommendationTypeList"
    """<p>An array of strings that specify the recommendation template type or types.</p> <dl> <dt>Alarm</dt> <dd> <p>The template is an <a>AlarmRecommendation</a> template.</p> </dd> <dt>Sop</dt> <dd> <p>The template is a <a>SopRecommendation</a> template.</p> </dd> <dt>Test</dt> <dd> <p>The template is a <a>TestRecommendation</a> template.</p> </dd> </dl>"""
    format: "aws_sdk_resiliencehub.types.template_format.TemplateFormat"
    """<p>Format of the recommendation template.</p> <dl> <dt>CfnJson</dt> <dd> <p>The template is CloudFormation JSON.</p> </dd> <dt>CfnYaml</dt> <dd> <p>The template is CloudFormation YAML.</p> </dd> </dl>"""
    recommendation_template_arn: "aws_sdk_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) for the recommendation template.</p>"""
    message: NotRequired["aws_sdk_resiliencehub.types.string500.String500"]
    """<p>Message for the recommendation template.</p>"""
    status: "aws_sdk_resiliencehub.types.recommendation_template_status.RecommendationTemplateStatus"
    """<p>Status of the action.</p>"""
    name: "aws_sdk_resiliencehub.types.entity_name.EntityName"
    """<p>Name for the recommendation template.</p>"""
    start_time: NotRequired["aws_sdk_resiliencehub.types.time_stamp.TimeStamp"]
    """<p>The start time for the action.</p>"""
    end_time: NotRequired["aws_sdk_resiliencehub.types.time_stamp.TimeStamp"]
    """<p>The end time for the action.</p>"""
    tags: NotRequired["aws_sdk_resiliencehub.types.tag_map.TagMap"]
    """<p>Tags assigned to the resource. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key/value pair.</p>"""
    needs_replacements: NotRequired[
        "aws_sdk_resiliencehub.types.boolean_optional.BooleanOptional"
    ]
    """<p>Indicates if replacements are needed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationTemplate) -> dict:
    out: dict = {}
    if "templates_location" in value:
        import aws_sdk_resiliencehub.types.s3_location

        out["templatesLocation"] = (
            aws_sdk_resiliencehub.types.s3_location.serialize_json(
                value["templates_location"]
            )
        )
    out["assessmentArn"] = value["assessment_arn"]
    if "app_arn" in value:
        out["appArn"] = value["app_arn"]
    if "recommendation_ids" in value:
        import aws_sdk_resiliencehub.types.recommendation_id_list

        out["recommendationIds"] = (
            aws_sdk_resiliencehub.types.recommendation_id_list.serialize_json(
                value["recommendation_ids"]
            )
        )
    import aws_sdk_resiliencehub.types.render_recommendation_type_list

    out["recommendationTypes"] = (
        aws_sdk_resiliencehub.types.render_recommendation_type_list.serialize_json(
            value["recommendation_types"]
        )
    )
    import aws_sdk_resiliencehub.types.template_format

    out["format"] = aws_sdk_resiliencehub.types.template_format.serialize_json(
        value["format"]
    )
    out["recommendationTemplateArn"] = value["recommendation_template_arn"]
    if "message" in value:
        out["message"] = value["message"]
    import aws_sdk_resiliencehub.types.recommendation_template_status

    out["status"] = (
        aws_sdk_resiliencehub.types.recommendation_template_status.serialize_json(
            value["status"]
        )
    )
    out["name"] = value["name"]
    if "start_time" in value:
        import aws_sdk_resiliencehub.types.time_stamp

        out["startTime"] = aws_sdk_resiliencehub.types.time_stamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_resiliencehub.types.time_stamp

        out["endTime"] = aws_sdk_resiliencehub.types.time_stamp.serialize_json(
            value["end_time"]
        )
    if "tags" in value:
        import aws_sdk_resiliencehub.types.tag_map

        out["tags"] = aws_sdk_resiliencehub.types.tag_map.serialize_json(value["tags"])
    if "needs_replacements" in value:
        out["needsReplacements"] = value["needs_replacements"]
    return out


def deserialize_json(data: dict) -> RecommendationTemplate:
    out: RecommendationTemplate = {}  # type: ignore[typeddict-item]
    if "templatesLocation" in data:
        import aws_sdk_resiliencehub.types.s3_location

        out["templates_location"] = (
            aws_sdk_resiliencehub.types.s3_location.deserialize_json(
                data["templatesLocation"]
            )
        )
    if "assessmentArn" in data:
        out["assessment_arn"] = data["assessmentArn"]
    else:
        raise DeserializationError("RecommendationTemplate.assessment_arn required")
    if "appArn" in data:
        out["app_arn"] = data["appArn"]
    if "recommendationIds" in data:
        import aws_sdk_resiliencehub.types.recommendation_id_list

        out["recommendation_ids"] = (
            aws_sdk_resiliencehub.types.recommendation_id_list.deserialize_json(
                data["recommendationIds"]
            )
        )
    if "recommendationTypes" in data:
        import aws_sdk_resiliencehub.types.render_recommendation_type_list

        out["recommendation_types"] = (
            aws_sdk_resiliencehub.types.render_recommendation_type_list.deserialize_json(
                data["recommendationTypes"]
            )
        )
    else:
        raise DeserializationError(
            "RecommendationTemplate.recommendation_types required"
        )
    if "format" in data:
        import aws_sdk_resiliencehub.types.template_format

        out["format"] = aws_sdk_resiliencehub.types.template_format.deserialize_json(
            data["format"]
        )
    else:
        raise DeserializationError("RecommendationTemplate.format required")
    if "recommendationTemplateArn" in data:
        out["recommendation_template_arn"] = data["recommendationTemplateArn"]
    else:
        raise DeserializationError(
            "RecommendationTemplate.recommendation_template_arn required"
        )
    if "message" in data:
        out["message"] = data["message"]
    if "status" in data:
        import aws_sdk_resiliencehub.types.recommendation_template_status

        out["status"] = (
            aws_sdk_resiliencehub.types.recommendation_template_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("RecommendationTemplate.status required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("RecommendationTemplate.name required")
    if "startTime" in data:
        import aws_sdk_resiliencehub.types.time_stamp

        out["start_time"] = aws_sdk_resiliencehub.types.time_stamp.deserialize_json(
            data["startTime"]
        )
    if "endTime" in data:
        import aws_sdk_resiliencehub.types.time_stamp

        out["end_time"] = aws_sdk_resiliencehub.types.time_stamp.deserialize_json(
            data["endTime"]
        )
    if "tags" in data:
        import aws_sdk_resiliencehub.types.tag_map

        out["tags"] = aws_sdk_resiliencehub.types.tag_map.deserialize_json(data["tags"])
    if "needsReplacements" in data:
        out["needs_replacements"] = data["needsReplacements"]
    return out
