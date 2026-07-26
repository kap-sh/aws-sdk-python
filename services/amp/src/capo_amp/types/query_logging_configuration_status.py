"""Generated from Smithy shape ``com.amazonaws.amp#QueryLoggingConfigurationStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amp.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amp.types.query_logging_configuration_status_code


class QueryLoggingConfigurationStatus(TypedDict, closed=True):
    status_code: "capo_amp.types.query_logging_configuration_status_code.QueryLoggingConfigurationStatusCode"
    """<p>The current status of the query logging configuration.</p>"""
    status_reason: NotRequired["str"]
    """<p>If there is a failure, the reason for the failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryLoggingConfigurationStatus) -> dict:
    out: dict = {}
    out["statusCode"] = value["status_code"]
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_json(data: dict) -> QueryLoggingConfigurationStatus:
    out: QueryLoggingConfigurationStatus = {}  # type: ignore[typeddict-item]
    if "statusCode" in data:
        out["status_code"] = data["statusCode"]
    else:
        raise DeserializationError(
            "QueryLoggingConfigurationStatus.status_code required"
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    return out
