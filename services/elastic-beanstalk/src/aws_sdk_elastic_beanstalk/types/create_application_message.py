"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#CreateApplicationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_beanstalk._protocol.xml import Element
from aws_sdk_elastic_beanstalk.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.application_name
    import aws_sdk_elastic_beanstalk.types.application_resource_lifecycle_config
    import aws_sdk_elastic_beanstalk.types.description
    import aws_sdk_elastic_beanstalk.types.tags


class CreateApplicationMessage(TypedDict, closed=True):
    application_name: "aws_sdk_elastic_beanstalk.types.application_name.ApplicationName"
    """<p>The name of the application. Must be unique within your account.</p>"""
    description: NotRequired["aws_sdk_elastic_beanstalk.types.description.Description"]
    """<p>Your description of the application.</p>"""
    resource_lifecycle_config: NotRequired[
        "aws_sdk_elastic_beanstalk.types.application_resource_lifecycle_config.ApplicationResourceLifecycleConfig"
    ]
    """<p>Specifies an application resource lifecycle configuration to prevent your application from accumulating too many versions.</p>"""
    tags: NotRequired["aws_sdk_elastic_beanstalk.types.tags.Tags"]
    """<p>Specifies the tags applied to the application.</p> <p>Elastic Beanstalk applies these tags only to the application. Environments that you create in the application don't inherit the tags.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateApplicationMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.ApplicationName", str(value["application_name"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "resource_lifecycle_config" in value:
        import aws_sdk_elastic_beanstalk.types.application_resource_lifecycle_config

        aws_sdk_elastic_beanstalk.types.application_resource_lifecycle_config.serialize_query(
            value["resource_lifecycle_config"],
            pairs,
            f"{prefix}.ResourceLifecycleConfig",
        )
    if "tags" in value:
        import aws_sdk_elastic_beanstalk.types.tags

        aws_sdk_elastic_beanstalk.types.tags.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> CreateApplicationMessage:
    out: CreateApplicationMessage = {}  # type: ignore[typeddict-item]
    child_application_name = el.find("ApplicationName")
    if child_application_name is not None:
        out["application_name"] = str(child_application_name.text or "")
    else:
        raise DeserializationError("CreateApplicationMessage.application_name required")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_resource_lifecycle_config = el.find("ResourceLifecycleConfig")
    if child_resource_lifecycle_config is not None:
        import aws_sdk_elastic_beanstalk.types.application_resource_lifecycle_config

        out["resource_lifecycle_config"] = (
            aws_sdk_elastic_beanstalk.types.application_resource_lifecycle_config.deserialize_query(
                child_resource_lifecycle_config
            )
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_elastic_beanstalk.types.tags

        out["tags"] = aws_sdk_elastic_beanstalk.types.tags.deserialize_query(child_tags)
    return out
