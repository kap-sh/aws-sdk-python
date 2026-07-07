"""Generated from Smithy shape ``com.amazonaws.autoscaling#StartInstanceRefreshAnswer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.xml_string_max_len255


class StartInstanceRefreshAnswer(TypedDict, closed=True):
    instance_refresh_id: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>A unique ID for tracking the progress of the instance refresh.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StartInstanceRefreshAnswer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instance_refresh_id" in value:
        pairs.append((f"{prefix}.InstanceRefreshId", str(value["instance_refresh_id"])))


def deserialize_query(el: Element) -> StartInstanceRefreshAnswer:
    out: StartInstanceRefreshAnswer = {}  # type: ignore[typeddict-item]
    child_instance_refresh_id = el.find("InstanceRefreshId")
    if child_instance_refresh_id is not None:
        out["instance_refresh_id"] = str(child_instance_refresh_id.text or "")
    return out
