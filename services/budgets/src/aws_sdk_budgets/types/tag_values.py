"""Generated from Smithy shape ``com.amazonaws.budgets#TagValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_budgets.types.match_options
    import aws_sdk_budgets.types.tag_key
    import aws_sdk_budgets.types.values


class TagValues(TypedDict, closed=True):
    key: NotRequired["aws_sdk_budgets.types.tag_key.TagKey"]
    """<p>The key for the tag.</p>"""
    values: NotRequired["aws_sdk_budgets.types.values.Values"]
    """<p>The specific value of the tag.</p>"""
    match_options: NotRequired["aws_sdk_budgets.types.match_options.MatchOptions"]
    """<p>The match options that you can use to filter your results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagValues) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "values" in value:
        import aws_sdk_budgets.types.values

        out["Values"] = aws_sdk_budgets.types.values.serialize_aws_json_1_1(
            value["values"]
        )
    if "match_options" in value:
        import aws_sdk_budgets.types.match_options

        out["MatchOptions"] = (
            aws_sdk_budgets.types.match_options.serialize_aws_json_1_1(
                value["match_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagValues:
    out: TagValues = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Values" in data:
        import aws_sdk_budgets.types.values

        out["values"] = aws_sdk_budgets.types.values.deserialize_aws_json_1_1(
            data["Values"]
        )
    if "MatchOptions" in data:
        import aws_sdk_budgets.types.match_options

        out["match_options"] = (
            aws_sdk_budgets.types.match_options.deserialize_aws_json_1_1(
                data["MatchOptions"]
            )
        )
    return out
