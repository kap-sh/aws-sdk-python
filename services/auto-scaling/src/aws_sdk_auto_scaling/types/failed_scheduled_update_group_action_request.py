"""Generated from Smithy shape ``com.amazonaws.autoscaling#FailedScheduledUpdateGroupActionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.xml_string
    import aws_sdk_auto_scaling.types.xml_string_max_len64
    import aws_sdk_auto_scaling.types.xml_string_max_len255


class FailedScheduledUpdateGroupActionRequest(TypedDict):
    scheduled_action_name: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the scheduled action.</p>"""
    error_code: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len64.XmlStringMaxLen64"
    ]
    """<p>The error code.</p>"""
    error_message: NotRequired["aws_sdk_auto_scaling.types.xml_string.XmlString"]
    """<p>The error message accompanying the error code.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: FailedScheduledUpdateGroupActionRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "scheduled_action_name" in value:
        pairs.append(
            (f"{prefix}.ScheduledActionName", str(value["scheduled_action_name"]))
        )
    if "error_code" in value:
        pairs.append((f"{prefix}.ErrorCode", str(value["error_code"])))
    if "error_message" in value:
        pairs.append((f"{prefix}.ErrorMessage", str(value["error_message"])))


def deserialize_query(el: Element) -> FailedScheduledUpdateGroupActionRequest:
    out: FailedScheduledUpdateGroupActionRequest = {}  # type: ignore[typeddict-item]
    child_scheduled_action_name = el.find("ScheduledActionName")
    if child_scheduled_action_name is not None:
        out["scheduled_action_name"] = str(child_scheduled_action_name.text or "")
    child_error_code = el.find("ErrorCode")
    if child_error_code is not None:
        out["error_code"] = str(child_error_code.text or "")
    child_error_message = el.find("ErrorMessage")
    if child_error_message is not None:
        out["error_message"] = str(child_error_message.text or "")
    return out
