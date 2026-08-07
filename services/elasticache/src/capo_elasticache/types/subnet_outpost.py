"""Generated from Smithy shape ``com.amazonaws.elasticache#SubnetOutpost``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.string


class SubnetOutpost(TypedDict, closed=True):
    subnet_outpost_arn: NotRequired["capo_elasticache.types.string.String"]
    """<p>The outpost ARN of the subnet.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SubnetOutpost, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "subnet_outpost_arn" in value:
        pairs.append(
            (f"{key_prefix}SubnetOutpostArn", str(value["subnet_outpost_arn"]))
        )


def deserialize_query(el: Element) -> SubnetOutpost:
    out: SubnetOutpost = {}  # type: ignore[typeddict-item]
    child_subnet_outpost_arn = el.find("SubnetOutpostArn")
    if child_subnet_outpost_arn is not None:
        out["subnet_outpost_arn"] = str(child_subnet_outpost_arn.text or "")
    return out
