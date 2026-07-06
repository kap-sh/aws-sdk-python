"""Generated from Smithy shape ``com.amazonaws.mturk#ParameterMapEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mturk.types.string
    import aws_sdk_mturk.types.string_list


class ParameterMapEntry(TypedDict, closed=True):
    key: NotRequired["aws_sdk_mturk.types.string.String"]
    """<p> The QuestionID from the HIT that is used to identify which question requires Mechanical Turk to score as part of the ScoreMyKnownAnswers/2011-09-01 Review Policy. </p>"""
    values: NotRequired["aws_sdk_mturk.types.string_list.StringList"]
    """<p> The list of answers to the question specified in the MapEntry Key element. The Worker must match all values in order for the answer to be scored correctly. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterMapEntry) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "values" in value:
        import aws_sdk_mturk.types.string_list

        out["Values"] = aws_sdk_mturk.types.string_list.serialize_aws_json_1_1(
            value["values"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ParameterMapEntry:
    out: ParameterMapEntry = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Values" in data:
        import aws_sdk_mturk.types.string_list

        out["values"] = aws_sdk_mturk.types.string_list.deserialize_aws_json_1_1(
            data["Values"]
        )
    return out
