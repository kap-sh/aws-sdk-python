"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ApplicationResourceLifecycleDescriptionMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.application_name
    import aws_sdk_elastic_beanstalk.types.application_resource_lifecycle_config


class ApplicationResourceLifecycleDescriptionMessage(TypedDict):
    application_name: NotRequired[
        "aws_sdk_elastic_beanstalk.types.application_name.ApplicationName"
    ]
    """<p>The name of the application.</p>"""
    resource_lifecycle_config: NotRequired[
        "aws_sdk_elastic_beanstalk.types.application_resource_lifecycle_config.ApplicationResourceLifecycleConfig"
    ]
    """<p>The lifecycle configuration.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ApplicationResourceLifecycleDescriptionMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "application_name" in value:
        pairs.append((f"{prefix}.ApplicationName", str(value["application_name"])))
    if "resource_lifecycle_config" in value:
        import aws_sdk_elastic_beanstalk.types.application_resource_lifecycle_config

        aws_sdk_elastic_beanstalk.types.application_resource_lifecycle_config.serialize_query(
            value["resource_lifecycle_config"],
            pairs,
            f"{prefix}.ResourceLifecycleConfig",
        )


def deserialize_query(el: Element) -> ApplicationResourceLifecycleDescriptionMessage:
    out: ApplicationResourceLifecycleDescriptionMessage = {}  # type: ignore[typeddict-item]
    child_application_name = el.find("ApplicationName")
    if child_application_name is not None:
        out["application_name"] = str(child_application_name.text or "")
    child_resource_lifecycle_config = el.find("ResourceLifecycleConfig")
    if child_resource_lifecycle_config is not None:
        import aws_sdk_elastic_beanstalk.types.application_resource_lifecycle_config

        out["resource_lifecycle_config"] = (
            aws_sdk_elastic_beanstalk.types.application_resource_lifecycle_config.deserialize_query(
                child_resource_lifecycle_config
            )
        )
    return out
