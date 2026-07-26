"""Generated from Smithy shape ``com.amazonaws.lakeformation#LakeFormationOptInsInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lakeformation.types.lake_formation_opt_ins_info

LakeFormationOptInsInfoList: TypeAlias = list[
    "capo_lakeformation.types.lake_formation_opt_ins_info.LakeFormationOptInsInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: LakeFormationOptInsInfoList) -> list:
    import capo_lakeformation.types.lake_formation_opt_ins_info

    out: list = []
    for item in value:
        out.append(
            capo_lakeformation.types.lake_formation_opt_ins_info.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> LakeFormationOptInsInfoList:
    import capo_lakeformation.types.lake_formation_opt_ins_info

    out: LakeFormationOptInsInfoList = []
    for item in data:
        out.append(
            capo_lakeformation.types.lake_formation_opt_ins_info.deserialize_json(item)
        )
    return out
