"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#TagValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bcm_dashboards.types.match_options
    import aws_sdk_bcm_dashboards.types.string_list


class TagValues(TypedDict, closed=True):
    key: NotRequired["str"]
    """<p>The key of the tag to filter on.</p>"""
    values: NotRequired["aws_sdk_bcm_dashboards.types.string_list.StringList"]
    """<p>The values to match for the specified tag key.</p>"""
    match_options: NotRequired[
        "aws_sdk_bcm_dashboards.types.match_options.MatchOptions"
    ]
    """<p>The match options for tag values, such as <code>EQUALS</code>, <code>CONTAINS</code>, <code>STARTS_WITH</code>, or <code>ENDS_WITH</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagValues) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "values" in value:
        import aws_sdk_bcm_dashboards.types.string_list

        out["values"] = aws_sdk_bcm_dashboards.types.string_list.serialize_aws_json_1_0(
            value["values"]
        )
    if "match_options" in value:
        import aws_sdk_bcm_dashboards.types.match_options

        out["matchOptions"] = (
            aws_sdk_bcm_dashboards.types.match_options.serialize_aws_json_1_0(
                value["match_options"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TagValues:
    out: TagValues = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    if "values" in data:
        import aws_sdk_bcm_dashboards.types.string_list

        out["values"] = (
            aws_sdk_bcm_dashboards.types.string_list.deserialize_aws_json_1_0(
                data["values"]
            )
        )
    if "matchOptions" in data:
        import aws_sdk_bcm_dashboards.types.match_options

        out["match_options"] = (
            aws_sdk_bcm_dashboards.types.match_options.deserialize_aws_json_1_0(
                data["matchOptions"]
            )
        )
    return out
