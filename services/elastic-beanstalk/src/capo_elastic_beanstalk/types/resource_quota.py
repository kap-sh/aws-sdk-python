"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ResourceQuota``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.boxed_int


class ResourceQuota(TypedDict, closed=True):
    maximum: NotRequired["capo_elastic_beanstalk.types.boxed_int.BoxedInt"]
    """<p>The maximum number of instances of this Elastic Beanstalk resource type that an AWS account can use.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ResourceQuota, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "maximum" in value:
        pairs.append((f"{key_prefix}Maximum", str(value["maximum"])))


def deserialize_query(el: Element) -> ResourceQuota:
    out: ResourceQuota = {}  # type: ignore[typeddict-item]
    child_maximum = el.find("Maximum")
    if child_maximum is not None:
        out["maximum"] = int(child_maximum.text or "")
    return out
