"""Generated from Smithy shape ``com.amazonaws.lakeformation#ListLakeFormationOptInsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.lake_formation_opt_ins_info_list
    import aws_sdk_lakeformation.types.token


class ListLakeFormationOptInsResponse(TypedDict, closed=True):
    lake_formation_opt_ins_info_list: NotRequired[
        "aws_sdk_lakeformation.types.lake_formation_opt_ins_info_list.LakeFormationOptInsInfoList"
    ]
    """<p>A list of principal-resource pairs that have Lake Formation permissins enforced.</p>"""
    next_token: NotRequired["aws_sdk_lakeformation.types.token.Token"]
    """<p>A continuation token, if this is not the first call to retrieve this list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLakeFormationOptInsResponse) -> dict:
    out: dict = {}
    if "lake_formation_opt_ins_info_list" in value:
        import aws_sdk_lakeformation.types.lake_formation_opt_ins_info_list

        out["LakeFormationOptInsInfoList"] = (
            aws_sdk_lakeformation.types.lake_formation_opt_ins_info_list.serialize_json(
                value["lake_formation_opt_ins_info_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLakeFormationOptInsResponse:
    out: ListLakeFormationOptInsResponse = {}  # type: ignore[typeddict-item]
    if "LakeFormationOptInsInfoList" in data:
        import aws_sdk_lakeformation.types.lake_formation_opt_ins_info_list

        out["lake_formation_opt_ins_info_list"] = (
            aws_sdk_lakeformation.types.lake_formation_opt_ins_info_list.deserialize_json(
                data["LakeFormationOptInsInfoList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
