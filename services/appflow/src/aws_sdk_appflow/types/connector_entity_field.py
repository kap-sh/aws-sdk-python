"""Generated from Smithy shape ``com.amazonaws.appflow#ConnectorEntityField``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.boolean
    import aws_sdk_appflow.types.custom_properties
    import aws_sdk_appflow.types.description
    import aws_sdk_appflow.types.destination_field_properties
    import aws_sdk_appflow.types.identifier
    import aws_sdk_appflow.types.label
    import aws_sdk_appflow.types.source_field_properties
    import aws_sdk_appflow.types.string
    import aws_sdk_appflow.types.supported_field_type_details


class ConnectorEntityField(TypedDict):
    identifier: "aws_sdk_appflow.types.identifier.Identifier"
    """<p> The unique identifier of the connector field. </p>"""
    parent_identifier: NotRequired["aws_sdk_appflow.types.identifier.Identifier"]
    """<p>The parent identifier of the connector field.</p>"""
    label: NotRequired["aws_sdk_appflow.types.label.Label"]
    """<p> The label applied to a connector entity field. </p>"""
    is_primary_key: "aws_sdk_appflow.types.boolean.Boolean"
    """<p>Booelan value that indicates whether this field can be used as a primary key.</p>"""
    default_value: NotRequired["aws_sdk_appflow.types.string.String"]
    """<p>Default value that can be assigned to this field.</p>"""
    is_deprecated: "aws_sdk_appflow.types.boolean.Boolean"
    """<p>Booelan value that indicates whether this field is deprecated or not.</p>"""
    supported_field_type_details: NotRequired[
        "aws_sdk_appflow.types.supported_field_type_details.SupportedFieldTypeDetails"
    ]
    """<p> Contains details regarding the supported <code>FieldType</code>, including the corresponding <code>filterOperators</code> and <code>supportedValues</code>. </p>"""
    description: NotRequired["aws_sdk_appflow.types.description.Description"]
    """<p> A description of the connector entity field. </p>"""
    source_properties: NotRequired[
        "aws_sdk_appflow.types.source_field_properties.SourceFieldProperties"
    ]
    """<p> The properties that can be applied to a field when the connector is being used as a source. </p>"""
    destination_properties: NotRequired[
        "aws_sdk_appflow.types.destination_field_properties.DestinationFieldProperties"
    ]
    """<p> The properties applied to a field when the connector is being used as a destination. </p>"""
    custom_properties: NotRequired[
        "aws_sdk_appflow.types.custom_properties.CustomProperties"
    ]
    """<p>A map that has specific properties related to the ConnectorEntityField.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorEntityField) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    if "parent_identifier" in value:
        out["parentIdentifier"] = value["parent_identifier"]
    if "label" in value:
        out["label"] = value["label"]
    out["isPrimaryKey"] = value.get("is_primary_key", False)
    if "default_value" in value:
        out["defaultValue"] = value["default_value"]
    out["isDeprecated"] = value.get("is_deprecated", False)
    if "supported_field_type_details" in value:
        import aws_sdk_appflow.types.supported_field_type_details

        out["supportedFieldTypeDetails"] = (
            aws_sdk_appflow.types.supported_field_type_details.serialize_json(
                value["supported_field_type_details"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "source_properties" in value:
        import aws_sdk_appflow.types.source_field_properties

        out["sourceProperties"] = (
            aws_sdk_appflow.types.source_field_properties.serialize_json(
                value["source_properties"]
            )
        )
    if "destination_properties" in value:
        import aws_sdk_appflow.types.destination_field_properties

        out["destinationProperties"] = (
            aws_sdk_appflow.types.destination_field_properties.serialize_json(
                value["destination_properties"]
            )
        )
    if "custom_properties" in value:
        import aws_sdk_appflow.types.custom_properties

        out["customProperties"] = (
            aws_sdk_appflow.types.custom_properties.serialize_json(
                value["custom_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConnectorEntityField:
    out: ConnectorEntityField = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("ConnectorEntityField.identifier required")
    if "parentIdentifier" in data:
        out["parent_identifier"] = data["parentIdentifier"]
    if "label" in data:
        out["label"] = data["label"]
    if "isPrimaryKey" in data:
        out["is_primary_key"] = data["isPrimaryKey"]
    else:
        out["is_primary_key"] = False
    if "defaultValue" in data:
        out["default_value"] = data["defaultValue"]
    if "isDeprecated" in data:
        out["is_deprecated"] = data["isDeprecated"]
    else:
        out["is_deprecated"] = False
    if "supportedFieldTypeDetails" in data:
        import aws_sdk_appflow.types.supported_field_type_details

        out["supported_field_type_details"] = (
            aws_sdk_appflow.types.supported_field_type_details.deserialize_json(
                data["supportedFieldTypeDetails"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "sourceProperties" in data:
        import aws_sdk_appflow.types.source_field_properties

        out["source_properties"] = (
            aws_sdk_appflow.types.source_field_properties.deserialize_json(
                data["sourceProperties"]
            )
        )
    if "destinationProperties" in data:
        import aws_sdk_appflow.types.destination_field_properties

        out["destination_properties"] = (
            aws_sdk_appflow.types.destination_field_properties.deserialize_json(
                data["destinationProperties"]
            )
        )
    if "customProperties" in data:
        import aws_sdk_appflow.types.custom_properties

        out["custom_properties"] = (
            aws_sdk_appflow.types.custom_properties.deserialize_json(
                data["customProperties"]
            )
        )
    return out
