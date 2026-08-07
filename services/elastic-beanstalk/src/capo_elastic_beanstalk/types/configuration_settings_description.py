"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ConfigurationSettingsDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.application_name
    import capo_elastic_beanstalk.types.configuration_deployment_status
    import capo_elastic_beanstalk.types.configuration_option_settings_list
    import capo_elastic_beanstalk.types.configuration_template_name
    import capo_elastic_beanstalk.types.creation_date
    import capo_elastic_beanstalk.types.description
    import capo_elastic_beanstalk.types.environment_name
    import capo_elastic_beanstalk.types.platform_arn
    import capo_elastic_beanstalk.types.solution_stack_name
    import capo_elastic_beanstalk.types.update_date


class ConfigurationSettingsDescription(TypedDict, closed=True):
    solution_stack_name: NotRequired[
        "capo_elastic_beanstalk.types.solution_stack_name.SolutionStackName"
    ]
    """<p>The name of the solution stack this configuration set uses.</p>"""
    platform_arn: NotRequired["capo_elastic_beanstalk.types.platform_arn.PlatformArn"]
    """<p>The ARN of the platform version.</p>"""
    application_name: NotRequired[
        "capo_elastic_beanstalk.types.application_name.ApplicationName"
    ]
    """<p>The name of the application associated with this configuration set.</p>"""
    template_name: NotRequired[
        "capo_elastic_beanstalk.types.configuration_template_name.ConfigurationTemplateName"
    ]
    """<p> If not <code>null</code>, the name of the configuration template for this configuration set. </p>"""
    description: NotRequired["capo_elastic_beanstalk.types.description.Description"]
    """<p>Describes this configuration set.</p>"""
    environment_name: NotRequired[
        "capo_elastic_beanstalk.types.environment_name.EnvironmentName"
    ]
    """<p> If not <code>null</code>, the name of the environment for this configuration set. </p>"""
    deployment_status: NotRequired[
        "capo_elastic_beanstalk.types.configuration_deployment_status.ConfigurationDeploymentStatus"
    ]
    """<p> If this configuration set is associated with an environment, the <code>DeploymentStatus</code> parameter indicates the deployment status of this configuration set: </p> <ul> <li> <p> <code>null</code>: This configuration is not associated with a running environment.</p> </li> <li> <p> <code>pending</code>: This is a draft configuration that is not deployed to the associated environment but is in the process of deploying.</p> </li> <li> <p> <code>deployed</code>: This is the configuration that is currently deployed to the associated running environment.</p> </li> <li> <p> <code>failed</code>: This is a draft configuration that failed to successfully deploy.</p> </li> </ul>"""
    date_created: NotRequired["capo_elastic_beanstalk.types.creation_date.CreationDate"]
    """<p>The date (in UTC time) when this configuration set was created.</p>"""
    date_updated: NotRequired["capo_elastic_beanstalk.types.update_date.UpdateDate"]
    """<p>The date (in UTC time) when this configuration set was last modified.</p>"""
    option_settings: NotRequired[
        "capo_elastic_beanstalk.types.configuration_option_settings_list.ConfigurationOptionSettingsList"
    ]
    """<p>A list of the configuration options and their values in this configuration set.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ConfigurationSettingsDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "solution_stack_name" in value:
        pairs.append(
            (f"{key_prefix}SolutionStackName", str(value["solution_stack_name"]))
        )
    if "platform_arn" in value:
        pairs.append((f"{key_prefix}PlatformArn", str(value["platform_arn"])))
    if "application_name" in value:
        pairs.append((f"{key_prefix}ApplicationName", str(value["application_name"])))
    if "template_name" in value:
        pairs.append((f"{key_prefix}TemplateName", str(value["template_name"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "environment_name" in value:
        pairs.append((f"{key_prefix}EnvironmentName", str(value["environment_name"])))
    if "deployment_status" in value:
        import capo_elastic_beanstalk.types.configuration_deployment_status

        capo_elastic_beanstalk.types.configuration_deployment_status.serialize_query(
            value["deployment_status"], pairs, f"{key_prefix}DeploymentStatus"
        )
    if "date_created" in value:
        import capo_elastic_beanstalk.types.creation_date

        capo_elastic_beanstalk.types.creation_date.serialize_query(
            value["date_created"], pairs, f"{key_prefix}DateCreated"
        )
    if "date_updated" in value:
        import capo_elastic_beanstalk.types.update_date

        capo_elastic_beanstalk.types.update_date.serialize_query(
            value["date_updated"], pairs, f"{key_prefix}DateUpdated"
        )
    if "option_settings" in value:
        import capo_elastic_beanstalk.types.configuration_option_settings_list

        capo_elastic_beanstalk.types.configuration_option_settings_list.serialize_query(
            value["option_settings"], pairs, f"{key_prefix}OptionSettings"
        )


def deserialize_query(el: Element) -> ConfigurationSettingsDescription:
    out: ConfigurationSettingsDescription = {}  # type: ignore[typeddict-item]
    child_solution_stack_name = el.find("SolutionStackName")
    if child_solution_stack_name is not None:
        out["solution_stack_name"] = str(child_solution_stack_name.text or "")
    child_platform_arn = el.find("PlatformArn")
    if child_platform_arn is not None:
        out["platform_arn"] = str(child_platform_arn.text or "")
    child_application_name = el.find("ApplicationName")
    if child_application_name is not None:
        out["application_name"] = str(child_application_name.text or "")
    child_template_name = el.find("TemplateName")
    if child_template_name is not None:
        out["template_name"] = str(child_template_name.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_environment_name = el.find("EnvironmentName")
    if child_environment_name is not None:
        out["environment_name"] = str(child_environment_name.text or "")
    child_deployment_status = el.find("DeploymentStatus")
    if child_deployment_status is not None:
        import capo_elastic_beanstalk.types.configuration_deployment_status

        out["deployment_status"] = (
            capo_elastic_beanstalk.types.configuration_deployment_status.deserialize_query(
                child_deployment_status
            )
        )
    child_date_created = el.find("DateCreated")
    if child_date_created is not None:
        import capo_elastic_beanstalk.types.creation_date

        out["date_created"] = (
            capo_elastic_beanstalk.types.creation_date.deserialize_query(
                child_date_created
            )
        )
    child_date_updated = el.find("DateUpdated")
    if child_date_updated is not None:
        import capo_elastic_beanstalk.types.update_date

        out["date_updated"] = (
            capo_elastic_beanstalk.types.update_date.deserialize_query(
                child_date_updated
            )
        )
    child_option_settings = el.find("OptionSettings")
    if child_option_settings is not None:
        import capo_elastic_beanstalk.types.configuration_option_settings_list

        out["option_settings"] = (
            capo_elastic_beanstalk.types.configuration_option_settings_list.deserialize_query(
                child_option_settings
            )
        )
    return out
