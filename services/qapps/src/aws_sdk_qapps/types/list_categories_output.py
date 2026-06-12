"""Generated from Smithy shape ``com.amazonaws.qapps#ListCategoriesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_qapps.types.categories_list


class ListCategoriesOutput(TypedDict):
    categories: NotRequired["aws_sdk_qapps.types.categories_list.CategoriesList"]
    """<p>The categories of a Amazon Q Business application environment instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCategoriesOutput) -> dict:
    out: dict = {}
    if "categories" in value:
        import aws_sdk_qapps.types.categories_list

        out["categories"] = aws_sdk_qapps.types.categories_list.serialize_json(
            value["categories"]
        )
    return out


def deserialize_json(data: dict) -> ListCategoriesOutput:
    out: ListCategoriesOutput = {}  # type: ignore[typeddict-item]
    if "categories" in data:
        import aws_sdk_qapps.types.categories_list

        out["categories"] = aws_sdk_qapps.types.categories_list.deserialize_json(
            data["categories"]
        )
    return out
