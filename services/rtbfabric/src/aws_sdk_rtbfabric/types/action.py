"""Generated from Smithy shape ``com.amazonaws.rtbfabric#Action``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_rtbfabric.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.header_tag_action
    import aws_sdk_rtbfabric.types.no_bid_action


class _Action_noBid(TypedDict):
    noBid: "aws_sdk_rtbfabric.types.no_bid_action.NoBidAction"


class _Action_headerTag(TypedDict):
    headerTag: "aws_sdk_rtbfabric.types.header_tag_action.HeaderTagAction"


Action: TypeAlias = _Action_noBid | _Action_headerTag


# --- restJson1 ser/de ---
def serialize_json(value: Action) -> dict:
    if "noBid" in value:
        import aws_sdk_rtbfabric.types.no_bid_action

        return {
            "noBid": aws_sdk_rtbfabric.types.no_bid_action.serialize_json(
                value["noBid"]
            )
        }
    elif "headerTag" in value:
        import aws_sdk_rtbfabric.types.header_tag_action

        return {
            "headerTag": aws_sdk_rtbfabric.types.header_tag_action.serialize_json(
                value["headerTag"]
            )
        }
    else:
        raise SerializationError("Action: no variant present")


def deserialize_json(data: dict) -> Action:
    if "noBid" in data:
        import aws_sdk_rtbfabric.types.no_bid_action

        return {
            "noBid": aws_sdk_rtbfabric.types.no_bid_action.deserialize_json(
                data["noBid"]
            )
        }
    elif "headerTag" in data:
        import aws_sdk_rtbfabric.types.header_tag_action

        return {
            "headerTag": aws_sdk_rtbfabric.types.header_tag_action.deserialize_json(
                data["headerTag"]
            )
        }
    else:
        raise DeserializationError("Action: no recognized variant key")
