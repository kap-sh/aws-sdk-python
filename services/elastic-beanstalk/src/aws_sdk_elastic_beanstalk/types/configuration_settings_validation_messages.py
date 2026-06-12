"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ConfigurationSettingsValidationMessages``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.validation_messages_list


class ConfigurationSettingsValidationMessages(TypedDict):
    messages: NotRequired[
        "aws_sdk_elastic_beanstalk.types.validation_messages_list.ValidationMessagesList"
    ]
    """<p> A list of <a>ValidationMessage</a>. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ConfigurationSettingsValidationMessages,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "messages" in value:
        import aws_sdk_elastic_beanstalk.types.validation_messages_list

        aws_sdk_elastic_beanstalk.types.validation_messages_list.serialize_query(
            value["messages"], pairs, f"{prefix}.Messages"
        )


def deserialize_query(el: Element) -> ConfigurationSettingsValidationMessages:
    out: ConfigurationSettingsValidationMessages = {}  # type: ignore[typeddict-item]
    child_messages = el.find("Messages")
    if child_messages is not None:
        import aws_sdk_elastic_beanstalk.types.validation_messages_list

        out["messages"] = (
            aws_sdk_elastic_beanstalk.types.validation_messages_list.deserialize_query(
                child_messages
            )
        )
    return out
