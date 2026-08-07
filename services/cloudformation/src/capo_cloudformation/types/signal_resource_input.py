"""Generated from Smithy shape ``com.amazonaws.cloudformation#SignalResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.logical_resource_id
    import capo_cloudformation.types.resource_signal_status
    import capo_cloudformation.types.resource_signal_unique_id
    import capo_cloudformation.types.stack_name_or_id


class SignalResourceInput(TypedDict, closed=True):
    stack_name: NotRequired["capo_cloudformation.types.stack_name_or_id.StackNameOrId"]
    """<p>The stack name or unique stack ID that includes the resource that you want to signal.</p>"""
    logical_resource_id: NotRequired[
        "capo_cloudformation.types.logical_resource_id.LogicalResourceId"
    ]
    """<p>The logical ID of the resource that you want to signal. The logical ID is the name of the resource that given in the template.</p>"""
    unique_id: NotRequired[
        "capo_cloudformation.types.resource_signal_unique_id.ResourceSignalUniqueId"
    ]
    """<p>A unique ID of the signal. When you signal Amazon EC2 instances or Auto Scaling groups, specify the instance ID that you are signaling as the unique ID. If you send multiple signals to a single resource (such as signaling a wait condition), each signal requires a different unique ID.</p>"""
    status: NotRequired[
        "capo_cloudformation.types.resource_signal_status.ResourceSignalStatus"
    ]
    """<p>The status of the signal, which is either success or failure. A failure signal causes CloudFormation to immediately fail the stack creation or update.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SignalResourceInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "stack_name" in value:
        pairs.append((f"{key_prefix}StackName", str(value["stack_name"])))
    if "logical_resource_id" in value:
        pairs.append(
            (f"{key_prefix}LogicalResourceId", str(value["logical_resource_id"]))
        )
    if "unique_id" in value:
        pairs.append((f"{key_prefix}UniqueId", str(value["unique_id"])))
    if "status" in value:
        import capo_cloudformation.types.resource_signal_status

        capo_cloudformation.types.resource_signal_status.serialize_query(
            value["status"], pairs, f"{key_prefix}Status"
        )


def deserialize_query(el: Element) -> SignalResourceInput:
    out: SignalResourceInput = {}  # type: ignore[typeddict-item]
    child_stack_name = el.find("StackName")
    if child_stack_name is not None:
        out["stack_name"] = str(child_stack_name.text or "")
    child_logical_resource_id = el.find("LogicalResourceId")
    if child_logical_resource_id is not None:
        out["logical_resource_id"] = str(child_logical_resource_id.text or "")
    child_unique_id = el.find("UniqueId")
    if child_unique_id is not None:
        out["unique_id"] = str(child_unique_id.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import capo_cloudformation.types.resource_signal_status

        out["status"] = (
            capo_cloudformation.types.resource_signal_status.deserialize_query(
                child_status
            )
        )
    return out
