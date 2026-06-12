"""Generated from Smithy shape ``com.amazonaws.s3control#StorageLensGroupFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.match_any_prefix
    import aws_sdk_s3_control.types.match_any_suffix
    import aws_sdk_s3_control.types.match_any_tag
    import aws_sdk_s3_control.types.match_object_age
    import aws_sdk_s3_control.types.match_object_size
    import aws_sdk_s3_control.types.storage_lens_group_and_operator
    import aws_sdk_s3_control.types.storage_lens_group_or_operator

StorageLensGroupFilter = TypedDict(
    "StorageLensGroupFilter",
    {
        "match_any_prefix": NotRequired[
            "aws_sdk_s3_control.types.match_any_prefix.MatchAnyPrefix"
        ],
        "match_any_suffix": NotRequired[
            "aws_sdk_s3_control.types.match_any_suffix.MatchAnySuffix"
        ],
        "match_any_tag": NotRequired[
            "aws_sdk_s3_control.types.match_any_tag.MatchAnyTag"
        ],
        "match_object_age": NotRequired[
            "aws_sdk_s3_control.types.match_object_age.MatchObjectAge"
        ],
        "match_object_size": NotRequired[
            "aws_sdk_s3_control.types.match_object_size.MatchObjectSize"
        ],
        "and": NotRequired[
            "aws_sdk_s3_control.types.storage_lens_group_and_operator.StorageLensGroupAndOperator"
        ],
        "or": NotRequired[
            "aws_sdk_s3_control.types.storage_lens_group_or_operator.StorageLensGroupOrOperator"
        ],
    },
)


# --- restXml ser/de ---
def serialize_xml(value: StorageLensGroupFilter, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "match_any_prefix" in value:
        import aws_sdk_s3_control.types.match_any_prefix

        aws_sdk_s3_control.types.match_any_prefix.serialize_xml(
            value["match_any_prefix"], el, "MatchAnyPrefix"
        )
    if "match_any_suffix" in value:
        import aws_sdk_s3_control.types.match_any_suffix

        aws_sdk_s3_control.types.match_any_suffix.serialize_xml(
            value["match_any_suffix"], el, "MatchAnySuffix"
        )
    if "match_any_tag" in value:
        import aws_sdk_s3_control.types.match_any_tag

        aws_sdk_s3_control.types.match_any_tag.serialize_xml(
            value["match_any_tag"], el, "MatchAnyTag"
        )
    if "match_object_age" in value:
        import aws_sdk_s3_control.types.match_object_age

        aws_sdk_s3_control.types.match_object_age.serialize_xml(
            value["match_object_age"], el, "MatchObjectAge"
        )
    if "match_object_size" in value:
        import aws_sdk_s3_control.types.match_object_size

        aws_sdk_s3_control.types.match_object_size.serialize_xml(
            value["match_object_size"], el, "MatchObjectSize"
        )
    if "and" in value:
        import aws_sdk_s3_control.types.storage_lens_group_and_operator

        aws_sdk_s3_control.types.storage_lens_group_and_operator.serialize_xml(
            value["and"], el, "And"
        )
    if "or" in value:
        import aws_sdk_s3_control.types.storage_lens_group_or_operator

        aws_sdk_s3_control.types.storage_lens_group_or_operator.serialize_xml(
            value["or"], el, "Or"
        )


def deserialize_xml(el: Element) -> StorageLensGroupFilter:
    out: StorageLensGroupFilter = {}  # type: ignore[typeddict-item]
    child_match_any_prefix = el.find("MatchAnyPrefix")
    if child_match_any_prefix is not None:
        import aws_sdk_s3_control.types.match_any_prefix

        out["match_any_prefix"] = (
            aws_sdk_s3_control.types.match_any_prefix.deserialize_xml(
                child_match_any_prefix
            )
        )
    child_match_any_suffix = el.find("MatchAnySuffix")
    if child_match_any_suffix is not None:
        import aws_sdk_s3_control.types.match_any_suffix

        out["match_any_suffix"] = (
            aws_sdk_s3_control.types.match_any_suffix.deserialize_xml(
                child_match_any_suffix
            )
        )
    child_match_any_tag = el.find("MatchAnyTag")
    if child_match_any_tag is not None:
        import aws_sdk_s3_control.types.match_any_tag

        out["match_any_tag"] = aws_sdk_s3_control.types.match_any_tag.deserialize_xml(
            child_match_any_tag
        )
    child_match_object_age = el.find("MatchObjectAge")
    if child_match_object_age is not None:
        import aws_sdk_s3_control.types.match_object_age

        out["match_object_age"] = (
            aws_sdk_s3_control.types.match_object_age.deserialize_xml(
                child_match_object_age
            )
        )
    child_match_object_size = el.find("MatchObjectSize")
    if child_match_object_size is not None:
        import aws_sdk_s3_control.types.match_object_size

        out["match_object_size"] = (
            aws_sdk_s3_control.types.match_object_size.deserialize_xml(
                child_match_object_size
            )
        )
    child_and = el.find("And")
    if child_and is not None:
        import aws_sdk_s3_control.types.storage_lens_group_and_operator

        out["and"] = (
            aws_sdk_s3_control.types.storage_lens_group_and_operator.deserialize_xml(
                child_and
            )
        )
    child_or = el.find("Or")
    if child_or is not None:
        import aws_sdk_s3_control.types.storage_lens_group_or_operator

        out["or"] = (
            aws_sdk_s3_control.types.storage_lens_group_or_operator.deserialize_xml(
                child_or
            )
        )
    return out
