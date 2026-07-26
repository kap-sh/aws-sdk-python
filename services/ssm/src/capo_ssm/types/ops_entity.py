"""Generated from Smithy shape ``com.amazonaws.ssm#OpsEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.ops_entity_id
    import capo_ssm.types.ops_entity_item_map


class OpsEntity(TypedDict, closed=True):
    id: NotRequired["capo_ssm.types.ops_entity_id.OpsEntityId"]
    """<p>The query ID.</p>"""
    data: NotRequired["capo_ssm.types.ops_entity_item_map.OpsEntityItemMap"]
    """<p>The data returned by the query.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsEntity) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "data" in value:
        import capo_ssm.types.ops_entity_item_map

        out["Data"] = capo_ssm.types.ops_entity_item_map.serialize_aws_json_1_1(
            value["data"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsEntity:
    out: OpsEntity = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Data" in data:
        import capo_ssm.types.ops_entity_item_map

        out["data"] = capo_ssm.types.ops_entity_item_map.deserialize_aws_json_1_1(
            data["Data"]
        )
    return out
