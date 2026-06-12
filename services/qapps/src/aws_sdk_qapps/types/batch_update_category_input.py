"""Generated from Smithy shape ``com.amazonaws.qapps#BatchUpdateCategoryInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.category_list_input
    import aws_sdk_qapps.types.instance_id


class BatchUpdateCategoryInput(TypedDict):
    instance_id: "aws_sdk_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    categories: "aws_sdk_qapps.types.category_list_input.CategoryListInput"
    """<p>The list of categories to be updated with their new values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateCategoryInput) -> dict:
    out: dict = {}
    import aws_sdk_qapps.types.category_list_input

    out["categories"] = aws_sdk_qapps.types.category_list_input.serialize_json(
        value["categories"]
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateCategoryInput:
    out: BatchUpdateCategoryInput = {}  # type: ignore[typeddict-item]
    if "categories" in data:
        import aws_sdk_qapps.types.category_list_input

        out["categories"] = aws_sdk_qapps.types.category_list_input.deserialize_json(
            data["categories"]
        )
    else:
        raise DeserializationError("BatchUpdateCategoryInput.categories required")
    return out
