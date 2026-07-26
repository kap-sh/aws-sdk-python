"""Generated from Smithy shape ``com.amazonaws.iot#ListMitigationActionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.mitigation_action_identifier_list
    import capo_iot.types.next_token


class ListMitigationActionsResponse(TypedDict, closed=True):
    action_identifiers: NotRequired[
        "capo_iot.types.mitigation_action_identifier_list.MitigationActionIdentifierList"
    ]
    """<p>A set of actions that matched the specified filter criteria.</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>The token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMitigationActionsResponse) -> dict:
    out: dict = {}
    if "action_identifiers" in value:
        import capo_iot.types.mitigation_action_identifier_list

        out["actionIdentifiers"] = (
            capo_iot.types.mitigation_action_identifier_list.serialize_json(
                value["action_identifiers"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMitigationActionsResponse:
    out: ListMitigationActionsResponse = {}  # type: ignore[typeddict-item]
    if "actionIdentifiers" in data:
        import capo_iot.types.mitigation_action_identifier_list

        out["action_identifiers"] = (
            capo_iot.types.mitigation_action_identifier_list.deserialize_json(
                data["actionIdentifiers"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
