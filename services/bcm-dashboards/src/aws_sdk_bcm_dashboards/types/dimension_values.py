"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#DimensionValues``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bcm_dashboards.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_dashboards.types.dimension
    import aws_sdk_bcm_dashboards.types.match_options
    import aws_sdk_bcm_dashboards.types.string_list


class DimensionValues(TypedDict):
    key: "aws_sdk_bcm_dashboards.types.dimension.Dimension"
    """<p>The key of the dimension to filter on (for example, <code>SERVICE</code>, <code>USAGE_TYPE</code>, or <code>OPERATION</code>).</p>"""
    values: "aws_sdk_bcm_dashboards.types.string_list.StringList"
    """<p>The values to match for the specified dimension key.</p>"""
    match_options: NotRequired[
        "aws_sdk_bcm_dashboards.types.match_options.MatchOptions"
    ]
    """<p>The match options for dimension values, such as <code>EQUALS</code>, <code>CONTAINS</code>, <code>STARTS_WITH</code>, or <code>ENDS_WITH</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DimensionValues) -> dict:
    out: dict = {}
    import aws_sdk_bcm_dashboards.types.dimension

    out["key"] = aws_sdk_bcm_dashboards.types.dimension.serialize_aws_json_1_0(
        value["key"]
    )
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


def deserialize_aws_json_1_0(data: dict) -> DimensionValues:
    out: DimensionValues = {}  # type: ignore[typeddict-item]
    if "key" in data:
        import aws_sdk_bcm_dashboards.types.dimension

        out["key"] = aws_sdk_bcm_dashboards.types.dimension.deserialize_aws_json_1_0(
            data["key"]
        )
    else:
        raise DeserializationError("DimensionValues.key required")
    if "values" in data:
        import aws_sdk_bcm_dashboards.types.string_list

        out["values"] = (
            aws_sdk_bcm_dashboards.types.string_list.deserialize_aws_json_1_0(
                data["values"]
            )
        )
    else:
        raise DeserializationError("DimensionValues.values required")
    if "matchOptions" in data:
        import aws_sdk_bcm_dashboards.types.match_options

        out["match_options"] = (
            aws_sdk_bcm_dashboards.types.match_options.deserialize_aws_json_1_0(
                data["matchOptions"]
            )
        )
    return out
