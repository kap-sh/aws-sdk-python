"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#EndpointSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.boolean_optional
    import capo_database_migration_service.types.endpoint_setting_enum_values
    import capo_database_migration_service.types.endpoint_setting_type_value
    import capo_database_migration_service.types.integer_optional
    import capo_database_migration_service.types.string


class EndpointSetting(TypedDict, closed=True):
    name: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The name that you want to give the endpoint settings.</p>"""
    type: NotRequired[
        "capo_database_migration_service.types.endpoint_setting_type_value.EndpointSettingTypeValue"
    ]
    """<p>The type of endpoint. Valid values are <code>source</code> and <code>target</code>.</p>"""
    enum_values: NotRequired[
        "capo_database_migration_service.types.endpoint_setting_enum_values.EndpointSettingEnumValues"
    ]
    """<p>Enumerated values to use for this endpoint.</p>"""
    sensitive: NotRequired[
        "capo_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>A value that marks this endpoint setting as sensitive.</p>"""
    units: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The unit of measure for this endpoint setting.</p>"""
    applicability: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The relevance or validity of an endpoint setting for an engine name and its endpoint type.</p>"""
    int_value_min: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The minimum value of an endpoint setting that is of type <code>int</code>.</p>"""
    int_value_max: NotRequired[
        "capo_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The maximum value of an endpoint setting that is of type <code>int</code>.</p>"""
    default_value: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The default value of the endpoint setting if no value is specified using <code>CreateEndpoint</code> or <code>ModifyEndpoint</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointSetting) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import capo_database_migration_service.types.endpoint_setting_type_value

        out["Type"] = (
            capo_database_migration_service.types.endpoint_setting_type_value.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "enum_values" in value:
        import capo_database_migration_service.types.endpoint_setting_enum_values

        out["EnumValues"] = (
            capo_database_migration_service.types.endpoint_setting_enum_values.serialize_aws_json_1_1(
                value["enum_values"]
            )
        )
    if "sensitive" in value:
        out["Sensitive"] = value["sensitive"]
    if "units" in value:
        out["Units"] = value["units"]
    if "applicability" in value:
        out["Applicability"] = value["applicability"]
    if "int_value_min" in value:
        out["IntValueMin"] = value["int_value_min"]
    if "int_value_max" in value:
        out["IntValueMax"] = value["int_value_max"]
    if "default_value" in value:
        out["DefaultValue"] = value["default_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EndpointSetting:
    out: EndpointSetting = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Type" in data:
        import capo_database_migration_service.types.endpoint_setting_type_value

        out["type"] = (
            capo_database_migration_service.types.endpoint_setting_type_value.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "EnumValues" in data:
        import capo_database_migration_service.types.endpoint_setting_enum_values

        out["enum_values"] = (
            capo_database_migration_service.types.endpoint_setting_enum_values.deserialize_aws_json_1_1(
                data["EnumValues"]
            )
        )
    if "Sensitive" in data:
        out["sensitive"] = data["Sensitive"]
    if "Units" in data:
        out["units"] = data["Units"]
    if "Applicability" in data:
        out["applicability"] = data["Applicability"]
    if "IntValueMin" in data:
        out["int_value_min"] = data["IntValueMin"]
    if "IntValueMax" in data:
        out["int_value_max"] = data["IntValueMax"]
    if "DefaultValue" in data:
        out["default_value"] = data["DefaultValue"]
    return out
