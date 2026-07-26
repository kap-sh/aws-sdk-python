"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#OptionStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.boolean
    import capo_elasticsearch_service.types.option_state
    import capo_elasticsearch_service.types.u_int_value
    import capo_elasticsearch_service.types.update_timestamp


class OptionStatus(TypedDict, closed=True):
    creation_date: "capo_elasticsearch_service.types.update_timestamp.UpdateTimestamp"
    """<p>Timestamp which tells the creation date for the entity.</p>"""
    update_date: "capo_elasticsearch_service.types.update_timestamp.UpdateTimestamp"
    """<p>Timestamp which tells the last updated time for the entity.</p>"""
    update_version: "capo_elasticsearch_service.types.u_int_value.UIntValue"
    """<p>Specifies the latest version for the entity.</p>"""
    state: "capo_elasticsearch_service.types.option_state.OptionState"
    """<p>Provides the <code>OptionState</code> for the Elasticsearch domain.</p>"""
    pending_deletion: NotRequired["capo_elasticsearch_service.types.boolean.Boolean"]
    """<p>Indicates whether the Elasticsearch domain is being deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OptionStatus) -> dict:
    out: dict = {}
    import capo_elasticsearch_service.types.update_timestamp

    out["CreationDate"] = (
        capo_elasticsearch_service.types.update_timestamp.serialize_json(
            value["creation_date"]
        )
    )
    import capo_elasticsearch_service.types.update_timestamp

    out["UpdateDate"] = (
        capo_elasticsearch_service.types.update_timestamp.serialize_json(
            value["update_date"]
        )
    )
    out["UpdateVersion"] = value.get("update_version", 0)
    import capo_elasticsearch_service.types.option_state

    out["State"] = capo_elasticsearch_service.types.option_state.serialize_json(
        value["state"]
    )
    if "pending_deletion" in value:
        out["PendingDeletion"] = value["pending_deletion"]
    return out


def deserialize_json(data: dict) -> OptionStatus:
    out: OptionStatus = {}  # type: ignore[typeddict-item]
    if "CreationDate" in data:
        import capo_elasticsearch_service.types.update_timestamp

        out["creation_date"] = (
            capo_elasticsearch_service.types.update_timestamp.deserialize_json(
                data["CreationDate"]
            )
        )
    else:
        raise DeserializationError("OptionStatus.creation_date required")
    if "UpdateDate" in data:
        import capo_elasticsearch_service.types.update_timestamp

        out["update_date"] = (
            capo_elasticsearch_service.types.update_timestamp.deserialize_json(
                data["UpdateDate"]
            )
        )
    else:
        raise DeserializationError("OptionStatus.update_date required")
    if "UpdateVersion" in data:
        out["update_version"] = data["UpdateVersion"]
    else:
        out["update_version"] = 0
    if "State" in data:
        import capo_elasticsearch_service.types.option_state

        out["state"] = capo_elasticsearch_service.types.option_state.deserialize_json(
            data["State"]
        )
    else:
        raise DeserializationError("OptionStatus.state required")
    if "PendingDeletion" in data:
        out["pending_deletion"] = data["PendingDeletion"]
    return out
