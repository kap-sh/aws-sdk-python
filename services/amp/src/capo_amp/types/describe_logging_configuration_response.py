"""Generated from Smithy shape ``com.amazonaws.amp#DescribeLoggingConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_amp.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amp.types.logging_configuration_metadata


class DescribeLoggingConfigurationResponse(TypedDict, closed=True):
    logging_configuration: (
        "capo_amp.types.logging_configuration_metadata.LoggingConfigurationMetadata"
    )
    """<p>A structure that displays the information about the logging configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeLoggingConfigurationResponse) -> dict:
    out: dict = {}
    import capo_amp.types.logging_configuration_metadata

    out["loggingConfiguration"] = (
        capo_amp.types.logging_configuration_metadata.serialize_json(
            value["logging_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> DescribeLoggingConfigurationResponse:
    out: DescribeLoggingConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "loggingConfiguration" in data:
        import capo_amp.types.logging_configuration_metadata

        out["logging_configuration"] = (
            capo_amp.types.logging_configuration_metadata.deserialize_json(
                data["loggingConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeLoggingConfigurationResponse.logging_configuration required"
        )
    return out
