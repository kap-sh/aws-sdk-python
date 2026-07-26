"""Generated from Smithy shape ``com.amazonaws.schemas#DiscovererSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_schemas.types.__boolean
    import capo_schemas.types.__string
    import capo_schemas.types.discoverer_state
    import capo_schemas.types.tags


class DiscovererSummary(TypedDict, closed=True):
    discoverer_arn: NotRequired["capo_schemas.types.__string.__string"]
    """<p>The ARN of the discoverer.</p>"""
    discoverer_id: NotRequired["capo_schemas.types.__string.__string"]
    """<p>The ID of the discoverer.</p>"""
    source_arn: NotRequired["capo_schemas.types.__string.__string"]
    """<p>The ARN of the event bus.</p>"""
    state: NotRequired["capo_schemas.types.discoverer_state.DiscovererState"]
    """<p>The state of the discoverer.</p>"""
    cross_account: NotRequired["capo_schemas.types.__boolean.__boolean"]
    """<p>The Status if the discoverer will discover schemas from events sent from another account.</p>"""
    tags: NotRequired["capo_schemas.types.tags.Tags"]
    """<p>Tags associated with the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DiscovererSummary) -> dict:
    out: dict = {}
    if "discoverer_arn" in value:
        out["DiscovererArn"] = value["discoverer_arn"]
    if "discoverer_id" in value:
        out["DiscovererId"] = value["discoverer_id"]
    if "source_arn" in value:
        out["SourceArn"] = value["source_arn"]
    if "state" in value:
        import capo_schemas.types.discoverer_state

        out["State"] = capo_schemas.types.discoverer_state.serialize_json(
            value["state"]
        )
    if "cross_account" in value:
        out["CrossAccount"] = value["cross_account"]
    if "tags" in value:
        import capo_schemas.types.tags

        out["tags"] = capo_schemas.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> DiscovererSummary:
    out: DiscovererSummary = {}  # type: ignore[typeddict-item]
    if "DiscovererArn" in data:
        out["discoverer_arn"] = data["DiscovererArn"]
    if "DiscovererId" in data:
        out["discoverer_id"] = data["DiscovererId"]
    if "SourceArn" in data:
        out["source_arn"] = data["SourceArn"]
    if "State" in data:
        import capo_schemas.types.discoverer_state

        out["state"] = capo_schemas.types.discoverer_state.deserialize_json(
            data["State"]
        )
    if "CrossAccount" in data:
        out["cross_account"] = data["CrossAccount"]
    if "tags" in data:
        import capo_schemas.types.tags

        out["tags"] = capo_schemas.types.tags.deserialize_json(data["tags"])
    return out
