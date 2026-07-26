"""Generated from Smithy shape ``com.amazonaws.dax#DescribeParameterGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dax.types.parameter_group_list
    import capo_dax.types.string


class DescribeParameterGroupsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_dax.types.string.String"]
    """<p>Provides an identifier to allow retrieval of paginated results.</p>"""
    parameter_groups: NotRequired[
        "capo_dax.types.parameter_group_list.ParameterGroupList"
    ]
    """<p>An array of parameter groups. Each element in the array represents one parameter group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeParameterGroupsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "parameter_groups" in value:
        import capo_dax.types.parameter_group_list

        out["ParameterGroups"] = (
            capo_dax.types.parameter_group_list.serialize_aws_json_1_1(
                value["parameter_groups"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeParameterGroupsResponse:
    out: DescribeParameterGroupsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "ParameterGroups" in data:
        import capo_dax.types.parameter_group_list

        out["parameter_groups"] = (
            capo_dax.types.parameter_group_list.deserialize_aws_json_1_1(
                data["ParameterGroups"]
            )
        )
    return out
