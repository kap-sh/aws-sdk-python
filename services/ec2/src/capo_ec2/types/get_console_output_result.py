"""Generated from Smithy shape ``com.amazonaws.ec2#GetConsoleOutputResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.date_time
    import capo_ec2.types.string


class GetConsoleOutputResult(TypedDict, closed=True):
    instance_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the instance.</p>"""
    timestamp: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The time at which the output was last updated.</p>"""
    output: NotRequired["capo_ec2.types.string.String"]
    """<p>The console output, base64-encoded. If you are using a command line tool, the tool decodes the output for you.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetConsoleOutputResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "timestamp" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["timestamp"], pairs, f"{key_prefix}Timestamp"
        )
    if "output" in value:
        pairs.append((f"{key_prefix}Output", str(value["output"])))


def deserialize_ec2_query(el: Element) -> GetConsoleOutputResult:
    out: GetConsoleOutputResult = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("instanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_timestamp = el.find("timestamp")
    if child_timestamp is not None:
        import capo_ec2.types.date_time

        out["timestamp"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_timestamp
        )
    child_output = el.find("output")
    if child_output is not None:
        out["output"] = str(child_output.text or "")
    return out
