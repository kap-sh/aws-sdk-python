"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#CostCategoryValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.match_options
    import capo_bcm_dashboards.types.string_list


class CostCategoryValues(TypedDict, closed=True):
    key: NotRequired["str"]
    """<p>The key of the cost category to filter on.</p>"""
    values: NotRequired["capo_bcm_dashboards.types.string_list.StringList"]
    """<p>The values to match for the specified cost category key.</p>"""
    match_options: NotRequired["capo_bcm_dashboards.types.match_options.MatchOptions"]
    """<p>The match options for cost category values, such as <code>EQUALS</code>, <code>CONTAINS</code>, <code>STARTS_WITH</code>, or <code>ENDS_WITH</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CostCategoryValues) -> dict:
    out: dict = {}
    if "key" in value:
        out["key"] = value["key"]
    if "values" in value:
        import capo_bcm_dashboards.types.string_list

        out["values"] = capo_bcm_dashboards.types.string_list.serialize_aws_json_1_0(
            value["values"]
        )
    if "match_options" in value:
        import capo_bcm_dashboards.types.match_options

        out["matchOptions"] = (
            capo_bcm_dashboards.types.match_options.serialize_aws_json_1_0(
                value["match_options"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CostCategoryValues:
    out: CostCategoryValues = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    if "values" in data:
        import capo_bcm_dashboards.types.string_list

        out["values"] = capo_bcm_dashboards.types.string_list.deserialize_aws_json_1_0(
            data["values"]
        )
    if "matchOptions" in data:
        import capo_bcm_dashboards.types.match_options

        out["match_options"] = (
            capo_bcm_dashboards.types.match_options.deserialize_aws_json_1_0(
                data["matchOptions"]
            )
        )
    return out
