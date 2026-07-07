"""Generated from Smithy shape ``com.amazonaws.quicksight#TemplateVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.data_set_configuration_list
    import aws_sdk_quicksight.types.resource_status
    import aws_sdk_quicksight.types.sheet_list
    import aws_sdk_quicksight.types.template_error_list
    import aws_sdk_quicksight.types.timestamp
    import aws_sdk_quicksight.types.version_description
    import aws_sdk_quicksight.types.version_number


class TemplateVersion(TypedDict, closed=True):
    created_time: NotRequired["aws_sdk_quicksight.types.timestamp.Timestamp"]
    """<p>The time that this template version was created.</p>"""
    errors: NotRequired[
        "aws_sdk_quicksight.types.template_error_list.TemplateErrorList"
    ]
    """<p>Errors associated with this template version.</p>"""
    version_number: NotRequired["aws_sdk_quicksight.types.version_number.VersionNumber"]
    """<p>The version number of the template version.</p>"""
    status: NotRequired["aws_sdk_quicksight.types.resource_status.ResourceStatus"]
    """<p>The status that is associated with the template.</p> <ul> <li> <p> <code>CREATION_IN_PROGRESS</code> </p> </li> <li> <p> <code>CREATION_SUCCESSFUL</code> </p> </li> <li> <p> <code>CREATION_FAILED</code> </p> </li> <li> <p> <code>UPDATE_IN_PROGRESS</code> </p> </li> <li> <p> <code>UPDATE_SUCCESSFUL</code> </p> </li> <li> <p> <code>UPDATE_FAILED</code> </p> </li> <li> <p> <code>DELETED</code> </p> </li> </ul>"""
    data_set_configurations: NotRequired[
        "aws_sdk_quicksight.types.data_set_configuration_list.DataSetConfigurationList"
    ]
    """<p>Schema of the dataset identified by the placeholder. Any dashboard created from this template should be bound to new datasets matching the same schema described through this API operation.</p>"""
    description: NotRequired[
        "aws_sdk_quicksight.types.version_description.VersionDescription"
    ]
    """<p>The description of the template.</p>"""
    source_entity_arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of an analysis or template that was used to create this template.</p>"""
    theme_arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The ARN of the theme associated with this version of the template.</p>"""
    sheets: NotRequired["aws_sdk_quicksight.types.sheet_list.SheetList"]
    """<p>A list of the associated sheets with the unique identifier and name of each sheet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateVersion) -> dict:
    out: dict = {}
    if "created_time" in value:
        import aws_sdk_quicksight.types.timestamp

        out["CreatedTime"] = aws_sdk_quicksight.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "errors" in value:
        import aws_sdk_quicksight.types.template_error_list

        out["Errors"] = aws_sdk_quicksight.types.template_error_list.serialize_json(
            value["errors"]
        )
    if "version_number" in value:
        out["VersionNumber"] = value["version_number"]
    if "status" in value:
        import aws_sdk_quicksight.types.resource_status

        out["Status"] = aws_sdk_quicksight.types.resource_status.serialize_json(
            value["status"]
        )
    if "data_set_configurations" in value:
        import aws_sdk_quicksight.types.data_set_configuration_list

        out["DataSetConfigurations"] = (
            aws_sdk_quicksight.types.data_set_configuration_list.serialize_json(
                value["data_set_configurations"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "source_entity_arn" in value:
        out["SourceEntityArn"] = value["source_entity_arn"]
    if "theme_arn" in value:
        out["ThemeArn"] = value["theme_arn"]
    if "sheets" in value:
        import aws_sdk_quicksight.types.sheet_list

        out["Sheets"] = aws_sdk_quicksight.types.sheet_list.serialize_json(
            value["sheets"]
        )
    return out


def deserialize_json(data: dict) -> TemplateVersion:
    out: TemplateVersion = {}  # type: ignore[typeddict-item]
    if "CreatedTime" in data:
        import aws_sdk_quicksight.types.timestamp

        out["created_time"] = aws_sdk_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if "Errors" in data:
        import aws_sdk_quicksight.types.template_error_list

        out["errors"] = aws_sdk_quicksight.types.template_error_list.deserialize_json(
            data["Errors"]
        )
    if "VersionNumber" in data:
        out["version_number"] = data["VersionNumber"]
    if "Status" in data:
        import aws_sdk_quicksight.types.resource_status

        out["status"] = aws_sdk_quicksight.types.resource_status.deserialize_json(
            data["Status"]
        )
    if "DataSetConfigurations" in data:
        import aws_sdk_quicksight.types.data_set_configuration_list

        out["data_set_configurations"] = (
            aws_sdk_quicksight.types.data_set_configuration_list.deserialize_json(
                data["DataSetConfigurations"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "SourceEntityArn" in data:
        out["source_entity_arn"] = data["SourceEntityArn"]
    if "ThemeArn" in data:
        out["theme_arn"] = data["ThemeArn"]
    if "Sheets" in data:
        import aws_sdk_quicksight.types.sheet_list

        out["sheets"] = aws_sdk_quicksight.types.sheet_list.deserialize_json(
            data["Sheets"]
        )
    return out
