"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateDataSourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.data_source_configuration_input
    import aws_sdk_datazone.types.data_source_id
    import aws_sdk_datazone.types.description
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.enable_setting
    import aws_sdk_datazone.types.form_input_list
    import aws_sdk_datazone.types.name
    import aws_sdk_datazone.types.recommendation_configuration
    import aws_sdk_datazone.types.schedule_configuration


class UpdateDataSourceInput(TypedDict, closed=True):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the domain in which to update a data source.</p>"""
    identifier: "aws_sdk_datazone.types.data_source_id.DataSourceId"
    """<p>The identifier of the data source to be updated.</p>"""
    name: NotRequired["aws_sdk_datazone.types.name.Name"]
    """<p>The name to be updated as part of the <code>UpdateDataSource</code> action.</p>"""
    description: NotRequired["aws_sdk_datazone.types.description.Description"]
    """<p>The description to be updated as part of the <code>UpdateDataSource</code> action.</p>"""
    enable_setting: NotRequired["aws_sdk_datazone.types.enable_setting.EnableSetting"]
    """<p>The enable setting to be updated as part of the <code>UpdateDataSource</code> action.</p>"""
    publish_on_import: NotRequired["bool"]
    """<p>The publish on import setting to be updated as part of the <code>UpdateDataSource</code> action.</p>"""
    asset_forms_input: NotRequired[
        "aws_sdk_datazone.types.form_input_list.FormInputList"
    ]
    """<p>The asset forms to be updated as part of the <code>UpdateDataSource</code> action.</p>"""
    schedule: NotRequired[
        "aws_sdk_datazone.types.schedule_configuration.ScheduleConfiguration"
    ]
    """<p>The schedule to be updated as part of the <code>UpdateDataSource</code> action.</p>"""
    configuration: NotRequired[
        "aws_sdk_datazone.types.data_source_configuration_input.DataSourceConfigurationInput"
    ]
    """<p>The configuration to be updated as part of the <code>UpdateDataSource</code> action.</p>"""
    recommendation: NotRequired[
        "aws_sdk_datazone.types.recommendation_configuration.RecommendationConfiguration"
    ]
    """<p>The recommendation to be updated as part of the <code>UpdateDataSource</code> action.</p>"""
    retain_permissions_on_revoke_failure: NotRequired["bool"]
    """<p>Specifies that the granted permissions are retained in case of a self-subscribe functionality failure for a data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataSourceInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "enable_setting" in value:
        import aws_sdk_datazone.types.enable_setting

        out["enableSetting"] = aws_sdk_datazone.types.enable_setting.serialize_json(
            value["enable_setting"]
        )
    if "publish_on_import" in value:
        out["publishOnImport"] = value["publish_on_import"]
    if "asset_forms_input" in value:
        import aws_sdk_datazone.types.form_input_list

        out["assetFormsInput"] = aws_sdk_datazone.types.form_input_list.serialize_json(
            value["asset_forms_input"]
        )
    if "schedule" in value:
        import aws_sdk_datazone.types.schedule_configuration

        out["schedule"] = aws_sdk_datazone.types.schedule_configuration.serialize_json(
            value["schedule"]
        )
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
    if "retain_permissions_on_revoke_failure" in value:
        out["retainPermissionsOnRevokeFailure"] = value[
            "retain_permissions_on_revoke_failure"
        ]
    return out


def deserialize_json(data: dict) -> UpdateDataSourceInput:
    out: UpdateDataSourceInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "enableSetting" in data:
        import aws_sdk_datazone.types.enable_setting

        out["enable_setting"] = aws_sdk_datazone.types.enable_setting.deserialize_json(
            data["enableSetting"]
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
    if "schedule" in data:
        import aws_sdk_datazone.types.schedule_configuration

        out["schedule"] = (
            aws_sdk_datazone.types.schedule_configuration.deserialize_json(
                data["schedule"]
            )
        )
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
    if "retainPermissionsOnRevokeFailure" in data:
        out["retain_permissions_on_revoke_failure"] = data[
            "retainPermissionsOnRevokeFailure"
        ]
    return out
