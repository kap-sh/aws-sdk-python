"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorRuntimeSetting``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appflow.types.boolean
    import aws_sdk_appflow.types.connector_runtime_setting_data_type
    import aws_sdk_appflow.types.connector_runtime_setting_scope
    import aws_sdk_appflow.types.connector_supplied_value_option_list
    import aws_sdk_appflow.types.description
    import aws_sdk_appflow.types.key
    import aws_sdk_appflow.types.label


class ConnectorRuntimeSetting(TypedDict):
    key: NotRequired["aws_sdk_appflow.types.key.Key"]
    """<p>Contains value information about the connector runtime setting.</p>"""
    data_type: NotRequired[
        "aws_sdk_appflow.types.connector_runtime_setting_data_type.ConnectorRuntimeSettingDataType"
    ]
    """<p>Data type of the connector runtime setting.</p>"""
    is_required: "aws_sdk_appflow.types.boolean.Boolean"
    """<p>Indicates whether this connector runtime setting is required.</p>"""
    label: NotRequired["aws_sdk_appflow.types.label.Label"]
    """<p>A label used for connector runtime setting.</p>"""
    description: NotRequired["aws_sdk_appflow.types.description.Description"]
    """<p>A description about the connector runtime setting.</p>"""
    scope: NotRequired[
        "aws_sdk_appflow.types.connector_runtime_setting_scope.ConnectorRuntimeSettingScope"
    ]
    """<p>Indicates the scope of the connector runtime setting.</p>"""
    connector_supplied_value_options: NotRequired[
        "aws_sdk_appflow.types.connector_supplied_value_option_list.ConnectorSuppliedValueOptionList"
    ]
    """<p>Contains default values for the connector runtime setting that are supplied by the connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorRuntimeSetting) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "data_type" in value:
        out["dataType"] = value["data_type"]
    out["isRequired"] = value.get("is_required", False)
    if "label" in value:
        out["label"] = value["label"]
    if "description" in value:
        out["description"] = value["description"]
    if "scope" in value:
        out["scope"] = value["scope"]
    if "connector_supplied_value_options" in value:
        import aws_sdk_appflow.types.connector_supplied_value_option_list

        out["connectorSuppliedValueOptions"] = (
            aws_sdk_appflow.types.connector_supplied_value_option_list.serialize_json(
                value["connector_supplied_value_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConnectorRuntimeSetting:
    out: ConnectorRuntimeSetting = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    if "dataType" in data:
        out["data_type"] = data["dataType"]
    if "isRequired" in data:
        out["is_required"] = data["isRequired"]
    else:
        out["is_required"] = False
    if "label" in data:
        out["label"] = data["label"]
    if "description" in data:
        out["description"] = data["description"]
    if "scope" in data:
        out["scope"] = data["scope"]
    if "connectorSuppliedValueOptions" in data:
        import aws_sdk_appflow.types.connector_supplied_value_option_list

        out["connector_supplied_value_options"] = (
            aws_sdk_appflow.types.connector_supplied_value_option_list.deserialize_json(
                data["connectorSuppliedValueOptions"]
            )
        )
    return out
