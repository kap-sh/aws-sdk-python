"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListOfLakeFormationTagPolicies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.lake_formation_tag_policy_details

ListOfLakeFormationTagPolicies: TypeAlias = list[
    "aws_sdk_dataexchange.types.lake_formation_tag_policy_details.LakeFormationTagPolicyDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfLakeFormationTagPolicies) -> list:
    import aws_sdk_dataexchange.types.lake_formation_tag_policy_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_dataexchange.types.lake_formation_tag_policy_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListOfLakeFormationTagPolicies:
    import aws_sdk_dataexchange.types.lake_formation_tag_policy_details

    out: ListOfLakeFormationTagPolicies = []
    for item in data:
        out.append(
            aws_sdk_dataexchange.types.lake_formation_tag_policy_details.deserialize_json(
                item
            )
        )
    return out
