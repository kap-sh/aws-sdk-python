"""Generated from Smithy shape ``com.amazonaws.s3control#StorageLensGroupAndOperator``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.match_any_prefix
    import capo_s3_control.types.match_any_suffix
    import capo_s3_control.types.match_any_tag
    import capo_s3_control.types.match_object_age
    import capo_s3_control.types.match_object_size


class StorageLensGroupAndOperator(TypedDict, closed=True):
    match_any_prefix: NotRequired[
        "capo_s3_control.types.match_any_prefix.MatchAnyPrefix"
    ]
    """<p> Contains a list of prefixes. At least one prefix must be specified. Up to 10 prefixes are allowed. </p>"""
    match_any_suffix: NotRequired[
        "capo_s3_control.types.match_any_suffix.MatchAnySuffix"
    ]
    """<p> Contains a list of suffixes. At least one suffix must be specified. Up to 10 suffixes are allowed. </p>"""
    match_any_tag: NotRequired["capo_s3_control.types.match_any_tag.MatchAnyTag"]
    """<p> Contains the list of object tags. At least one object tag must be specified. Up to 10 object tags are allowed. </p>"""
    match_object_age: NotRequired[
        "capo_s3_control.types.match_object_age.MatchObjectAge"
    ]
    """<p> Contains <code>DaysGreaterThan</code> and <code>DaysLessThan</code> to define the object age range (minimum and maximum number of days). </p>"""
    match_object_size: NotRequired[
        "capo_s3_control.types.match_object_size.MatchObjectSize"
    ]
    """<p> Contains <code>BytesGreaterThan</code> and <code>BytesLessThan</code> to define the object size range (minimum and maximum number of Bytes). </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: StorageLensGroupAndOperator, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "match_any_prefix" in value:
        import capo_s3_control.types.match_any_prefix

        capo_s3_control.types.match_any_prefix.serialize_xml(
            value["match_any_prefix"], el, "MatchAnyPrefix"
        )
    if "match_any_suffix" in value:
        import capo_s3_control.types.match_any_suffix

        capo_s3_control.types.match_any_suffix.serialize_xml(
            value["match_any_suffix"], el, "MatchAnySuffix"
        )
    if "match_any_tag" in value:
        import capo_s3_control.types.match_any_tag

        capo_s3_control.types.match_any_tag.serialize_xml(
            value["match_any_tag"], el, "MatchAnyTag"
        )
    if "match_object_age" in value:
        import capo_s3_control.types.match_object_age

        capo_s3_control.types.match_object_age.serialize_xml(
            value["match_object_age"], el, "MatchObjectAge"
        )
    if "match_object_size" in value:
        import capo_s3_control.types.match_object_size

        capo_s3_control.types.match_object_size.serialize_xml(
            value["match_object_size"], el, "MatchObjectSize"
        )


def deserialize_xml(el: Element) -> StorageLensGroupAndOperator:
    out: StorageLensGroupAndOperator = {}  # type: ignore[typeddict-item]
    child_match_any_prefix = el.find("MatchAnyPrefix")
    if child_match_any_prefix is not None:
        import capo_s3_control.types.match_any_prefix

        out["match_any_prefix"] = (
            capo_s3_control.types.match_any_prefix.deserialize_xml(
                child_match_any_prefix
            )
        )
    child_match_any_suffix = el.find("MatchAnySuffix")
    if child_match_any_suffix is not None:
        import capo_s3_control.types.match_any_suffix

        out["match_any_suffix"] = (
            capo_s3_control.types.match_any_suffix.deserialize_xml(
                child_match_any_suffix
            )
        )
    child_match_any_tag = el.find("MatchAnyTag")
    if child_match_any_tag is not None:
        import capo_s3_control.types.match_any_tag

        out["match_any_tag"] = capo_s3_control.types.match_any_tag.deserialize_xml(
            child_match_any_tag
        )
    child_match_object_age = el.find("MatchObjectAge")
    if child_match_object_age is not None:
        import capo_s3_control.types.match_object_age

        out["match_object_age"] = (
            capo_s3_control.types.match_object_age.deserialize_xml(
                child_match_object_age
            )
        )
    child_match_object_size = el.find("MatchObjectSize")
    if child_match_object_size is not None:
        import capo_s3_control.types.match_object_size

        out["match_object_size"] = (
            capo_s3_control.types.match_object_size.deserialize_xml(
                child_match_object_size
            )
        )
    return out
