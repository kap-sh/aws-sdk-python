"""Generated from Smithy shape ``com.amazonaws.quicksight#BrandDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.application_theme
    import aws_sdk_quicksight.types.description
    import aws_sdk_quicksight.types.logo_configuration
    import aws_sdk_quicksight.types.name


class BrandDefinition(TypedDict):
    brand_name: "aws_sdk_quicksight.types.name.Name"
    """<p>The name of the brand.</p>"""
    description: NotRequired["aws_sdk_quicksight.types.description.Description"]
    """<p>The description of the brand.</p>"""
    application_theme: NotRequired[
        "aws_sdk_quicksight.types.application_theme.ApplicationTheme"
    ]
    """<p>The application theme of the brand.</p>"""
    logo_configuration: NotRequired[
        "aws_sdk_quicksight.types.logo_configuration.LogoConfiguration"
    ]
    """<p>The logo configuration of the brand.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrandDefinition) -> dict:
    out: dict = {}
    out["BrandName"] = value["brand_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "application_theme" in value:
        import aws_sdk_quicksight.types.application_theme

        out["ApplicationTheme"] = (
            aws_sdk_quicksight.types.application_theme.serialize_json(
                value["application_theme"]
            )
        )
    if "logo_configuration" in value:
        import aws_sdk_quicksight.types.logo_configuration

        out["LogoConfiguration"] = (
            aws_sdk_quicksight.types.logo_configuration.serialize_json(
                value["logo_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> BrandDefinition:
    out: BrandDefinition = {}  # type: ignore[typeddict-item]
    if "BrandName" in data:
        out["brand_name"] = data["BrandName"]
    else:
        raise DeserializationError("BrandDefinition.brand_name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "ApplicationTheme" in data:
        import aws_sdk_quicksight.types.application_theme

        out["application_theme"] = (
            aws_sdk_quicksight.types.application_theme.deserialize_json(
                data["ApplicationTheme"]
            )
        )
    if "LogoConfiguration" in data:
        import aws_sdk_quicksight.types.logo_configuration

        out["logo_configuration"] = (
            aws_sdk_quicksight.types.logo_configuration.deserialize_json(
                data["LogoConfiguration"]
            )
        )
    return out
