"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElasticBeanstalkEnvironmentDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_elastic_beanstalk_environment_environment_links
    import aws_sdk_securityhub.types.aws_elastic_beanstalk_environment_option_settings
    import aws_sdk_securityhub.types.aws_elastic_beanstalk_environment_tier
    import aws_sdk_securityhub.types.non_empty_string


class AwsElasticBeanstalkEnvironmentDetails(TypedDict):
    application_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the application that is associated with the environment.</p>"""
    cname: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The URL to the CNAME for this environment.</p>"""
    date_created: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The creation date for this environment.</p>"""
    date_updated: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The date when this environment was last modified.</p>"""
    description: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>A description of the environment.</p>"""
    endpoint_url: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>For load-balanced, autoscaling environments, the URL to the load balancer. For single-instance environments, the IP address of the instance.</p>"""
    environment_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the environment.</p>"""
    environment_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the environment.</p>"""
    environment_links: NotRequired[
        "aws_sdk_securityhub.types.aws_elastic_beanstalk_environment_environment_links.AwsElasticBeanstalkEnvironmentEnvironmentLinks"
    ]
    """<p>Links to other environments in the same group.</p>"""
    environment_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the environment.</p>"""
    option_settings: NotRequired[
        "aws_sdk_securityhub.types.aws_elastic_beanstalk_environment_option_settings.AwsElasticBeanstalkEnvironmentOptionSettings"
    ]
    """<p>The configuration setting for the environment.</p>"""
    platform_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the platform version for the environment.</p>"""
    solution_stack_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the solution stack that is deployed with the environment.</p>"""
    status: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The current operational status of the environment. Valid values are as follows:</p> <ul> <li> <p> <code>Aborting</code> </p> </li> <li> <p> <code>Launching</code> </p> </li> <li> <p> <code>LinkingFrom</code> </p> </li> <li> <p> <code>LinkingTo</code> </p> </li> <li> <p> <code>Ready</code> </p> </li> <li> <p> <code>Terminated</code> </p> </li> <li> <p> <code>Terminating</code> </p> </li> <li> <p> <code>Updating</code> </p> </li> </ul>"""
    tier: NotRequired[
        "aws_sdk_securityhub.types.aws_elastic_beanstalk_environment_tier.AwsElasticBeanstalkEnvironmentTier"
    ]
    """<p>The tier of the environment.</p>"""
    version_label: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The application version of the environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsElasticBeanstalkEnvironmentDetails) -> dict:
    out: dict = {}
    if "application_name" in value:
        out["ApplicationName"] = value["application_name"]
    if "cname" in value:
        out["Cname"] = value["cname"]
    if "date_created" in value:
        out["DateCreated"] = value["date_created"]
    if "date_updated" in value:
        out["DateUpdated"] = value["date_updated"]
    if "description" in value:
        out["Description"] = value["description"]
    if "endpoint_url" in value:
        out["EndpointUrl"] = value["endpoint_url"]
    if "environment_arn" in value:
        out["EnvironmentArn"] = value["environment_arn"]
    if "environment_id" in value:
        out["EnvironmentId"] = value["environment_id"]
    if "environment_links" in value:
        import aws_sdk_securityhub.types.aws_elastic_beanstalk_environment_environment_links

        out["EnvironmentLinks"] = (
            aws_sdk_securityhub.types.aws_elastic_beanstalk_environment_environment_links.serialize_json(
                value["environment_links"]
            )
        )
    if "environment_name" in value:
        out["EnvironmentName"] = value["environment_name"]
    if "option_settings" in value:
        import aws_sdk_securityhub.types.aws_elastic_beanstalk_environment_option_settings

        out["OptionSettings"] = (
            aws_sdk_securityhub.types.aws_elastic_beanstalk_environment_option_settings.serialize_json(
                value["option_settings"]
            )
        )
    if "platform_arn" in value:
        out["PlatformArn"] = value["platform_arn"]
    if "solution_stack_name" in value:
        out["SolutionStackName"] = value["solution_stack_name"]
    if "status" in value:
        out["Status"] = value["status"]
    if "tier" in value:
        import aws_sdk_securityhub.types.aws_elastic_beanstalk_environment_tier

        out["Tier"] = (
            aws_sdk_securityhub.types.aws_elastic_beanstalk_environment_tier.serialize_json(
                value["tier"]
            )
        )
    if "version_label" in value:
        out["VersionLabel"] = value["version_label"]
    return out


def deserialize_json(data: dict) -> AwsElasticBeanstalkEnvironmentDetails:
    out: AwsElasticBeanstalkEnvironmentDetails = {}  # type: ignore[typeddict-item]
    if "ApplicationName" in data:
        out["application_name"] = data["ApplicationName"]
    if "Cname" in data:
        out["cname"] = data["Cname"]
    if "DateCreated" in data:
        out["date_created"] = data["DateCreated"]
    if "DateUpdated" in data:
        out["date_updated"] = data["DateUpdated"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "EndpointUrl" in data:
        out["endpoint_url"] = data["EndpointUrl"]
    if "EnvironmentArn" in data:
        out["environment_arn"] = data["EnvironmentArn"]
    if "EnvironmentId" in data:
        out["environment_id"] = data["EnvironmentId"]
    if "EnvironmentLinks" in data:
        import aws_sdk_securityhub.types.aws_elastic_beanstalk_environment_environment_links

        out["environment_links"] = (
            aws_sdk_securityhub.types.aws_elastic_beanstalk_environment_environment_links.deserialize_json(
                data["EnvironmentLinks"]
            )
        )
    if "EnvironmentName" in data:
        out["environment_name"] = data["EnvironmentName"]
    if "OptionSettings" in data:
        import aws_sdk_securityhub.types.aws_elastic_beanstalk_environment_option_settings

        out["option_settings"] = (
            aws_sdk_securityhub.types.aws_elastic_beanstalk_environment_option_settings.deserialize_json(
                data["OptionSettings"]
            )
        )
    if "PlatformArn" in data:
        out["platform_arn"] = data["PlatformArn"]
    if "SolutionStackName" in data:
        out["solution_stack_name"] = data["SolutionStackName"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "Tier" in data:
        import aws_sdk_securityhub.types.aws_elastic_beanstalk_environment_tier

        out["tier"] = (
            aws_sdk_securityhub.types.aws_elastic_beanstalk_environment_tier.deserialize_json(
                data["Tier"]
            )
        )
    if "VersionLabel" in data:
        out["version_label"] = data["VersionLabel"]
    return out
