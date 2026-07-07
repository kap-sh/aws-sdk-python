"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CollaborationAnalysisTemplate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanrooms.types.account_id
    import aws_sdk_cleanrooms.types.analysis_format
    import aws_sdk_cleanrooms.types.analysis_parameter_list
    import aws_sdk_cleanrooms.types.analysis_schema
    import aws_sdk_cleanrooms.types.analysis_source
    import aws_sdk_cleanrooms.types.analysis_source_metadata
    import aws_sdk_cleanrooms.types.analysis_template_arn
    import aws_sdk_cleanrooms.types.analysis_template_identifier
    import aws_sdk_cleanrooms.types.analysis_template_validation_status_detail_list
    import aws_sdk_cleanrooms.types.collaboration_arn
    import aws_sdk_cleanrooms.types.error_message_configuration
    import aws_sdk_cleanrooms.types.resource_alias
    import aws_sdk_cleanrooms.types.resource_description
    import aws_sdk_cleanrooms.types.synthetic_data_parameters
    import aws_sdk_cleanrooms.types.uuid


class CollaborationAnalysisTemplate(TypedDict, closed=True):
    id: "aws_sdk_cleanrooms.types.analysis_template_identifier.AnalysisTemplateIdentifier"
    """<p>The identifier of the analysis template.</p>"""
    arn: "aws_sdk_cleanrooms.types.analysis_template_arn.AnalysisTemplateArn"
    """<p>The Amazon Resource Name (ARN) of the analysis template.</p>"""
    collaboration_id: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>A unique identifier for the collaboration that the analysis templates belong to. Currently accepts collaboration ID.</p>"""
    collaboration_arn: "aws_sdk_cleanrooms.types.collaboration_arn.CollaborationArn"
    """<p>The unique ARN for the analysis template’s associated collaboration.</p>"""
    description: NotRequired[
        "aws_sdk_cleanrooms.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the analysis template.</p>"""
    creator_account_id: "aws_sdk_cleanrooms.types.account_id.AccountId"
    """<p>The identifier used to reference members of the collaboration. Currently only supports Amazon Web Services account ID.</p>"""
    name: "aws_sdk_cleanrooms.types.resource_alias.ResourceAlias"
    """<p>The name of the analysis template.</p>"""
    create_time: "datetime.datetime"
    """<p>The time that the analysis template within a collaboration was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The time that the analysis template in the collaboration was last updated.</p>"""
    schema: "aws_sdk_cleanrooms.types.analysis_schema.AnalysisSchema"
    """<p>The entire schema object.</p>"""
    format: "aws_sdk_cleanrooms.types.analysis_format.AnalysisFormat"
    """<p>The format of the analysis template in the collaboration.</p>"""
    source: NotRequired["aws_sdk_cleanrooms.types.analysis_source.AnalysisSource"]
    """<p>The source of the analysis template within a collaboration.</p>"""
    source_metadata: NotRequired[
        "aws_sdk_cleanrooms.types.analysis_source_metadata.AnalysisSourceMetadata"
    ]
    """<p> The source metadata for the collaboration analysis template.</p>"""
    analysis_parameters: NotRequired[
        "aws_sdk_cleanrooms.types.analysis_parameter_list.AnalysisParameterList"
    ]
    """<p>The analysis parameters that have been specified in the analysis template.</p>"""
    validations: NotRequired[
        "aws_sdk_cleanrooms.types.analysis_template_validation_status_detail_list.AnalysisTemplateValidationStatusDetailList"
    ]
    """<p>The validations that were performed.</p>"""
    error_message_configuration: NotRequired[
        "aws_sdk_cleanrooms.types.error_message_configuration.ErrorMessageConfiguration"
    ]
    """<p>The configuration that specifies the level of detail in error messages returned by analyses using this template. When set to <code>DETAILED</code>, error messages include more information to help troubleshoot issues with PySpark jobs. Detailed error messages may expose underlying data, including sensitive information. Recommended for faster troubleshooting in development and testing environments.</p>"""
    synthetic_data_parameters: NotRequired[
        "aws_sdk_cleanrooms.types.synthetic_data_parameters.SyntheticDataParameters"
    ]
    """<p>The synthetic data generation parameters configured for this collaboration analysis template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CollaborationAnalysisTemplate) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["collaborationId"] = value["collaboration_id"]
    out["collaborationArn"] = value["collaboration_arn"]
    if "description" in value:
        out["description"] = value["description"]
    out["creatorAccountId"] = value["creator_account_id"]
    out["name"] = value["name"]
    import aws_sdk_cleanrooms.types._prelude.timestamp

    out["createTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import aws_sdk_cleanrooms.types._prelude.timestamp

    out["updateTime"] = aws_sdk_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    import aws_sdk_cleanrooms.types.analysis_schema

    out["schema"] = aws_sdk_cleanrooms.types.analysis_schema.serialize_json(
        value["schema"]
    )
    import aws_sdk_cleanrooms.types.analysis_format

    out["format"] = aws_sdk_cleanrooms.types.analysis_format.serialize_json(
        value["format"]
    )
    if "source" in value:
        import aws_sdk_cleanrooms.types.analysis_source

        out["source"] = aws_sdk_cleanrooms.types.analysis_source.serialize_json(
            value["source"]
        )
    if "source_metadata" in value:
        import aws_sdk_cleanrooms.types.analysis_source_metadata

        out["sourceMetadata"] = (
            aws_sdk_cleanrooms.types.analysis_source_metadata.serialize_json(
                value["source_metadata"]
            )
        )
    if "analysis_parameters" in value:
        import aws_sdk_cleanrooms.types.analysis_parameter_list

        out["analysisParameters"] = (
            aws_sdk_cleanrooms.types.analysis_parameter_list.serialize_json(
                value["analysis_parameters"]
            )
        )
    if "validations" in value:
        import aws_sdk_cleanrooms.types.analysis_template_validation_status_detail_list

        out["validations"] = (
            aws_sdk_cleanrooms.types.analysis_template_validation_status_detail_list.serialize_json(
                value["validations"]
            )
        )
    if "error_message_configuration" in value:
        import aws_sdk_cleanrooms.types.error_message_configuration

        out["errorMessageConfiguration"] = (
            aws_sdk_cleanrooms.types.error_message_configuration.serialize_json(
                value["error_message_configuration"]
            )
        )
    if "synthetic_data_parameters" in value:
        import aws_sdk_cleanrooms.types.synthetic_data_parameters

        out["syntheticDataParameters"] = (
            aws_sdk_cleanrooms.types.synthetic_data_parameters.serialize_json(
                value["synthetic_data_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> CollaborationAnalysisTemplate:
    out: CollaborationAnalysisTemplate = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CollaborationAnalysisTemplate.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CollaborationAnalysisTemplate.arn required")
    if "collaborationId" in data:
        out["collaboration_id"] = data["collaborationId"]
    else:
        raise DeserializationError(
            "CollaborationAnalysisTemplate.collaboration_id required"
        )
    if "collaborationArn" in data:
        out["collaboration_arn"] = data["collaborationArn"]
    else:
        raise DeserializationError(
            "CollaborationAnalysisTemplate.collaboration_arn required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "creatorAccountId" in data:
        out["creator_account_id"] = data["creatorAccountId"]
    else:
        raise DeserializationError(
            "CollaborationAnalysisTemplate.creator_account_id required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CollaborationAnalysisTemplate.name required")
    if "createTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError("CollaborationAnalysisTemplate.create_time required")
    if "updateTime" in data:
        import aws_sdk_cleanrooms.types._prelude.timestamp

        out["update_time"] = (
            aws_sdk_cleanrooms.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError("CollaborationAnalysisTemplate.update_time required")
    if "schema" in data:
        import aws_sdk_cleanrooms.types.analysis_schema

        out["schema"] = aws_sdk_cleanrooms.types.analysis_schema.deserialize_json(
            data["schema"]
        )
    else:
        raise DeserializationError("CollaborationAnalysisTemplate.schema required")
    if "format" in data:
        import aws_sdk_cleanrooms.types.analysis_format

        out["format"] = aws_sdk_cleanrooms.types.analysis_format.deserialize_json(
            data["format"]
        )
    else:
        raise DeserializationError("CollaborationAnalysisTemplate.format required")
    if "source" in data:
        import aws_sdk_cleanrooms.types.analysis_source

        out["source"] = aws_sdk_cleanrooms.types.analysis_source.deserialize_json(
            data["source"]
        )
    if "sourceMetadata" in data:
        import aws_sdk_cleanrooms.types.analysis_source_metadata

        out["source_metadata"] = (
            aws_sdk_cleanrooms.types.analysis_source_metadata.deserialize_json(
                data["sourceMetadata"]
            )
        )
    if "analysisParameters" in data:
        import aws_sdk_cleanrooms.types.analysis_parameter_list

        out["analysis_parameters"] = (
            aws_sdk_cleanrooms.types.analysis_parameter_list.deserialize_json(
                data["analysisParameters"]
            )
        )
    if "validations" in data:
        import aws_sdk_cleanrooms.types.analysis_template_validation_status_detail_list

        out["validations"] = (
            aws_sdk_cleanrooms.types.analysis_template_validation_status_detail_list.deserialize_json(
                data["validations"]
            )
        )
    if "errorMessageConfiguration" in data:
        import aws_sdk_cleanrooms.types.error_message_configuration

        out["error_message_configuration"] = (
            aws_sdk_cleanrooms.types.error_message_configuration.deserialize_json(
                data["errorMessageConfiguration"]
            )
        )
    if "syntheticDataParameters" in data:
        import aws_sdk_cleanrooms.types.synthetic_data_parameters

        out["synthetic_data_parameters"] = (
            aws_sdk_cleanrooms.types.synthetic_data_parameters.deserialize_json(
                data["syntheticDataParameters"]
            )
        )
    return out
