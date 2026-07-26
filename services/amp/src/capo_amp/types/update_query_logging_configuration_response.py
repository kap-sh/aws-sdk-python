"""Generated from Smithy shape ``com.amazonaws.amp#UpdateQueryLoggingConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_amp.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amp.types.query_logging_configuration_status


class UpdateQueryLoggingConfigurationResponse(TypedDict, closed=True):
    status: "capo_amp.types.query_logging_configuration_status.QueryLoggingConfigurationStatus"
    """<p>The current status of the query logging configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQueryLoggingConfigurationResponse) -> dict:
    out: dict = {}
    import capo_amp.types.query_logging_configuration_status

    out["status"] = capo_amp.types.query_logging_configuration_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> UpdateQueryLoggingConfigurationResponse:
    out: UpdateQueryLoggingConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import capo_amp.types.query_logging_configuration_status

        out["status"] = (
            capo_amp.types.query_logging_configuration_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateQueryLoggingConfigurationResponse.status required"
        )
    return out
