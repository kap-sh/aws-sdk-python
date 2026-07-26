"""Generated from Smithy shape ``com.amazonaws.rtbfabric#Action``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_rtbfabric.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_rtbfabric.types.header_tag_action
    import capo_rtbfabric.types.no_bid_action


class _Action_noBid(TypedDict, closed=True):
    noBid: "capo_rtbfabric.types.no_bid_action.NoBidAction"


class _Action_headerTag(TypedDict, closed=True):
    headerTag: "capo_rtbfabric.types.header_tag_action.HeaderTagAction"


Action: TypeAlias = _Action_noBid | _Action_headerTag


# --- restJson1 ser/de ---
def serialize_json(value: Action) -> dict:
    if "noBid" in value:
        import capo_rtbfabric.types.no_bid_action

        return {
            "noBid": capo_rtbfabric.types.no_bid_action.serialize_json(value["noBid"])
        }
    elif "headerTag" in value:
        import capo_rtbfabric.types.header_tag_action

        return {
            "headerTag": capo_rtbfabric.types.header_tag_action.serialize_json(
                value["headerTag"]
            )
        }
    else:
        raise SerializationError("Action: no variant present")


def deserialize_json(data: dict) -> Action:
    if "noBid" in data:
        import capo_rtbfabric.types.no_bid_action

        return {
            "noBid": capo_rtbfabric.types.no_bid_action.deserialize_json(data["noBid"])
        }
    elif "headerTag" in data:
        import capo_rtbfabric.types.header_tag_action

        return {
            "headerTag": capo_rtbfabric.types.header_tag_action.deserialize_json(
                data["headerTag"]
            )
        }
    else:
        raise DeserializationError("Action: no recognized variant key")
