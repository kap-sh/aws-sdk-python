"""Generated from Smithy shape ``com.amazonaws.ssm#OpsEntityItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.ops_entity_item_capture_time
    import capo_ssm.types.ops_entity_item_entry_list


class OpsEntityItem(TypedDict, closed=True):
    capture_time: NotRequired[
        "capo_ssm.types.ops_entity_item_capture_time.OpsEntityItemCaptureTime"
    ]
    """<p>The time the OpsData was captured.</p>"""
    content: NotRequired[
        "capo_ssm.types.ops_entity_item_entry_list.OpsEntityItemEntryList"
    ]
    """<p>The details of an OpsData summary.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsEntityItem) -> dict:
    out: dict = {}
    if "capture_time" in value:
        out["CaptureTime"] = value["capture_time"]
    if "content" in value:
        import capo_ssm.types.ops_entity_item_entry_list

        out["Content"] = (
            capo_ssm.types.ops_entity_item_entry_list.serialize_aws_json_1_1(
                value["content"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsEntityItem:
    out: OpsEntityItem = {}  # type: ignore[typeddict-item]
    if data.get("CaptureTime") is not None:
        out["capture_time"] = data["CaptureTime"]
    if data.get("Content") is not None:
        import capo_ssm.types.ops_entity_item_entry_list

        out["content"] = (
            capo_ssm.types.ops_entity_item_entry_list.deserialize_aws_json_1_1(
                data["Content"]
            )
        )
    return out
