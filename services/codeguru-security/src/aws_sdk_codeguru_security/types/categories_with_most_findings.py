"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#CategoriesWithMostFindings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeguru_security.types.category_with_finding_num

CategoriesWithMostFindings: TypeAlias = list[
    "aws_sdk_codeguru_security.types.category_with_finding_num.CategoryWithFindingNum"
]


# --- restJson1 ser/de ---
def serialize_json(value: CategoriesWithMostFindings) -> list:
    import aws_sdk_codeguru_security.types.category_with_finding_num

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codeguru_security.types.category_with_finding_num.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CategoriesWithMostFindings:
    import aws_sdk_codeguru_security.types.category_with_finding_num

    out: CategoriesWithMostFindings = []
    for item in data:
        out.append(
            aws_sdk_codeguru_security.types.category_with_finding_num.deserialize_json(
                item
            )
        )
    return out
