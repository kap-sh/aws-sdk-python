"""Generated from Smithy shape ``com.amazonaws.opensearch#InsightEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearch.types.insight_entity_type
    import capo_opensearch.types.insight_entity_value


class InsightEntity(TypedDict, closed=True):
    type: "capo_opensearch.types.insight_entity_type.InsightEntityType"
    """<p>The type of the entity. Possible values are <code>Account</code> and <code>DomainName</code>.</p>"""
    value: NotRequired["capo_opensearch.types.insight_entity_value.InsightEntityValue"]
    """<p>The value of the entity. For <code>DomainName</code>, this is the domain name. For <code>Account</code>, this is the Amazon Web Services account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsightEntity) -> dict:
    out: dict = {}
    import capo_opensearch.types.insight_entity_type

    out["Type"] = capo_opensearch.types.insight_entity_type.serialize_json(
        value["type"]
    )
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> InsightEntity:
    out: InsightEntity = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_opensearch.types.insight_entity_type

        out["type"] = capo_opensearch.types.insight_entity_type.deserialize_json(
            data["Type"]
        )
    else:
        raise DeserializationError("InsightEntity.type required")
    if "Value" in data:
        out["value"] = data["Value"]
    return out
