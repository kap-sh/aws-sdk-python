"""Generated from Smithy shape ``com.amazonaws.guardduty#ListTrustedEntitySetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string
    import capo_guardduty.types.trusted_entity_set_ids


class ListTrustedEntitySetsResponse(TypedDict, closed=True):
    trusted_entity_set_ids: NotRequired[
        "capo_guardduty.types.trusted_entity_set_ids.TrustedEntitySetIds"
    ]
    """<p>The IDs of the trusted entity set resources.</p>"""
    next_token: NotRequired["capo_guardduty.types.string.String"]
    """<p>The pagination parameter to be used on the next list operation to retrieve more items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTrustedEntitySetsResponse) -> dict:
    out: dict = {}
    if "trusted_entity_set_ids" in value:
        import capo_guardduty.types.trusted_entity_set_ids

        out["trustedEntitySetIds"] = (
            capo_guardduty.types.trusted_entity_set_ids.serialize_json(
                value["trusted_entity_set_ids"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTrustedEntitySetsResponse:
    out: ListTrustedEntitySetsResponse = {}  # type: ignore[typeddict-item]
    if "trustedEntitySetIds" in data:
        import capo_guardduty.types.trusted_entity_set_ids

        out["trusted_entity_set_ids"] = (
            capo_guardduty.types.trusted_entity_set_ids.deserialize_json(
                data["trustedEntitySetIds"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
