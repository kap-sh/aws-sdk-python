"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ResourceQuotas``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.resource_quota


class ResourceQuotas(TypedDict, closed=True):
    application_quota: NotRequired[
        "capo_elastic_beanstalk.types.resource_quota.ResourceQuota"
    ]
    """<p>The quota for applications in the AWS account.</p>"""
    application_version_quota: NotRequired[
        "capo_elastic_beanstalk.types.resource_quota.ResourceQuota"
    ]
    """<p>The quota for application versions in the AWS account.</p>"""
    environment_quota: NotRequired[
        "capo_elastic_beanstalk.types.resource_quota.ResourceQuota"
    ]
    """<p>The quota for environments in the AWS account.</p>"""
    configuration_template_quota: NotRequired[
        "capo_elastic_beanstalk.types.resource_quota.ResourceQuota"
    ]
    """<p>The quota for configuration templates in the AWS account.</p>"""
    custom_platform_quota: NotRequired[
        "capo_elastic_beanstalk.types.resource_quota.ResourceQuota"
    ]
    """<p>The quota for custom platforms in the AWS account.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ResourceQuotas, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "application_quota" in value:
        import capo_elastic_beanstalk.types.resource_quota

        capo_elastic_beanstalk.types.resource_quota.serialize_query(
            value["application_quota"], pairs, f"{prefix}.ApplicationQuota"
        )
    if "application_version_quota" in value:
        import capo_elastic_beanstalk.types.resource_quota

        capo_elastic_beanstalk.types.resource_quota.serialize_query(
            value["application_version_quota"],
            pairs,
            f"{prefix}.ApplicationVersionQuota",
        )
    if "environment_quota" in value:
        import capo_elastic_beanstalk.types.resource_quota

        capo_elastic_beanstalk.types.resource_quota.serialize_query(
            value["environment_quota"], pairs, f"{prefix}.EnvironmentQuota"
        )
    if "configuration_template_quota" in value:
        import capo_elastic_beanstalk.types.resource_quota

        capo_elastic_beanstalk.types.resource_quota.serialize_query(
            value["configuration_template_quota"],
            pairs,
            f"{prefix}.ConfigurationTemplateQuota",
        )
    if "custom_platform_quota" in value:
        import capo_elastic_beanstalk.types.resource_quota

        capo_elastic_beanstalk.types.resource_quota.serialize_query(
            value["custom_platform_quota"], pairs, f"{prefix}.CustomPlatformQuota"
        )


def deserialize_query(el: Element) -> ResourceQuotas:
    out: ResourceQuotas = {}  # type: ignore[typeddict-item]
    child_application_quota = el.find("ApplicationQuota")
    if child_application_quota is not None:
        import capo_elastic_beanstalk.types.resource_quota

        out["application_quota"] = (
            capo_elastic_beanstalk.types.resource_quota.deserialize_query(
                child_application_quota
            )
        )
    child_application_version_quota = el.find("ApplicationVersionQuota")
    if child_application_version_quota is not None:
        import capo_elastic_beanstalk.types.resource_quota

        out["application_version_quota"] = (
            capo_elastic_beanstalk.types.resource_quota.deserialize_query(
                child_application_version_quota
            )
        )
    child_environment_quota = el.find("EnvironmentQuota")
    if child_environment_quota is not None:
        import capo_elastic_beanstalk.types.resource_quota

        out["environment_quota"] = (
            capo_elastic_beanstalk.types.resource_quota.deserialize_query(
                child_environment_quota
            )
        )
    child_configuration_template_quota = el.find("ConfigurationTemplateQuota")
    if child_configuration_template_quota is not None:
        import capo_elastic_beanstalk.types.resource_quota

        out["configuration_template_quota"] = (
            capo_elastic_beanstalk.types.resource_quota.deserialize_query(
                child_configuration_template_quota
            )
        )
    child_custom_platform_quota = el.find("CustomPlatformQuota")
    if child_custom_platform_quota is not None:
        import capo_elastic_beanstalk.types.resource_quota

        out["custom_platform_quota"] = (
            capo_elastic_beanstalk.types.resource_quota.deserialize_query(
                child_custom_platform_quota
            )
        )
    return out
