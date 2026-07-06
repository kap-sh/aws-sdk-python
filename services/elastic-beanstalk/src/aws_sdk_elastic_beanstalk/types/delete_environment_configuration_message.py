"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#DeleteEnvironmentConfigurationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_elastic_beanstalk._protocol.xml import Element
from aws_sdk_elastic_beanstalk.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.application_name
    import aws_sdk_elastic_beanstalk.types.environment_name


class DeleteEnvironmentConfigurationMessage(TypedDict, closed=True):
    application_name: "aws_sdk_elastic_beanstalk.types.application_name.ApplicationName"
    """<p>The name of the application the environment is associated with.</p>"""
    environment_name: "aws_sdk_elastic_beanstalk.types.environment_name.EnvironmentName"
    """<p>The name of the environment to delete the draft configuration from.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteEnvironmentConfigurationMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((f"{prefix}.ApplicationName", str(value["application_name"])))
    pairs.append((f"{prefix}.EnvironmentName", str(value["environment_name"])))


def deserialize_query(el: Element) -> DeleteEnvironmentConfigurationMessage:
    out: DeleteEnvironmentConfigurationMessage = {}  # type: ignore[typeddict-item]
    child_application_name = el.find("ApplicationName")
    if child_application_name is not None:
        out["application_name"] = str(child_application_name.text or "")
    else:
        raise DeserializationError(
            "DeleteEnvironmentConfigurationMessage.application_name required"
        )
    child_environment_name = el.find("EnvironmentName")
    if child_environment_name is not None:
        out["environment_name"] = str(child_environment_name.text or "")
    else:
        raise DeserializationError(
            "DeleteEnvironmentConfigurationMessage.environment_name required"
        )
    return out
