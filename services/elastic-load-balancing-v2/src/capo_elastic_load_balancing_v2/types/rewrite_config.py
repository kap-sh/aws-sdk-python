"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#RewriteConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.string_value


class RewriteConfig(TypedDict, closed=True):
    regex: NotRequired["capo_elastic_load_balancing_v2.types.string_value.StringValue"]
    """<p>The regular expression to match in the input string. The maximum length of the string is 1,024 characters.</p>"""
    replace: NotRequired[
        "capo_elastic_load_balancing_v2.types.string_value.StringValue"
    ]
    """<p>The replacement string to use when rewriting the matched input. The maximum length of the string is 1,024 characters. You can specify capture groups in the regular expression (for example, $1 and $2).</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RewriteConfig, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "regex" in value:
        pairs.append((f"{key_prefix}Regex", str(value["regex"])))
    if "replace" in value:
        pairs.append((f"{key_prefix}Replace", str(value["replace"])))


def deserialize_query(el: Element) -> RewriteConfig:
    out: RewriteConfig = {}  # type: ignore[typeddict-item]
    child_regex = el.find("Regex")
    if child_regex is not None:
        out["regex"] = str(child_regex.text or "")
    child_replace = el.find("Replace")
    if child_replace is not None:
        out["replace"] = str(child_replace.text or "")
    return out
