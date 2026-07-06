"""Generated from Smithy shape ``com.amazonaws.appflow#AuthParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appflow.types.boolean
    import aws_sdk_appflow.types.connector_supplied_value_list
    import aws_sdk_appflow.types.description
    import aws_sdk_appflow.types.key
    import aws_sdk_appflow.types.label


class AuthParameter(TypedDict, closed=True):
    key: NotRequired["aws_sdk_appflow.types.key.Key"]
    """<p>The authentication key required to authenticate with the connector.</p>"""
    is_required: "aws_sdk_appflow.types.boolean.Boolean"
    """<p>Indicates whether this authentication parameter is required.</p>"""
    label: NotRequired["aws_sdk_appflow.types.label.Label"]
    """<p>Label used for authentication parameter.</p>"""
    description: NotRequired["aws_sdk_appflow.types.description.Description"]
    """<p>A description about the authentication parameter.</p>"""
    is_sensitive_field: "aws_sdk_appflow.types.boolean.Boolean"
    """<p>Indicates whether this authentication parameter is a sensitive field.</p>"""
    connector_supplied_values: NotRequired[
        "aws_sdk_appflow.types.connector_supplied_value_list.ConnectorSuppliedValueList"
    ]
    """<p>Contains default values for this authentication parameter that are supplied by the connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthParameter) -> dict:
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
    return out


def deserialize_json(data: dict) -> AuthParameter:
    out: AuthParameter = {}  # type: ignore[typeddict-item]
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
    return out
