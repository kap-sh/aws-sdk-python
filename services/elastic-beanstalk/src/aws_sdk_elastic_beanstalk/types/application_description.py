"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ApplicationDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.application_arn
    import aws_sdk_elastic_beanstalk.types.application_name
    import aws_sdk_elastic_beanstalk.types.application_resource_lifecycle_config
    import aws_sdk_elastic_beanstalk.types.configuration_template_names_list
    import aws_sdk_elastic_beanstalk.types.creation_date
    import aws_sdk_elastic_beanstalk.types.description
    import aws_sdk_elastic_beanstalk.types.update_date
    import aws_sdk_elastic_beanstalk.types.version_labels_list


class ApplicationDescription(TypedDict):
    application_arn: NotRequired[
        "aws_sdk_elastic_beanstalk.types.application_arn.ApplicationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the application.</p>"""
    application_name: NotRequired[
        "aws_sdk_elastic_beanstalk.types.application_name.ApplicationName"
    ]
    """<p>The name of the application.</p>"""
    description: NotRequired["aws_sdk_elastic_beanstalk.types.description.Description"]
    """<p>User-defined description of the application.</p>"""
    date_created: NotRequired[
        "aws_sdk_elastic_beanstalk.types.creation_date.CreationDate"
    ]
    """<p>The date when the application was created.</p>"""
    date_updated: NotRequired["aws_sdk_elastic_beanstalk.types.update_date.UpdateDate"]
    """<p>The date when the application was last modified.</p>"""
    versions: NotRequired[
        "aws_sdk_elastic_beanstalk.types.version_labels_list.VersionLabelsList"
    ]
    """<p>The names of the versions for this application.</p>"""
    configuration_templates: NotRequired[
        "aws_sdk_elastic_beanstalk.types.configuration_template_names_list.ConfigurationTemplateNamesList"
    ]
    """<p>The names of the configuration templates associated with this application.</p>"""
    resource_lifecycle_config: NotRequired[
        "aws_sdk_elastic_beanstalk.types.application_resource_lifecycle_config.ApplicationResourceLifecycleConfig"
    ]
    """<p>The lifecycle settings for the application.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ApplicationDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "application_arn" in value:
        pairs.append((f"{prefix}.ApplicationArn", str(value["application_arn"])))
    if "application_name" in value:
        pairs.append((f"{prefix}.ApplicationName", str(value["application_name"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "date_created" in value:
        import aws_sdk_elastic_beanstalk.types.creation_date

        aws_sdk_elastic_beanstalk.types.creation_date.serialize_query(
            value["date_created"], pairs, f"{prefix}.DateCreated"
        )
    if "date_updated" in value:
        import aws_sdk_elastic_beanstalk.types.update_date

        aws_sdk_elastic_beanstalk.types.update_date.serialize_query(
            value["date_updated"], pairs, f"{prefix}.DateUpdated"
        )
    if "versions" in value:
        import aws_sdk_elastic_beanstalk.types.version_labels_list

        aws_sdk_elastic_beanstalk.types.version_labels_list.serialize_query(
            value["versions"], pairs, f"{prefix}.Versions"
        )
    if "configuration_templates" in value:
        import aws_sdk_elastic_beanstalk.types.configuration_template_names_list

        aws_sdk_elastic_beanstalk.types.configuration_template_names_list.serialize_query(
            value["configuration_templates"], pairs, f"{prefix}.ConfigurationTemplates"
        )
    if "resource_lifecycle_config" in value:
        import aws_sdk_elastic_beanstalk.types.application_resource_lifecycle_config

        aws_sdk_elastic_beanstalk.types.application_resource_lifecycle_config.serialize_query(
            value["resource_lifecycle_config"],
            pairs,
            f"{prefix}.ResourceLifecycleConfig",
        )


def deserialize_query(el: Element) -> ApplicationDescription:
    out: ApplicationDescription = {}  # type: ignore[typeddict-item]
    child_application_arn = el.find("ApplicationArn")
    if child_application_arn is not None:
        out["application_arn"] = str(child_application_arn.text or "")
    child_application_name = el.find("ApplicationName")
    if child_application_name is not None:
        out["application_name"] = str(child_application_name.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_date_created = el.find("DateCreated")
    if child_date_created is not None:
        import aws_sdk_elastic_beanstalk.types.creation_date

        out["date_created"] = (
            aws_sdk_elastic_beanstalk.types.creation_date.deserialize_query(
                child_date_created
            )
        )
    child_date_updated = el.find("DateUpdated")
    if child_date_updated is not None:
        import aws_sdk_elastic_beanstalk.types.update_date

        out["date_updated"] = (
            aws_sdk_elastic_beanstalk.types.update_date.deserialize_query(
                child_date_updated
            )
        )
    child_versions = el.find("Versions")
    if child_versions is not None:
        import aws_sdk_elastic_beanstalk.types.version_labels_list

        out["versions"] = (
            aws_sdk_elastic_beanstalk.types.version_labels_list.deserialize_query(
                child_versions
            )
        )
    child_configuration_templates = el.find("ConfigurationTemplates")
    if child_configuration_templates is not None:
        import aws_sdk_elastic_beanstalk.types.configuration_template_names_list

        out["configuration_templates"] = (
            aws_sdk_elastic_beanstalk.types.configuration_template_names_list.deserialize_query(
                child_configuration_templates
            )
        )
    child_resource_lifecycle_config = el.find("ResourceLifecycleConfig")
    if child_resource_lifecycle_config is not None:
        import aws_sdk_elastic_beanstalk.types.application_resource_lifecycle_config

        out["resource_lifecycle_config"] = (
            aws_sdk_elastic_beanstalk.types.application_resource_lifecycle_config.deserialize_query(
                child_resource_lifecycle_config
            )
        )
    return out
