"""Generated from Smithy shape ``com.amazonaws.qapps#BatchCreateCategoryInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.batch_create_category_input_category_list
    import aws_sdk_qapps.types.instance_id


class BatchCreateCategoryInput(TypedDict):
    instance_id: "aws_sdk_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""
    categories: "aws_sdk_qapps.types.batch_create_category_input_category_list.BatchCreateCategoryInputCategoryList"
    """<p>The list of category objects to be created</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateCategoryInput) -> dict:
    out: dict = {}
    import aws_sdk_qapps.types.batch_create_category_input_category_list

    out["categories"] = (
        aws_sdk_qapps.types.batch_create_category_input_category_list.serialize_json(
            value["categories"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchCreateCategoryInput:
    out: BatchCreateCategoryInput = {}  # type: ignore[typeddict-item]
    if "categories" in data:
        import aws_sdk_qapps.types.batch_create_category_input_category_list

        out["categories"] = (
            aws_sdk_qapps.types.batch_create_category_input_category_list.deserialize_json(
                data["categories"]
            )
        )
    else:
        raise DeserializationError("BatchCreateCategoryInput.categories required")
    return out
