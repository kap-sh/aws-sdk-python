"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ValidationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.configuration_option_name
    import aws_sdk_elastic_beanstalk.types.option_namespace
    import aws_sdk_elastic_beanstalk.types.validation_message_string
    import aws_sdk_elastic_beanstalk.types.validation_severity


class ValidationMessage(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_elastic_beanstalk.types.validation_message_string.ValidationMessageString"
    ]
    """<p>A message describing the error or warning.</p>"""
    severity: NotRequired[
        "aws_sdk_elastic_beanstalk.types.validation_severity.ValidationSeverity"
    ]
    """<p>An indication of the severity of this message:</p> <ul> <li> <p> <code>error</code>: This message indicates that this is not a valid setting for an option.</p> </li> <li> <p> <code>warning</code>: This message is providing information you should take into account.</p> </li> </ul>"""
    namespace: NotRequired[
        "aws_sdk_elastic_beanstalk.types.option_namespace.OptionNamespace"
    ]
    """<p>The namespace to which the option belongs.</p>"""
    option_name: NotRequired[
        "aws_sdk_elastic_beanstalk.types.configuration_option_name.ConfigurationOptionName"
    ]
    """<p>The name of the option.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ValidationMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))
    if "severity" in value:
        import aws_sdk_elastic_beanstalk.types.validation_severity

        aws_sdk_elastic_beanstalk.types.validation_severity.serialize_query(
            value["severity"], pairs, f"{prefix}.Severity"
        )
    if "namespace" in value:
        pairs.append((f"{prefix}.Namespace", str(value["namespace"])))
    if "option_name" in value:
        pairs.append((f"{prefix}.OptionName", str(value["option_name"])))


def deserialize_query(el: Element) -> ValidationMessage:
    out: ValidationMessage = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    child_severity = el.find("Severity")
    if child_severity is not None:
        import aws_sdk_elastic_beanstalk.types.validation_severity

        out["severity"] = (
            aws_sdk_elastic_beanstalk.types.validation_severity.deserialize_query(
                child_severity
            )
        )
    child_namespace = el.find("Namespace")
    if child_namespace is not None:
        out["namespace"] = str(child_namespace.text or "")
    child_option_name = el.find("OptionName")
    if child_option_name is not None:
        out["option_name"] = str(child_option_name.text or "")
    return out
