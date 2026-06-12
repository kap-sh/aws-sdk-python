"""Generated from Smithy shape ``com.amazonaws.connect#SecurityProfileSearchConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.security_profile_search_criteria

SecurityProfileSearchConditionList: TypeAlias = list[
    "aws_sdk_connect.types.security_profile_search_criteria.SecurityProfileSearchCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityProfileSearchConditionList) -> list:
    import aws_sdk_connect.types.security_profile_search_criteria

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.security_profile_search_criteria.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SecurityProfileSearchConditionList:
    import aws_sdk_connect.types.security_profile_search_criteria

    out: SecurityProfileSearchConditionList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.security_profile_search_criteria.deserialize_json(
                item
            )
        )
    return out
