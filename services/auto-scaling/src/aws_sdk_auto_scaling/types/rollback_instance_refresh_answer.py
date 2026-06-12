"""Generated from Smithy shape ``com.amazonaws.autoscaling#RollbackInstanceRefreshAnswer``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.xml_string_max_len255


class RollbackInstanceRefreshAnswer(TypedDict):
    instance_refresh_id: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The instance refresh ID associated with the request. This is the unique ID assigned to the instance refresh when it was started.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RollbackInstanceRefreshAnswer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instance_refresh_id" in value:
        pairs.append((f"{prefix}.InstanceRefreshId", str(value["instance_refresh_id"])))


def deserialize_query(el: Element) -> RollbackInstanceRefreshAnswer:
    out: RollbackInstanceRefreshAnswer = {}  # type: ignore[typeddict-item]
    child_instance_refresh_id = el.find("InstanceRefreshId")
    if child_instance_refresh_id is not None:
        out["instance_refresh_id"] = str(child_instance_refresh_id.text or "")
    return out
