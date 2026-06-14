"""Generated from Smithy shape ``com.amazonaws.datazone#CreateDataSourceInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.data_source_configuration_input
    import aws_sdk_datazone.types.data_source_type
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.enable_setting
    import aws_sdk_datazone.types.form_input_list
    import aws_sdk_datazone.types.name
    import aws_sdk_datazone.types.recommendation_configuration
    import aws_sdk_datazone.types.schedule_configuration


class CreateDataSourceInput(TypedDict):
    name: "aws_sdk_datazone.types.name.Name"
    """<p>The name of the data source.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description of the data source.</p>"""
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain where the data source is created.</p>"""
    project_identifier: "str"
    """<p>The identifier of the Amazon DataZone project in which you want to add this data source.</p>"""
    environment_identifier: NotRequired["str"]
    """<p>The unique identifier of the Amazon DataZone environment to which the data source publishes assets. </p>"""
    connection_identifier: NotRequired["str"]
    """<p>The ID of the connection.</p>"""
    type: "aws_sdk_datazone.types.data_source_type.DataSourceType"
    """<p>The type of the data source. In Amazon DataZone, you can use data sources to import technical metadata of assets (data) from the source databases or data warehouses into Amazon DataZone. In the current release of Amazon DataZone, you can create and run data sources for Amazon Web Services Glue and Amazon Redshift.</p>"""
    configuration: NotRequired[
        "aws_sdk_datazone.types.data_source_configuration_input.DataSourceConfigurationInput"
    ]
    """<p>Specifies the configuration of the data source. It can be set to either <code>glueRunConfiguration</code> or <code>redshiftRunConfiguration</code>.</p>"""
    recommendation: NotRequired[
        "aws_sdk_datazone.types.recommendation_configuration.RecommendationConfiguration"
    ]
    """<p>Specifies whether the business name generation is to be enabled for this data source.</p>"""
    enable_setting: NotRequired["aws_sdk_datazone.types.enable_setting.EnableSetting"]
    """<p>Specifies whether the data source is enabled.</p>"""
    schedule: NotRequired[
        "aws_sdk_datazone.types.schedule_configuration.ScheduleConfiguration"
    ]
    """<p>The schedule of the data source runs.</p>"""
    publish_on_import: NotRequired["bool"]
    """<p>Specifies whether the assets that this data source creates in the inventory are to be also automatically published to the catalog.</p>"""
    asset_forms_input: NotRequired[
        "aws_sdk_datazone.types.form_input_list.FormInputList"
    ]
    """<p>The metadata forms that are to be attached to the assets that this data source works with.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataSourceInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["projectIdentifier"] = value["project_identifier"]
    if "environment_identifier" in value:
        out["environmentIdentifier"] = value["environment_identifier"]
    if "connection_identifier" in value:
        out["connectionIdentifier"] = value["connection_identifier"]
    out["type"] = value["type"]
    if "configuration" in value:
        import aws_sdk_datazone.types.data_source_configuration_input

        out["configuration"] = (
            aws_sdk_datazone.types.data_source_configuration_input.serialize_json(
                value["configuration"]
            )
        )
    if "recommendation" in value:
        import aws_sdk_datazone.types.recommendation_configuration

        out["recommendation"] = (
            aws_sdk_datazone.types.recommendation_configuration.serialize_json(
                value["recommendation"]
            )
        )
    if "enable_setting" in value:
        import aws_sdk_datazone.types.enable_setting

        out["enableSetting"] = aws_sdk_datazone.types.enable_setting.serialize_json(
            value["enable_setting"]
        )
    if "schedule" in value:
        import aws_sdk_datazone.types.schedule_configuration

        out["schedule"] = aws_sdk_datazone.types.schedule_configuration.serialize_json(
            value["schedule"]
        )
    if "publish_on_import" in value:
        out["publishOnImport"] = value["publish_on_import"]
    if "asset_forms_input" in value:
        import aws_sdk_datazone.types.form_input_list

        out["assetFormsInput"] = aws_sdk_datazone.types.form_input_list.serialize_json(
            value["asset_forms_input"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateDataSourceInput:
    out: CreateDataSourceInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateDataSourceInput.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "projectIdentifier" in data:
        out["project_identifier"] = data["projectIdentifier"]
    else:
        raise DeserializationError("CreateDataSourceInput.project_identifier required")
    if "environmentIdentifier" in data:
        out["environment_identifier"] = data["environmentIdentifier"]
    if "connectionIdentifier" in data:
        out["connection_identifier"] = data["connectionIdentifier"]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("CreateDataSourceInput.type required")
    if "configuration" in data:
        import aws_sdk_datazone.types.data_source_configuration_input

        out["configuration"] = (
            aws_sdk_datazone.types.data_source_configuration_input.deserialize_json(
                data["configuration"]
            )
        )
    if "recommendation" in data:
        import aws_sdk_datazone.types.recommendation_configuration

        out["recommendation"] = (
            aws_sdk_datazone.types.recommendation_configuration.deserialize_json(
                data["recommendation"]
            )
        )
    if "enableSetting" in data:
        import aws_sdk_datazone.types.enable_setting

        out["enable_setting"] = aws_sdk_datazone.types.enable_setting.deserialize_json(
            data["enableSetting"]
        )
    if "schedule" in data:
        import aws_sdk_datazone.types.schedule_configuration

        out["schedule"] = (
            aws_sdk_datazone.types.schedule_configuration.deserialize_json(
                data["schedule"]
            )
        )
    if "publishOnImport" in data:
        out["publish_on_import"] = data["publishOnImport"]
    if "assetFormsInput" in data:
        import aws_sdk_datazone.types.form_input_list

        out["asset_forms_input"] = (
            aws_sdk_datazone.types.form_input_list.deserialize_json(
                data["assetFormsInput"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
