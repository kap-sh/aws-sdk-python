"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#DeleteConfigurationTemplateMessage``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_elastic_beanstalk._protocol.xml import Element
from aws_sdk_elastic_beanstalk.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.application_name
    import aws_sdk_elastic_beanstalk.types.configuration_template_name


class DeleteConfigurationTemplateMessage(TypedDict):
    application_name: "aws_sdk_elastic_beanstalk.types.application_name.ApplicationName"
    """<p>The name of the application to delete the configuration template from.</p>"""
    template_name: "aws_sdk_elastic_beanstalk.types.configuration_template_name.ConfigurationTemplateName"
    """<p>The name of the configuration template to delete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteConfigurationTemplateMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.ApplicationName", str(value["application_name"])))
    pairs.append((f"{prefix}.TemplateName", str(value["template_name"])))


def deserialize_query(el: Element) -> DeleteConfigurationTemplateMessage:
    out: DeleteConfigurationTemplateMessage = {}  # type: ignore[typeddict-item]
    child_application_name = el.find("ApplicationName")
    if child_application_name is not None:
        out["application_name"] = str(child_application_name.text or "")
    else:
        raise DeserializationError(
            "DeleteConfigurationTemplateMessage.application_name required"
        )
    child_template_name = el.find("TemplateName")
    if child_template_name is not None:
        out["template_name"] = str(child_template_name.text or "")
    else:
        raise DeserializationError(
            "DeleteConfigurationTemplateMessage.template_name required"
        )
    return out
