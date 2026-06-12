"""Generated from Smithy shape ``com.amazonaws.appconfig#ExtensionAssociation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.arn
    import aws_sdk_appconfig.types.identifier
    import aws_sdk_appconfig.types.integer
    import aws_sdk_appconfig.types.parameter_value_map


class ExtensionAssociation(TypedDict):
    id: NotRequired["aws_sdk_appconfig.types.identifier.Identifier"]
    """<p>The system-generated ID for the association.</p>"""
    extension_arn: NotRequired["aws_sdk_appconfig.types.arn.Arn"]
    """<p>The ARN of the extension defined in the association.</p>"""
    resource_arn: NotRequired["aws_sdk_appconfig.types.arn.Arn"]
    """<p>The ARNs of applications, configuration profiles, or environments defined in the association.</p>"""
    arn: NotRequired["aws_sdk_appconfig.types.arn.Arn"]
    """<p>The system-generated Amazon Resource Name (ARN) for the extension.</p>"""
    parameters: NotRequired[
        "aws_sdk_appconfig.types.parameter_value_map.ParameterValueMap"
    ]
    """<p>The parameter names and values defined in the association.</p>"""
    extension_version_number: "aws_sdk_appconfig.types.integer.Integer"
    """<p>The version number for the extension defined in the association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExtensionAssociation) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "extension_arn" in value:
        out["ExtensionArn"] = value["extension_arn"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "parameters" in value:
        import aws_sdk_appconfig.types.parameter_value_map

        out["Parameters"] = aws_sdk_appconfig.types.parameter_value_map.serialize_json(
            value["parameters"]
        )
    out["ExtensionVersionNumber"] = value.get("extension_version_number", 0)
    return out


def deserialize_json(data: dict) -> ExtensionAssociation:
    out: ExtensionAssociation = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "ExtensionArn" in data:
        out["extension_arn"] = data["ExtensionArn"]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Parameters" in data:
        import aws_sdk_appconfig.types.parameter_value_map

        out["parameters"] = (
            aws_sdk_appconfig.types.parameter_value_map.deserialize_json(
                data["Parameters"]
            )
        )
    if "ExtensionVersionNumber" in data:
        out["extension_version_number"] = data["ExtensionVersionNumber"]
    else:
        out["extension_version_number"] = 0
    return out
