"""Generated from Smithy shape ``com.amazonaws.ssm#OpsEntityItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.ops_entity_item_capture_time
    import aws_sdk_ssm.types.ops_entity_item_entry_list


class OpsEntityItem(TypedDict):
    capture_time: NotRequired[
        "aws_sdk_ssm.types.ops_entity_item_capture_time.OpsEntityItemCaptureTime"
    ]
    """<p>The time the OpsData was captured.</p>"""
    content: NotRequired[
        "aws_sdk_ssm.types.ops_entity_item_entry_list.OpsEntityItemEntryList"
    ]
    """<p>The details of an OpsData summary.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OpsEntityItem) -> dict:
    out: dict = {}
    if "capture_time" in value:
        out["CaptureTime"] = value["capture_time"]
    if "content" in value:
        import aws_sdk_ssm.types.ops_entity_item_entry_list

        out["Content"] = (
            aws_sdk_ssm.types.ops_entity_item_entry_list.serialize_aws_json_1_1(
                value["content"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OpsEntityItem:
    out: OpsEntityItem = {}  # type: ignore[typeddict-item]
    if "CaptureTime" in data:
        out["capture_time"] = data["CaptureTime"]
    if "Content" in data:
        import aws_sdk_ssm.types.ops_entity_item_entry_list

        out["content"] = (
            aws_sdk_ssm.types.ops_entity_item_entry_list.deserialize_aws_json_1_1(
                data["Content"]
            )
        )
    return out
