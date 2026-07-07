"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CreateAnalysisTemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.analysis_format
    import aws_sdk_cleanrooms.types.analysis_parameter_list
    import aws_sdk_cleanrooms.types.analysis_schema
    import aws_sdk_cleanrooms.types.analysis_source
    import aws_sdk_cleanrooms.types.error_message_configuration
    import aws_sdk_cleanrooms.types.membership_identifier
    import aws_sdk_cleanrooms.types.resource_description
    import aws_sdk_cleanrooms.types.synthetic_data_parameters
    import aws_sdk_cleanrooms.types.table_alias
    import aws_sdk_cleanrooms.types.tag_map


class CreateAnalysisTemplateInput(TypedDict, closed=True):
    description: NotRequired[
        "aws_sdk_cleanrooms.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the analysis template.</p>"""
    membership_identifier: (
        "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The identifier for a membership resource.</p>"""
    name: "aws_sdk_cleanrooms.types.table_alias.TableAlias"
    """<p>The name of the analysis template.</p>"""
    format: "aws_sdk_cleanrooms.types.analysis_format.AnalysisFormat"
    """<p>The format of the analysis template.</p>"""
    source: "aws_sdk_cleanrooms.types.analysis_source.AnalysisSource"
    """<p>The information in the analysis template.</p>"""
    tags: NotRequired["aws_sdk_cleanrooms.types.tag_map.TagMap"]
    """<p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>"""
    analysis_parameters: NotRequired[
        "aws_sdk_cleanrooms.types.analysis_parameter_list.AnalysisParameterList"
    ]
    """<p>The parameters of the analysis template.</p>"""
    schema: NotRequired["aws_sdk_cleanrooms.types.analysis_schema.AnalysisSchema"]
    error_message_configuration: NotRequired[
        "aws_sdk_cleanrooms.types.error_message_configuration.ErrorMessageConfiguration"
    ]
    """<p>The configuration that specifies the level of detail in error messages returned by analyses using this template. When set to <code>DETAILED</code>, error messages include more information to help troubleshoot issues with PySpark jobs. Detailed error messages may expose underlying data, including sensitive information. Recommended for faster troubleshooting in development and testing environments.</p>"""
    synthetic_data_parameters: NotRequired[
        "aws_sdk_cleanrooms.types.synthetic_data_parameters.SyntheticDataParameters"
    ]
    """<p>The parameters for generating synthetic data when running the analysis template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAnalysisTemplateInput) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    out["name"] = value["name"]
    import aws_sdk_cleanrooms.types.analysis_format

    out["format"] = aws_sdk_cleanrooms.types.analysis_format.serialize_json(
        value["format"]
    )
    import aws_sdk_cleanrooms.types.analysis_source

    out["source"] = aws_sdk_cleanrooms.types.analysis_source.serialize_json(
        value["source"]
    )
    if "tags" in value:
        import aws_sdk_cleanrooms.types.tag_map

        out["tags"] = aws_sdk_cleanrooms.types.tag_map.serialize_json(value["tags"])
    if "analysis_parameters" in value:
        import aws_sdk_cleanrooms.types.analysis_parameter_list

        out["analysisParameters"] = (
            aws_sdk_cleanrooms.types.analysis_parameter_list.serialize_json(
                value["analysis_parameters"]
            )
        )
    if "schema" in value:
        import aws_sdk_cleanrooms.types.analysis_schema

        out["schema"] = aws_sdk_cleanrooms.types.analysis_schema.serialize_json(
            value["schema"]
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


def deserialize_json(data: dict) -> CreateAnalysisTemplateInput:
    out: CreateAnalysisTemplateInput = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAnalysisTemplateInput.name required")
    if "format" in data:
        import aws_sdk_cleanrooms.types.analysis_format

        out["format"] = aws_sdk_cleanrooms.types.analysis_format.deserialize_json(
            data["format"]
        )
    else:
        raise DeserializationError("CreateAnalysisTemplateInput.format required")
    if "source" in data:
        import aws_sdk_cleanrooms.types.analysis_source

        out["source"] = aws_sdk_cleanrooms.types.analysis_source.deserialize_json(
            data["source"]
        )
    else:
        raise DeserializationError("CreateAnalysisTemplateInput.source required")
    if "tags" in data:
        import aws_sdk_cleanrooms.types.tag_map

        out["tags"] = aws_sdk_cleanrooms.types.tag_map.deserialize_json(data["tags"])
    if "analysisParameters" in data:
        import aws_sdk_cleanrooms.types.analysis_parameter_list

        out["analysis_parameters"] = (
            aws_sdk_cleanrooms.types.analysis_parameter_list.deserialize_json(
                data["analysisParameters"]
            )
        )
    if "schema" in data:
        import aws_sdk_cleanrooms.types.analysis_schema

        out["schema"] = aws_sdk_cleanrooms.types.analysis_schema.deserialize_json(
            data["schema"]
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
