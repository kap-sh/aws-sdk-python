"""Generated from Smithy shape ``com.amazonaws.qapps#BatchDeleteCategoryInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.delete_category_input_list
    import aws_sdk_qapps.types.instance_id


class BatchDeleteCategoryInput(TypedDict):
    instance_id: "aws_sdk_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    categories: "aws_sdk_qapps.types.delete_category_input_list.DeleteCategoryInputList"
    """<p>The list of IDs of the categories to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteCategoryInput) -> dict:
    out: dict = {}
    import aws_sdk_qapps.types.delete_category_input_list

    out["categories"] = aws_sdk_qapps.types.delete_category_input_list.serialize_json(
        value["categories"]
    )
    return out


def deserialize_json(data: dict) -> BatchDeleteCategoryInput:
    out: BatchDeleteCategoryInput = {}  # type: ignore[typeddict-item]
    if "categories" in data:
        import aws_sdk_qapps.types.delete_category_input_list

        out["categories"] = (
            aws_sdk_qapps.types.delete_category_input_list.deserialize_json(
                data["categories"]
            )
        )
    else:
        raise DeserializationError("BatchDeleteCategoryInput.categories required")
    return out
