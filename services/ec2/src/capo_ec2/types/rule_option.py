"""Generated from Smithy shape ``com.amazonaws.ec2#RuleOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.string_list


class RuleOption(TypedDict, closed=True):
    keyword: NotRequired["capo_ec2.types.string.String"]
    """<p>The Suricata keyword.</p>"""
    settings: NotRequired["capo_ec2.types.string_list.StringList"]
    """<p>The settings for the keyword.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RuleOption, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "keyword" in value:
        pairs.append((f"{prefix}.Keyword", str(value["keyword"])))
    if "settings" in value:
        import capo_ec2.types.string_list

        capo_ec2.types.string_list.serialize_ec2_query(
            value["settings"], pairs, f"{prefix}.SettingSet"
        )


def deserialize_ec2_query(el: Element) -> RuleOption:
    out: RuleOption = {}  # type: ignore[typeddict-item]
    child_keyword = el.find("Keyword")
    if child_keyword is not None:
        out["keyword"] = str(child_keyword.text or "")
    if el.find("SettingSet") is not None:
        import capo_ec2.types.string_list

        out["settings"] = capo_ec2.types.string_list.deserialize_ec2_query(
            el, "SettingSet"
        )
    return out
