"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#CreatePlatformVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_beanstalk._protocol.xml import Element
from aws_sdk_elastic_beanstalk.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.configuration_option_settings_list
    import aws_sdk_elastic_beanstalk.types.environment_name
    import aws_sdk_elastic_beanstalk.types.platform_name
    import aws_sdk_elastic_beanstalk.types.platform_version
    import aws_sdk_elastic_beanstalk.types.s3_location
    import aws_sdk_elastic_beanstalk.types.tags


class CreatePlatformVersionRequest(TypedDict):
    platform_name: "aws_sdk_elastic_beanstalk.types.platform_name.PlatformName"
    """<p>The name of your custom platform.</p>"""
    platform_version: "aws_sdk_elastic_beanstalk.types.platform_version.PlatformVersion"
    """<p>The number, such as 1.0.2, for the new platform version.</p>"""
    platform_definition_bundle: "aws_sdk_elastic_beanstalk.types.s3_location.S3Location"
    """<p>The location of the platform definition archive in Amazon S3.</p>"""
    environment_name: NotRequired[
        "aws_sdk_elastic_beanstalk.types.environment_name.EnvironmentName"
    ]
    """<p>The name of the builder environment.</p>"""
    option_settings: NotRequired[
        "aws_sdk_elastic_beanstalk.types.configuration_option_settings_list.ConfigurationOptionSettingsList"
    ]
    """<p>The configuration option settings to apply to the builder environment.</p>"""
    tags: NotRequired["aws_sdk_elastic_beanstalk.types.tags.Tags"]
    """<p>Specifies the tags applied to the new platform version.</p> <p>Elastic Beanstalk applies these tags only to the platform version. Environments that you create using the platform version don't inherit the tags.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreatePlatformVersionRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.PlatformName", str(value["platform_name"])))
    pairs.append((f"{prefix}.PlatformVersion", str(value["platform_version"])))
    import aws_sdk_elastic_beanstalk.types.s3_location

    aws_sdk_elastic_beanstalk.types.s3_location.serialize_query(
        value["platform_definition_bundle"], pairs, f"{prefix}.PlatformDefinitionBundle"
    )
    if "environment_name" in value:
        pairs.append((f"{prefix}.EnvironmentName", str(value["environment_name"])))
    if "option_settings" in value:
        import aws_sdk_elastic_beanstalk.types.configuration_option_settings_list

        aws_sdk_elastic_beanstalk.types.configuration_option_settings_list.serialize_query(
            value["option_settings"], pairs, f"{prefix}.OptionSettings"
        )
    if "tags" in value:
        import aws_sdk_elastic_beanstalk.types.tags

        aws_sdk_elastic_beanstalk.types.tags.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> CreatePlatformVersionRequest:
    out: CreatePlatformVersionRequest = {}  # type: ignore[typeddict-item]
    child_platform_name = el.find("PlatformName")
    if child_platform_name is not None:
        out["platform_name"] = str(child_platform_name.text or "")
    else:
        raise DeserializationError(
            "CreatePlatformVersionRequest.platform_name required"
        )
    child_platform_version = el.find("PlatformVersion")
    if child_platform_version is not None:
        out["platform_version"] = str(child_platform_version.text or "")
    else:
        raise DeserializationError(
            "CreatePlatformVersionRequest.platform_version required"
        )
    child_platform_definition_bundle = el.find("PlatformDefinitionBundle")
    if child_platform_definition_bundle is not None:
        import aws_sdk_elastic_beanstalk.types.s3_location

        out["platform_definition_bundle"] = (
            aws_sdk_elastic_beanstalk.types.s3_location.deserialize_query(
                child_platform_definition_bundle
            )
        )
    else:
        raise DeserializationError(
            "CreatePlatformVersionRequest.platform_definition_bundle required"
        )
    child_environment_name = el.find("EnvironmentName")
    if child_environment_name is not None:
        out["environment_name"] = str(child_environment_name.text or "")
    child_option_settings = el.find("OptionSettings")
    if child_option_settings is not None:
        import aws_sdk_elastic_beanstalk.types.configuration_option_settings_list

        out["option_settings"] = (
            aws_sdk_elastic_beanstalk.types.configuration_option_settings_list.deserialize_query(
                child_option_settings
            )
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_elastic_beanstalk.types.tags

        out["tags"] = aws_sdk_elastic_beanstalk.types.tags.deserialize_query(child_tags)
    return out
