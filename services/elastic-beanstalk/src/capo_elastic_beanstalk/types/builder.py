"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#Builder``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.arn


class Builder(TypedDict, closed=True):
    arn: NotRequired["capo_elastic_beanstalk.types.arn.ARN"]
    """<p>The ARN of the builder.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Builder, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "arn" in value:
        pairs.append((f"{key_prefix}ARN", str(value["arn"])))


def deserialize_query(el: Element) -> Builder:
    out: Builder = {}  # type: ignore[typeddict-item]
    child_arn = el.find("ARN")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    return out
