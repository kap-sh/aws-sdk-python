"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#UpdateApplicationResourceLifecycleMessage``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_elastic_beanstalk._protocol.xml import Element
from aws_sdk_elastic_beanstalk.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.application_name
    import aws_sdk_elastic_beanstalk.types.application_resource_lifecycle_config


class UpdateApplicationResourceLifecycleMessage(TypedDict):
    application_name: "aws_sdk_elastic_beanstalk.types.application_name.ApplicationName"
    """<p>The name of the application.</p>"""
    resource_lifecycle_config: "aws_sdk_elastic_beanstalk.types.application_resource_lifecycle_config.ApplicationResourceLifecycleConfig"
    """<p>The lifecycle configuration.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateApplicationResourceLifecycleMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((f"{prefix}.ApplicationName", str(value["application_name"])))
    import aws_sdk_elastic_beanstalk.types.application_resource_lifecycle_config

    aws_sdk_elastic_beanstalk.types.application_resource_lifecycle_config.serialize_query(
        value["resource_lifecycle_config"], pairs, f"{prefix}.ResourceLifecycleConfig"
    )


def deserialize_query(el: Element) -> UpdateApplicationResourceLifecycleMessage:
    out: UpdateApplicationResourceLifecycleMessage = {}  # type: ignore[typeddict-item]
    child_application_name = el.find("ApplicationName")
    if child_application_name is not None:
        out["application_name"] = str(child_application_name.text or "")
    else:
        raise DeserializationError(
            "UpdateApplicationResourceLifecycleMessage.application_name required"
        )
    child_resource_lifecycle_config = el.find("ResourceLifecycleConfig")
    if child_resource_lifecycle_config is not None:
        import aws_sdk_elastic_beanstalk.types.application_resource_lifecycle_config

        out["resource_lifecycle_config"] = (
            aws_sdk_elastic_beanstalk.types.application_resource_lifecycle_config.deserialize_query(
                child_resource_lifecycle_config
            )
        )
    else:
        raise DeserializationError(
            "UpdateApplicationResourceLifecycleMessage.resource_lifecycle_config required"
        )
    return out
