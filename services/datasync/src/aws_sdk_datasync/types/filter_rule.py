"""Generated from Smithy shape ``com.amazonaws.datasync#FilterRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datasync.types.filter_type
    import aws_sdk_datasync.types.filter_value


class FilterRule(TypedDict, closed=True):
    filter_type: NotRequired["aws_sdk_datasync.types.filter_type.FilterType"]
    """<p>The type of filter rule to apply. DataSync only supports the SIMPLE_PATTERN rule type.</p>"""
    value: NotRequired["aws_sdk_datasync.types.filter_value.FilterValue"]
    r"""<p>A single filter string that consists of the patterns to include or exclude. The patterns are delimited by \"|\" (that is, a pipe), for example: <code>/folder1|/folder2</code> </p> <p> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterRule) -> dict:
    out: dict = {}
    if "filter_type" in value:
        import aws_sdk_datasync.types.filter_type

        out["FilterType"] = aws_sdk_datasync.types.filter_type.serialize_aws_json_1_1(
            value["filter_type"]
        )
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FilterRule:
    out: FilterRule = {}  # type: ignore[typeddict-item]
    if "FilterType" in data:
        import aws_sdk_datasync.types.filter_type

        out["filter_type"] = (
            aws_sdk_datasync.types.filter_type.deserialize_aws_json_1_1(
                data["FilterType"]
            )
        )
    if "Value" in data:
        out["value"] = data["Value"]
    return out
