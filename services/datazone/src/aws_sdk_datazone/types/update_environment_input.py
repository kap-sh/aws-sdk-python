"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateEnvironmentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.environment_configuration_name
    import aws_sdk_datazone.types.environment_id
    import aws_sdk_datazone.types.environment_parameters_list
    import aws_sdk_datazone.types.glossary_terms


class UpdateEnvironmentInput(TypedDict, closed=True):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the domain in which the environment is to be updated.</p>"""
    identifier: "aws_sdk_datazone.types.environment_id.EnvironmentId"
    """<p>The identifier of the environment that is to be updated.</p>"""
    name: NotRequired["str"]
    """<p>The name to be updated as part of the <code>UpdateEnvironment</code> action.</p>"""
    description: NotRequired["str"]
    """<p>The description to be updated as part of the <code>UpdateEnvironment</code> action.</p>"""
    glossary_terms: NotRequired["aws_sdk_datazone.types.glossary_terms.GlossaryTerms"]
    """<p>The glossary terms to be updated as part of the <code>UpdateEnvironment</code> action.</p>"""
    blueprint_version: NotRequired["str"]
    """<p>The blueprint version to which the environment should be updated. You can only specify the following string for this parameter: <code>latest</code>.</p>"""
    user_parameters: NotRequired[
        "aws_sdk_datazone.types.environment_parameters_list.EnvironmentParametersList"
    ]
    """<p>The user parameters of the environment.</p>"""
    environment_configuration_name: NotRequired[
        "aws_sdk_datazone.types.environment_configuration_name.EnvironmentConfigurationName"
    ]
    """<p>The configuration name of the environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEnvironmentInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "glossary_terms" in value:
        import aws_sdk_datazone.types.glossary_terms

        out["glossaryTerms"] = aws_sdk_datazone.types.glossary_terms.serialize_json(
            value["glossary_terms"]
        )
    if "blueprint_version" in value:
        out["blueprintVersion"] = value["blueprint_version"]
    if "user_parameters" in value:
        import aws_sdk_datazone.types.environment_parameters_list

        out["userParameters"] = (
            aws_sdk_datazone.types.environment_parameters_list.serialize_json(
                value["user_parameters"]
            )
        )
    if "environment_configuration_name" in value:
        out["environmentConfigurationName"] = value["environment_configuration_name"]
    return out


def deserialize_json(data: dict) -> UpdateEnvironmentInput:
    out: UpdateEnvironmentInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "glossaryTerms" in data:
        import aws_sdk_datazone.types.glossary_terms

        out["glossary_terms"] = aws_sdk_datazone.types.glossary_terms.deserialize_json(
            data["glossaryTerms"]
        )
    if "blueprintVersion" in data:
        out["blueprint_version"] = data["blueprintVersion"]
    if "userParameters" in data:
        import aws_sdk_datazone.types.environment_parameters_list

        out["user_parameters"] = (
            aws_sdk_datazone.types.environment_parameters_list.deserialize_json(
                data["userParameters"]
            )
        )
    if "environmentConfigurationName" in data:
        out["environment_configuration_name"] = data["environmentConfigurationName"]
    return out
