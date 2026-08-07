"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#OptionRestrictionRegex``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.regex_label
    import capo_elastic_beanstalk.types.regex_pattern


class OptionRestrictionRegex(TypedDict, closed=True):
    pattern: NotRequired["capo_elastic_beanstalk.types.regex_pattern.RegexPattern"]
    """<p>The regular expression pattern that a string configuration option value with this restriction must match.</p>"""
    label: NotRequired["capo_elastic_beanstalk.types.regex_label.RegexLabel"]
    """<p>A unique name representing this regular expression.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: OptionRestrictionRegex, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "pattern" in value:
        pairs.append((f"{key_prefix}Pattern", str(value["pattern"])))
    if "label" in value:
        pairs.append((f"{key_prefix}Label", str(value["label"])))


def deserialize_query(el: Element) -> OptionRestrictionRegex:
    out: OptionRestrictionRegex = {}  # type: ignore[typeddict-item]
    child_pattern = el.find("Pattern")
    if child_pattern is not None:
        out["pattern"] = str(child_pattern.text or "")
    child_label = el.find("Label")
    if child_label is not None:
        out["label"] = str(child_label.text or "")
    return out
