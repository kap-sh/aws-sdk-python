"""Generated from Smithy shape ``com.amazonaws.gamelift#AttributeValue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.double_object
    import aws_sdk_gamelift.types.player_attribute_string
    import aws_sdk_gamelift.types.player_attribute_string_double_map
    import aws_sdk_gamelift.types.player_attribute_string_list


class AttributeValue(TypedDict):
    s: NotRequired[
        "aws_sdk_gamelift.types.player_attribute_string.PlayerAttributeString"
    ]
    """<p>For single string values. Maximum string length is 100 characters.</p>"""
    n: NotRequired["aws_sdk_gamelift.types.double_object.DoubleObject"]
    """<p>For number values, expressed as double.</p>"""
    sl: NotRequired[
        "aws_sdk_gamelift.types.player_attribute_string_list.PlayerAttributeStringList"
    ]
    """<p>For a list of up to 100 strings. Maximum length for each string is 100 characters. Duplicate values are not recognized; all occurrences of the repeated value after the first of a repeated value are ignored.</p>"""
    sdm: NotRequired[
        "aws_sdk_gamelift.types.player_attribute_string_double_map.PlayerAttributeStringDoubleMap"
    ]
    """<p>For a map of up to 10 data type:value pairs. Maximum length for each string value is 100 characters. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttributeValue) -> dict:
    out: dict = {}
    if "s" in value:
        out["S"] = value["s"]
    if "n" in value:
        out["N"] = value["n"]
    if "sl" in value:
        import aws_sdk_gamelift.types.player_attribute_string_list

        out["SL"] = (
            aws_sdk_gamelift.types.player_attribute_string_list.serialize_aws_json_1_1(
                value["sl"]
            )
        )
    if "sdm" in value:
        import aws_sdk_gamelift.types.player_attribute_string_double_map

        out["SDM"] = (
            aws_sdk_gamelift.types.player_attribute_string_double_map.serialize_aws_json_1_1(
                value["sdm"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AttributeValue:
    out: AttributeValue = {}  # type: ignore[typeddict-item]
    if "S" in data:
        out["s"] = data["S"]
    if "N" in data:
        out["n"] = data["N"]
    if "SL" in data:
        import aws_sdk_gamelift.types.player_attribute_string_list

        out["sl"] = (
            aws_sdk_gamelift.types.player_attribute_string_list.deserialize_aws_json_1_1(
                data["SL"]
            )
        )
    if "SDM" in data:
        import aws_sdk_gamelift.types.player_attribute_string_double_map

        out["sdm"] = (
            aws_sdk_gamelift.types.player_attribute_string_double_map.deserialize_aws_json_1_1(
                data["SDM"]
            )
        )
    return out
