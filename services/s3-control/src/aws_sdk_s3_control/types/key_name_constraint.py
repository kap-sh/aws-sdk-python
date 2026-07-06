"""Generated from Smithy shape ``com.amazonaws.s3control#KeyNameConstraint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_s3_control.types.non_empty_max_length1024_string_list


class KeyNameConstraint(TypedDict, closed=True):
    match_any_prefix: NotRequired[
        "aws_sdk_s3_control.types.non_empty_max_length1024_string_list.NonEmptyMaxLength1024StringList"
    ]
    """<p>If provided, the generated manifest includes objects where the specified string appears at the start of the object key string. Each KeyNameConstraint filter accepts an array of strings with a length of 1 string.</p>"""
    match_any_suffix: NotRequired[
        "aws_sdk_s3_control.types.non_empty_max_length1024_string_list.NonEmptyMaxLength1024StringList"
    ]
    """<p>If provided, the generated manifest includes objects where the specified string appears at the end of the object key string. Each KeyNameConstraint filter accepts an array of strings with a length of 1 string.</p>"""
    match_any_substring: NotRequired[
        "aws_sdk_s3_control.types.non_empty_max_length1024_string_list.NonEmptyMaxLength1024StringList"
    ]
    """<p>If provided, the generated manifest includes objects where the specified string appears anywhere within the object key string. Each KeyNameConstraint filter accepts an array of strings with a length of 1 string.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: KeyNameConstraint, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "match_any_prefix" in value:
        import aws_sdk_s3_control.types.non_empty_max_length1024_string_list

        aws_sdk_s3_control.types.non_empty_max_length1024_string_list.serialize_xml(
            value["match_any_prefix"], el, "MatchAnyPrefix"
        )
    if "match_any_suffix" in value:
        import aws_sdk_s3_control.types.non_empty_max_length1024_string_list

        aws_sdk_s3_control.types.non_empty_max_length1024_string_list.serialize_xml(
            value["match_any_suffix"], el, "MatchAnySuffix"
        )
    if "match_any_substring" in value:
        import aws_sdk_s3_control.types.non_empty_max_length1024_string_list

        aws_sdk_s3_control.types.non_empty_max_length1024_string_list.serialize_xml(
            value["match_any_substring"], el, "MatchAnySubstring"
        )


def deserialize_xml(el: Element) -> KeyNameConstraint:
    out: KeyNameConstraint = {}  # type: ignore[typeddict-item]
    child_match_any_prefix = el.find("MatchAnyPrefix")
    if child_match_any_prefix is not None:
        import aws_sdk_s3_control.types.non_empty_max_length1024_string_list

        out["match_any_prefix"] = (
            aws_sdk_s3_control.types.non_empty_max_length1024_string_list.deserialize_xml(
                child_match_any_prefix
            )
        )
    child_match_any_suffix = el.find("MatchAnySuffix")
    if child_match_any_suffix is not None:
        import aws_sdk_s3_control.types.non_empty_max_length1024_string_list

        out["match_any_suffix"] = (
            aws_sdk_s3_control.types.non_empty_max_length1024_string_list.deserialize_xml(
                child_match_any_suffix
            )
        )
    child_match_any_substring = el.find("MatchAnySubstring")
    if child_match_any_substring is not None:
        import aws_sdk_s3_control.types.non_empty_max_length1024_string_list

        out["match_any_substring"] = (
            aws_sdk_s3_control.types.non_empty_max_length1024_string_list.deserialize_xml(
                child_match_any_substring
            )
        )
    return out
