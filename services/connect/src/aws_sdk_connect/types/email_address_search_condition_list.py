"""Generated from Smithy shape ``com.amazonaws.connect#EmailAddressSearchConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.email_address_search_criteria

EmailAddressSearchConditionList: TypeAlias = list[
    "aws_sdk_connect.types.email_address_search_criteria.EmailAddressSearchCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: EmailAddressSearchConditionList) -> list:
    import aws_sdk_connect.types.email_address_search_criteria

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.email_address_search_criteria.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EmailAddressSearchConditionList:
    import aws_sdk_connect.types.email_address_search_criteria

    out: EmailAddressSearchConditionList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.email_address_search_criteria.deserialize_json(item)
        )
    return out
