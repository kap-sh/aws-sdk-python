"""Generated from Smithy shape ``com.amazonaws.datazone#ActionParameters``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_datazone.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.aws_console_link_parameters


class _ActionParameters_awsConsoleLink(TypedDict, closed=True):
    awsConsoleLink: (
        "aws_sdk_datazone.types.aws_console_link_parameters.AwsConsoleLinkParameters"
    )


ActionParameters: TypeAlias = _ActionParameters_awsConsoleLink


# --- restJson1 ser/de ---
def serialize_json(value: ActionParameters) -> dict:
    if "awsConsoleLink" in value:
        import aws_sdk_datazone.types.aws_console_link_parameters

        return {
            "awsConsoleLink": aws_sdk_datazone.types.aws_console_link_parameters.serialize_json(
                value["awsConsoleLink"]
            )
        }
    else:
        raise SerializationError("ActionParameters: no variant present")


def deserialize_json(data: dict) -> ActionParameters:
    if "awsConsoleLink" in data:
        import aws_sdk_datazone.types.aws_console_link_parameters

        return {
            "awsConsoleLink": aws_sdk_datazone.types.aws_console_link_parameters.deserialize_json(
                data["awsConsoleLink"]
            )
        }
    else:
        raise DeserializationError("ActionParameters: no recognized variant key")
