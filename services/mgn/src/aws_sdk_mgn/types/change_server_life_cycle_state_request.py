"""Generated from Smithy shape ``com.amazonaws.mgn#ChangeServerLifeCycleStateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.account_id
    import aws_sdk_mgn.types.change_server_life_cycle_state_source_server_lifecycle
    import aws_sdk_mgn.types.source_server_id


class ChangeServerLifeCycleStateRequest(TypedDict, closed=True):
    source_server_id: "aws_sdk_mgn.types.source_server_id.SourceServerID"
    """<p>The request to change the source server migration lifecycle state by source server ID.</p>"""
    life_cycle: "aws_sdk_mgn.types.change_server_life_cycle_state_source_server_lifecycle.ChangeServerLifeCycleStateSourceServerLifecycle"
    """<p>The request to change the source server migration lifecycle state.</p>"""
    account_id: NotRequired["aws_sdk_mgn.types.account_id.AccountID"]
    """<p>The request to change the source server migration account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChangeServerLifeCycleStateRequest) -> dict:
    out: dict = {}
    out["sourceServerID"] = value["source_server_id"]
    import aws_sdk_mgn.types.change_server_life_cycle_state_source_server_lifecycle

    out["lifeCycle"] = (
        aws_sdk_mgn.types.change_server_life_cycle_state_source_server_lifecycle.serialize_json(
            value["life_cycle"]
        )
    )
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> ChangeServerLifeCycleStateRequest:
    out: ChangeServerLifeCycleStateRequest = {}  # type: ignore[typeddict-item]
    if "sourceServerID" in data:
        out["source_server_id"] = data["sourceServerID"]
    else:
        raise DeserializationError(
            "ChangeServerLifeCycleStateRequest.source_server_id required"
        )
    if "lifeCycle" in data:
        import aws_sdk_mgn.types.change_server_life_cycle_state_source_server_lifecycle

        out["life_cycle"] = (
            aws_sdk_mgn.types.change_server_life_cycle_state_source_server_lifecycle.deserialize_json(
                data["lifeCycle"]
            )
        )
    else:
        raise DeserializationError(
            "ChangeServerLifeCycleStateRequest.life_cycle required"
        )
    if "accountID" in data:
        out["account_id"] = data["accountID"]
    return out
