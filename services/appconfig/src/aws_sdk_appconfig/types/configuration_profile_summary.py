"""Generated from Smithy shape ``com.amazonaws.appconfig#ConfigurationProfileSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.configuration_profile_type
    import aws_sdk_appconfig.types.id
    import aws_sdk_appconfig.types.long_name
    import aws_sdk_appconfig.types.uri
    import aws_sdk_appconfig.types.validator_type_list


class ConfigurationProfileSummary(TypedDict, closed=True):
    application_id: NotRequired["aws_sdk_appconfig.types.id.Id"]
    """<p>The application ID.</p>"""
    id: NotRequired["aws_sdk_appconfig.types.id.Id"]
    """<p>The ID of the configuration profile.</p>"""
    name: NotRequired["aws_sdk_appconfig.types.long_name.LongName"]
    """<p>The name of the configuration profile.</p>"""
    location_uri: NotRequired["aws_sdk_appconfig.types.uri.Uri"]
    """<p>The URI location of the configuration.</p>"""
    validator_types: NotRequired[
        "aws_sdk_appconfig.types.validator_type_list.ValidatorTypeList"
    ]
    """<p>The types of validators in the configuration profile.</p>"""
    type: NotRequired[
        "aws_sdk_appconfig.types.configuration_profile_type.ConfigurationProfileType"
    ]
    """<p>The type of configurations contained in the profile. AppConfig supports <code>feature flags</code> and <code>freeform</code> configurations. We recommend you create feature flag configurations to enable or disable new features and freeform configurations to distribute configurations to an application. When calling this API, enter one of the following values for <code>Type</code>:</p> <p> <code>AWS.AppConfig.FeatureFlags</code> </p> <p> <code>AWS.Freeform</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationProfileSummary) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "location_uri" in value:
        out["LocationUri"] = value["location_uri"]
    if "validator_types" in value:
        import aws_sdk_appconfig.types.validator_type_list

        out["ValidatorTypes"] = (
            aws_sdk_appconfig.types.validator_type_list.serialize_json(
                value["validator_types"]
            )
        )
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> ConfigurationProfileSummary:
    out: ConfigurationProfileSummary = {}  # type: ignore[typeddict-item]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "LocationUri" in data:
        out["location_uri"] = data["LocationUri"]
    if "ValidatorTypes" in data:
        import aws_sdk_appconfig.types.validator_type_list

        out["validator_types"] = (
            aws_sdk_appconfig.types.validator_type_list.deserialize_json(
                data["ValidatorTypes"]
            )
        )
    if "Type" in data:
        out["type"] = data["Type"]
    return out
