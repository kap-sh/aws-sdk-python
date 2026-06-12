"""Generated from Smithy shape ``com.amazonaws.appflow#OAuth2CustomParameter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appflow.types.boolean
    import aws_sdk_appflow.types.connector_supplied_value_list
    import aws_sdk_appflow.types.description
    import aws_sdk_appflow.types.key
    import aws_sdk_appflow.types.label
    import aws_sdk_appflow.types.o_auth2_custom_prop_type


class OAuth2CustomParameter(TypedDict):
    key: NotRequired["aws_sdk_appflow.types.key.Key"]
    """<p>The key of the custom parameter required for OAuth 2.0 authentication.</p>"""
    is_required: "aws_sdk_appflow.types.boolean.Boolean"
    """<p>Indicates whether the custom parameter for OAuth 2.0 authentication is required.</p>"""
    label: NotRequired["aws_sdk_appflow.types.label.Label"]
    """<p>The label of the custom parameter used for OAuth 2.0 authentication.</p>"""
    description: NotRequired["aws_sdk_appflow.types.description.Description"]
    """<p>A description about the custom parameter used for OAuth 2.0 authentication.</p>"""
    is_sensitive_field: "aws_sdk_appflow.types.boolean.Boolean"
    """<p>Indicates whether this authentication custom parameter is a sensitive field.</p>"""
    connector_supplied_values: NotRequired[
        "aws_sdk_appflow.types.connector_supplied_value_list.ConnectorSuppliedValueList"
    ]
    """<p>Contains default values for this authentication parameter that are supplied by the connector.</p>"""
    type: NotRequired[
        "aws_sdk_appflow.types.o_auth2_custom_prop_type.OAuth2CustomPropType"
    ]
    """<p>Indicates whether custom parameter is used with TokenUrl or AuthUrl.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OAuth2CustomParameter) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    out["isRequired"] = value.get("is_required", False)
    if "label" in value:
        out["label"] = value["label"]
    if "description" in value:
        out["description"] = value["description"]
    out["isSensitiveField"] = value.get("is_sensitive_field", False)
    if "connector_supplied_values" in value:
        import aws_sdk_appflow.types.connector_supplied_value_list

        out["connectorSuppliedValues"] = (
            aws_sdk_appflow.types.connector_supplied_value_list.serialize_json(
                value["connector_supplied_values"]
            )
        )
    if "type" in value:
        import aws_sdk_appflow.types.o_auth2_custom_prop_type

        out["type"] = aws_sdk_appflow.types.o_auth2_custom_prop_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> OAuth2CustomParameter:
    out: OAuth2CustomParameter = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    if "isRequired" in data:
        out["is_required"] = data["isRequired"]
    else:
        out["is_required"] = False
    if "label" in data:
        out["label"] = data["label"]
    if "description" in data:
        out["description"] = data["description"]
    if "isSensitiveField" in data:
        out["is_sensitive_field"] = data["isSensitiveField"]
    else:
        out["is_sensitive_field"] = False
    if "connectorSuppliedValues" in data:
        import aws_sdk_appflow.types.connector_supplied_value_list

        out["connector_supplied_values"] = (
            aws_sdk_appflow.types.connector_supplied_value_list.deserialize_json(
                data["connectorSuppliedValues"]
            )
        )
    if "type" in data:
        import aws_sdk_appflow.types.o_auth2_custom_prop_type

        out["type"] = aws_sdk_appflow.types.o_auth2_custom_prop_type.deserialize_json(
            data["type"]
        )
    return out
