"""Generated from Smithy shape ``com.amazonaws.macie2#TagScopeTerm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.__list_of_tag_value_pair
    import aws_sdk_macie2.types.__string
    import aws_sdk_macie2.types.job_comparator
    import aws_sdk_macie2.types.tag_target


class TagScopeTerm(TypedDict, closed=True):
    comparator: NotRequired["aws_sdk_macie2.types.job_comparator.JobComparator"]
    """<p>The operator to use in the condition. Valid values are EQ (equals) or NE (not equals).</p>"""
    key: NotRequired["aws_sdk_macie2.types.__string.__string"]
    """<p>The object property to use in the condition. The only valid value is TAG.</p>"""
    tag_values: NotRequired[
        "aws_sdk_macie2.types.__list_of_tag_value_pair.__listOfTagValuePair"
    ]
    """<p>The tag keys or tag key and value pairs to use in the condition. To specify only tag keys in a condition, specify the keys in this array and set the value for each associated tag value to an empty string.</p>"""
    target: NotRequired["aws_sdk_macie2.types.tag_target.TagTarget"]
    """<p>The type of object to apply the condition to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagScopeTerm) -> dict:
    out: dict = {}
    if "comparator" in value:
        import aws_sdk_macie2.types.job_comparator

        out["comparator"] = aws_sdk_macie2.types.job_comparator.serialize_json(
            value["comparator"]
        )
    if "key" in value:
        out["key"] = value["key"]
    if "tag_values" in value:
        import aws_sdk_macie2.types.__list_of_tag_value_pair

        out["tagValues"] = aws_sdk_macie2.types.__list_of_tag_value_pair.serialize_json(
            value["tag_values"]
        )
    if "target" in value:
        import aws_sdk_macie2.types.tag_target

        out["target"] = aws_sdk_macie2.types.tag_target.serialize_json(value["target"])
    return out


def deserialize_json(data: dict) -> TagScopeTerm:
    out: TagScopeTerm = {}  # type: ignore[typeddict-item]
    if "comparator" in data:
        import aws_sdk_macie2.types.job_comparator

        out["comparator"] = aws_sdk_macie2.types.job_comparator.deserialize_json(
            data["comparator"]
        )
    if "key" in data:
        out["key"] = data["key"]
    if "tagValues" in data:
        import aws_sdk_macie2.types.__list_of_tag_value_pair

        out["tag_values"] = (
            aws_sdk_macie2.types.__list_of_tag_value_pair.deserialize_json(
                data["tagValues"]
            )
        )
    if "target" in data:
        import aws_sdk_macie2.types.tag_target

        out["target"] = aws_sdk_macie2.types.tag_target.deserialize_json(data["target"])
    return out
