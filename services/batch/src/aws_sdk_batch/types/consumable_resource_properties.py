"""Generated from Smithy shape ``com.amazonaws.batch#ConsumableResourceProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.consumable_resource_list


class ConsumableResourceProperties(TypedDict):
    consumable_resource_list: NotRequired[
        "aws_sdk_batch.types.consumable_resource_list.ConsumableResourceList"
    ]
    """<p>The list of consumable resources required by a job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConsumableResourceProperties) -> dict:
    out: dict = {}
    if "consumable_resource_list" in value:
        import aws_sdk_batch.types.consumable_resource_list

        out["consumableResourceList"] = (
            aws_sdk_batch.types.consumable_resource_list.serialize_json(
                value["consumable_resource_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConsumableResourceProperties:
    out: ConsumableResourceProperties = {}  # type: ignore[typeddict-item]
    if "consumableResourceList" in data:
        import aws_sdk_batch.types.consumable_resource_list

        out["consumable_resource_list"] = (
            aws_sdk_batch.types.consumable_resource_list.deserialize_json(
                data["consumableResourceList"]
            )
        )
    return out
