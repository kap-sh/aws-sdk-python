"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#Trigger``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.resource_id


class Trigger(TypedDict):
    name: NotRequired["aws_sdk_elastic_beanstalk.types.resource_id.ResourceId"]
    """<p>The name of the trigger.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Trigger, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))


def deserialize_query(el: Element) -> Trigger:
    out: Trigger = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    return out
