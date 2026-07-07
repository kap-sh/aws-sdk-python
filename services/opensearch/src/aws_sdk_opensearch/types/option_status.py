"""Generated from Smithy shape ``com.amazonaws.opensearch#OptionStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.boolean
    import aws_sdk_opensearch.types.option_state
    import aws_sdk_opensearch.types.u_int_value
    import aws_sdk_opensearch.types.update_timestamp


class OptionStatus(TypedDict, closed=True):
    creation_date: "aws_sdk_opensearch.types.update_timestamp.UpdateTimestamp"
    """<p>The timestamp when the entity was created.</p>"""
    update_date: "aws_sdk_opensearch.types.update_timestamp.UpdateTimestamp"
    """<p>The timestamp of the last time the entity was updated.</p>"""
    update_version: "aws_sdk_opensearch.types.u_int_value.UIntValue"
    """<p>The latest version of the entity.</p>"""
    state: "aws_sdk_opensearch.types.option_state.OptionState"
    """<p>The state of the entity.</p>"""
    pending_deletion: NotRequired["aws_sdk_opensearch.types.boolean.Boolean"]
    """<p>Indicates whether the entity is being deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OptionStatus) -> dict:
    out: dict = {}
    import aws_sdk_opensearch.types.update_timestamp

    out["CreationDate"] = aws_sdk_opensearch.types.update_timestamp.serialize_json(
        value["creation_date"]
    )
    import aws_sdk_opensearch.types.update_timestamp

    out["UpdateDate"] = aws_sdk_opensearch.types.update_timestamp.serialize_json(
        value["update_date"]
    )
    out["UpdateVersion"] = value.get("update_version", 0)
    import aws_sdk_opensearch.types.option_state

    out["State"] = aws_sdk_opensearch.types.option_state.serialize_json(value["state"])
    if "pending_deletion" in value:
        out["PendingDeletion"] = value["pending_deletion"]
    return out


def deserialize_json(data: dict) -> OptionStatus:
    out: OptionStatus = {}  # type: ignore[typeddict-item]
    if "CreationDate" in data:
        import aws_sdk_opensearch.types.update_timestamp

        out["creation_date"] = (
            aws_sdk_opensearch.types.update_timestamp.deserialize_json(
                data["CreationDate"]
            )
        )
    else:
        raise DeserializationError("OptionStatus.creation_date required")
    if "UpdateDate" in data:
        import aws_sdk_opensearch.types.update_timestamp

        out["update_date"] = aws_sdk_opensearch.types.update_timestamp.deserialize_json(
            data["UpdateDate"]
        )
    else:
        raise DeserializationError("OptionStatus.update_date required")
    if "UpdateVersion" in data:
        out["update_version"] = data["UpdateVersion"]
    else:
        out["update_version"] = 0
    if "State" in data:
        import aws_sdk_opensearch.types.option_state

        out["state"] = aws_sdk_opensearch.types.option_state.deserialize_json(
            data["State"]
        )
    else:
        raise DeserializationError("OptionStatus.state required")
    if "PendingDeletion" in data:
        out["pending_deletion"] = data["PendingDeletion"]
    return out
