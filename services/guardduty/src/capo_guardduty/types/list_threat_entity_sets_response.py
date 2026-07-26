"""Generated from Smithy shape ``com.amazonaws.guardduty#ListThreatEntitySetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string
    import capo_guardduty.types.threat_entity_set_ids


class ListThreatEntitySetsResponse(TypedDict, closed=True):
    threat_entity_set_ids: NotRequired[
        "capo_guardduty.types.threat_entity_set_ids.ThreatEntitySetIds"
    ]
    """<p>The IDs of the threat entity set resources.</p>"""
    next_token: NotRequired["capo_guardduty.types.string.String"]
    """<p>The pagination parameter to be used on the next list operation to retrieve more items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListThreatEntitySetsResponse) -> dict:
    out: dict = {}
    if "threat_entity_set_ids" in value:
        import capo_guardduty.types.threat_entity_set_ids

        out["threatEntitySetIds"] = (
            capo_guardduty.types.threat_entity_set_ids.serialize_json(
                value["threat_entity_set_ids"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListThreatEntitySetsResponse:
    out: ListThreatEntitySetsResponse = {}  # type: ignore[typeddict-item]
    if "threatEntitySetIds" in data:
        import capo_guardduty.types.threat_entity_set_ids

        out["threat_entity_set_ids"] = (
            capo_guardduty.types.threat_entity_set_ids.deserialize_json(
                data["threatEntitySetIds"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
