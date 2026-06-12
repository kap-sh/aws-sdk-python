"""Generated from Smithy shape ``com.amazonaws.ivschat#DeleteLoggingConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ivschat.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivschat.types.logging_configuration_identifier


class DeleteLoggingConfigurationRequest(TypedDict):
    identifier: "aws_sdk_ivschat.types.logging_configuration_identifier.LoggingConfigurationIdentifier"
    """<p>Identifier of the logging configuration to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLoggingConfigurationRequest) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    return out


def deserialize_json(data: dict) -> DeleteLoggingConfigurationRequest:
    out: DeleteLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError(
            "DeleteLoggingConfigurationRequest.identifier required"
        )
    return out
