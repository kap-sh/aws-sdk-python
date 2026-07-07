"""Generated from Smithy shape ``com.amazonaws.ses#ConfigurationSetDoesNotExistException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ses.types.configuration_set_name
    import aws_sdk_ses.types.error_message


class ConfigurationSetDoesNotExistException_(TypedDict, closed=True):
    configuration_set_name: NotRequired[
        "aws_sdk_ses.types.configuration_set_name.ConfigurationSetName"
    ]
    """<p>Indicates that the configuration set does not exist.</p>"""
    message: NotRequired["aws_sdk_ses.types.error_message.ErrorMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ConfigurationSetDoesNotExistException_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "configuration_set_name" in value:
        pairs.append(
            (f"{prefix}.ConfigurationSetName", str(value["configuration_set_name"]))
        )
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> ConfigurationSetDoesNotExistException_:
    out: ConfigurationSetDoesNotExistException_ = {}  # type: ignore[typeddict-item]
    child_configuration_set_name = el.find("ConfigurationSetName")
    if child_configuration_set_name is not None:
        out["configuration_set_name"] = str(child_configuration_set_name.text or "")
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class ConfigurationSetDoesNotExistException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ses#ConfigurationSetDoesNotExistException``."""

    code: str | None = "ConfigurationSetDoesNotExistException"

    def __init__(self, data: ConfigurationSetDoesNotExistException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConfigurationSetDoesNotExistException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "ConfigurationSetDoesNotExistException":
        return cls(deserialize_query(el))
