"""Generated from Smithy shape ``com.amazonaws.mturk#PolicyParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mturk.types.parameter_map_entry_list
    import aws_sdk_mturk.types.string
    import aws_sdk_mturk.types.string_list


class PolicyParameter(TypedDict, closed=True):
    key: NotRequired["aws_sdk_mturk.types.string.String"]
    """<p> Name of the parameter from the list of Review Polices. </p>"""
    values: NotRequired["aws_sdk_mturk.types.string_list.StringList"]
    """<p> The list of values of the Parameter</p>"""
    map_entries: NotRequired[
        "aws_sdk_mturk.types.parameter_map_entry_list.ParameterMapEntryList"
    ]
    """<p> List of ParameterMapEntry objects. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PolicyParameter) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "values" in value:
        import aws_sdk_mturk.types.string_list

        out["Values"] = aws_sdk_mturk.types.string_list.serialize_aws_json_1_1(
            value["values"]
        )
    if "map_entries" in value:
        import aws_sdk_mturk.types.parameter_map_entry_list

        out["MapEntries"] = (
            aws_sdk_mturk.types.parameter_map_entry_list.serialize_aws_json_1_1(
                value["map_entries"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PolicyParameter:
    out: PolicyParameter = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Values" in data:
        import aws_sdk_mturk.types.string_list

        out["values"] = aws_sdk_mturk.types.string_list.deserialize_aws_json_1_1(
            data["Values"]
        )
    if "MapEntries" in data:
        import aws_sdk_mturk.types.parameter_map_entry_list

        out["map_entries"] = (
            aws_sdk_mturk.types.parameter_map_entry_list.deserialize_aws_json_1_1(
                data["MapEntries"]
            )
        )
    return out
