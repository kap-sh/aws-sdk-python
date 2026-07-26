"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListOfLakeFormationTagPolicies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dataexchange.types.lake_formation_tag_policy_details

ListOfLakeFormationTagPolicies: TypeAlias = list[
    "capo_dataexchange.types.lake_formation_tag_policy_details.LakeFormationTagPolicyDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfLakeFormationTagPolicies) -> list:
    import capo_dataexchange.types.lake_formation_tag_policy_details

    out: list = []
    for item in value:
        out.append(
            capo_dataexchange.types.lake_formation_tag_policy_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListOfLakeFormationTagPolicies:
    import capo_dataexchange.types.lake_formation_tag_policy_details

    out: ListOfLakeFormationTagPolicies = []
    for item in data:
        out.append(
            capo_dataexchange.types.lake_formation_tag_policy_details.deserialize_json(
                item
            )
        )
    return out
