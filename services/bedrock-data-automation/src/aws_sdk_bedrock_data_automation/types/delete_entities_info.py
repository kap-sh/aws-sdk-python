"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DeleteEntitiesInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.entity_id_list


class DeleteEntitiesInfo(TypedDict, closed=True):
    entity_ids: "aws_sdk_bedrock_data_automation.types.entity_id_list.EntityIdList"


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEntitiesInfo) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_data_automation.types.entity_id_list

    out["entityIds"] = (
        aws_sdk_bedrock_data_automation.types.entity_id_list.serialize_json(
            value["entity_ids"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteEntitiesInfo:
    out: DeleteEntitiesInfo = {}  # type: ignore[typeddict-item]
    if "entityIds" in data:
        import aws_sdk_bedrock_data_automation.types.entity_id_list

        out["entity_ids"] = (
            aws_sdk_bedrock_data_automation.types.entity_id_list.deserialize_json(
                data["entityIds"]
            )
        )
    else:
        raise DeserializationError("DeleteEntitiesInfo.entity_ids required")
    return out
