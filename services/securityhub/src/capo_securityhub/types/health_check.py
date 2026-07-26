"""Generated from Smithy shape ``com.amazonaws.securityhub#HealthCheck``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.connector_status
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.timestamp


class HealthCheck(TypedDict, closed=True):
    connector_status: NotRequired[
        "capo_securityhub.types.connector_status.ConnectorStatus"
    ]
    """<p>The status of the connectorV2.</p>"""
    message: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The message for the reason of connectorStatus change.</p>"""
    last_checked_at: NotRequired["capo_securityhub.types.timestamp.Timestamp"]
    """<p>ISO 8601 UTC timestamp for the time check the health status of the connectorV2.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HealthCheck) -> dict:
    out: dict = {}
    if "connector_status" in value:
        import capo_securityhub.types.connector_status

        out["ConnectorStatus"] = capo_securityhub.types.connector_status.serialize_json(
            value["connector_status"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "last_checked_at" in value:
        import capo_securityhub.types.timestamp

        out["LastCheckedAt"] = capo_securityhub.types.timestamp.serialize_json(
            value["last_checked_at"]
        )
    return out


def deserialize_json(data: dict) -> HealthCheck:
    out: HealthCheck = {}  # type: ignore[typeddict-item]
    if "ConnectorStatus" in data:
        import capo_securityhub.types.connector_status

        out["connector_status"] = (
            capo_securityhub.types.connector_status.deserialize_json(
                data["ConnectorStatus"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "LastCheckedAt" in data:
        import capo_securityhub.types.timestamp

        out["last_checked_at"] = capo_securityhub.types.timestamp.deserialize_json(
            data["LastCheckedAt"]
        )
    return out
