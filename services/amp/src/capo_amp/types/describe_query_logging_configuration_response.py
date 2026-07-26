"""Generated from Smithy shape ``com.amazonaws.amp#DescribeQueryLoggingConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_amp.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amp.types.query_logging_configuration_metadata


class DescribeQueryLoggingConfigurationResponse(TypedDict, closed=True):
    query_logging_configuration: "capo_amp.types.query_logging_configuration_metadata.QueryLoggingConfigurationMetadata"
    """<p>The detailed information about the query logging configuration for the specified workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeQueryLoggingConfigurationResponse) -> dict:
    out: dict = {}
    import capo_amp.types.query_logging_configuration_metadata

    out["queryLoggingConfiguration"] = (
        capo_amp.types.query_logging_configuration_metadata.serialize_json(
            value["query_logging_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> DescribeQueryLoggingConfigurationResponse:
    out: DescribeQueryLoggingConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "queryLoggingConfiguration" in data:
        import capo_amp.types.query_logging_configuration_metadata

        out["query_logging_configuration"] = (
            capo_amp.types.query_logging_configuration_metadata.deserialize_json(
                data["queryLoggingConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeQueryLoggingConfigurationResponse.query_logging_configuration required"
        )
    return out
