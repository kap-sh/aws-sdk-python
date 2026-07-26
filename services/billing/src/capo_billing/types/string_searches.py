"""Generated from Smithy shape ``com.amazonaws.billing#StringSearches``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.string_search

StringSearches: TypeAlias = list["capo_billing.types.string_search.StringSearch"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StringSearches) -> list:
    import capo_billing.types.string_search

    out: list = []
    for item in value:
        out.append(capo_billing.types.string_search.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> StringSearches:
    import capo_billing.types.string_search

    out: StringSearches = []
    for item in data:
        out.append(capo_billing.types.string_search.deserialize_aws_json_1_0(item))
    return out
