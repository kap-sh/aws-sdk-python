"""Generated from Smithy shape ``com.amazonaws.appfabric#AuditLogDestinationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_appfabric.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appfabric.types.destination


class AuditLogDestinationConfiguration(TypedDict, closed=True):
    destination: "capo_appfabric.types.destination.Destination"
    """<p>Contains information about an audit log destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuditLogDestinationConfiguration) -> dict:
    out: dict = {}
    import capo_appfabric.types.destination

    out["destination"] = capo_appfabric.types.destination.serialize_json(
        value["destination"]
    )
    return out


def deserialize_json(data: dict) -> AuditLogDestinationConfiguration:
    out: AuditLogDestinationConfiguration = {}  # type: ignore[typeddict-item]
    if "destination" in data:
        import capo_appfabric.types.destination

        out["destination"] = capo_appfabric.types.destination.deserialize_json(
            data["destination"]
        )
    else:
        raise DeserializationError(
            "AuditLogDestinationConfiguration.destination required"
        )
    return out
