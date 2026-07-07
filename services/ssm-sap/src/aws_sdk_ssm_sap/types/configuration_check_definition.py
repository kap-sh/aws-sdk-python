"""Generated from Smithy shape ``com.amazonaws.ssmsap#ConfigurationCheckDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm_sap.types.application_type_list
    import aws_sdk_ssm_sap.types.configuration_check_type


class ConfigurationCheckDefinition(TypedDict, closed=True):
    id: NotRequired[
        "aws_sdk_ssm_sap.types.configuration_check_type.ConfigurationCheckType"
    ]
    """<p>The unique identifier of the configuration check.</p>"""
    name: NotRequired["str"]
    """<p>The name of the configuration check.</p>"""
    description: NotRequired["str"]
    """<p>A description of what the configuration check validates.</p>"""
    applicable_application_types: NotRequired[
        "aws_sdk_ssm_sap.types.application_type_list.ApplicationTypeList"
    ]
    """<p>The list of SSMSAP application types that this configuration check can be evaluated against.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationCheckDefinition) -> dict:
    out: dict = {}
    if "id" in value:
        import aws_sdk_ssm_sap.types.configuration_check_type

        out["Id"] = aws_sdk_ssm_sap.types.configuration_check_type.serialize_json(
            value["id"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "applicable_application_types" in value:
        import aws_sdk_ssm_sap.types.application_type_list

        out["ApplicableApplicationTypes"] = (
            aws_sdk_ssm_sap.types.application_type_list.serialize_json(
                value["applicable_application_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConfigurationCheckDefinition:
    out: ConfigurationCheckDefinition = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        import aws_sdk_ssm_sap.types.configuration_check_type

        out["id"] = aws_sdk_ssm_sap.types.configuration_check_type.deserialize_json(
            data["Id"]
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "ApplicableApplicationTypes" in data:
        import aws_sdk_ssm_sap.types.application_type_list

        out["applicable_application_types"] = (
            aws_sdk_ssm_sap.types.application_type_list.deserialize_json(
                data["ApplicableApplicationTypes"]
            )
        )
    return out
