"""Generated from Smithy shape ``com.amazonaws.securityhub#SortCriteria``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.sort_criterion

SortCriteria: TypeAlias = list["aws_sdk_securityhub.types.sort_criterion.SortCriterion"]


# --- restJson1 ser/de ---
def serialize_json(value: SortCriteria) -> list:
    import aws_sdk_securityhub.types.sort_criterion

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.sort_criterion.serialize_json(item))
    return out


def deserialize_json(data: list) -> SortCriteria:
    import aws_sdk_securityhub.types.sort_criterion

    out: SortCriteria = []
    for item in data:
        out.append(aws_sdk_securityhub.types.sort_criterion.deserialize_json(item))
    return out
