"""Generated from Smithy shape ``com.amazonaws.ec2#ConversionTask``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.conversion_task_state
    import aws_sdk_ec2.types.import_instance_task_details
    import aws_sdk_ec2.types.import_volume_task_details
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list


class ConversionTask(TypedDict):
    conversion_task_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the conversion task.</p>"""
    expiration_time: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The time when the task expires. If the upload isn't complete before the expiration time, we automatically cancel the task.</p>"""
    import_instance: NotRequired[
        "aws_sdk_ec2.types.import_instance_task_details.ImportInstanceTaskDetails"
    ]
    """<p>If the task is for importing an instance, this contains information about the import instance task.</p>"""
    import_volume: NotRequired[
        "aws_sdk_ec2.types.import_volume_task_details.ImportVolumeTaskDetails"
    ]
    """<p>If the task is for importing a volume, this contains information about the import volume task.</p>"""
    state: NotRequired["aws_sdk_ec2.types.conversion_task_state.ConversionTaskState"]
    """<p>The state of the conversion task.</p>"""
    status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The status message related to the conversion task.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the task.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ConversionTask, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "conversion_task_id" in value:
        pairs.append((f"{prefix}.ConversionTaskId", str(value["conversion_task_id"])))
    if "expiration_time" in value:
        pairs.append((f"{prefix}.ExpirationTime", str(value["expiration_time"])))
    if "import_instance" in value:
        import aws_sdk_ec2.types.import_instance_task_details

        aws_sdk_ec2.types.import_instance_task_details.serialize_ec2_query(
            value["import_instance"], pairs, f"{prefix}.ImportInstance"
        )
    if "import_volume" in value:
        import aws_sdk_ec2.types.import_volume_task_details

        aws_sdk_ec2.types.import_volume_task_details.serialize_ec2_query(
            value["import_volume"], pairs, f"{prefix}.ImportVolume"
        )
    if "state" in value:
        import aws_sdk_ec2.types.conversion_task_state

        aws_sdk_ec2.types.conversion_task_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )
    if "status_message" in value:
        pairs.append((f"{prefix}.StatusMessage", str(value["status_message"])))
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )


def deserialize_ec2_query(el: Element) -> ConversionTask:
    out: ConversionTask = {}  # type: ignore[typeddict-item]
    child_conversion_task_id = el.find("ConversionTaskId")
    if child_conversion_task_id is not None:
        out["conversion_task_id"] = str(child_conversion_task_id.text or "")
    child_expiration_time = el.find("ExpirationTime")
    if child_expiration_time is not None:
        out["expiration_time"] = str(child_expiration_time.text or "")
    child_import_instance = el.find("ImportInstance")
    if child_import_instance is not None:
        import aws_sdk_ec2.types.import_instance_task_details

        out["import_instance"] = (
            aws_sdk_ec2.types.import_instance_task_details.deserialize_ec2_query(
                child_import_instance
            )
        )
    child_import_volume = el.find("ImportVolume")
    if child_import_volume is not None:
        import aws_sdk_ec2.types.import_volume_task_details

        out["import_volume"] = (
            aws_sdk_ec2.types.import_volume_task_details.deserialize_ec2_query(
                child_import_volume
            )
        )
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.conversion_task_state

        out["state"] = aws_sdk_ec2.types.conversion_task_state.deserialize_ec2_query(
            child_state
        )
    child_status_message = el.find("StatusMessage")
    if child_status_message is not None:
        out["status_message"] = str(child_status_message.text or "")
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    return out
