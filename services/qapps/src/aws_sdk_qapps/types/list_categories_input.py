"""Generated from Smithy shape ``com.amazonaws.qapps#ListCategoriesInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qapps.types.instance_id


class ListCategoriesInput(TypedDict):
    instance_id: "aws_sdk_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCategoriesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCategoriesInput:
    out: ListCategoriesInput = {}  # type: ignore[typeddict-item]
    return out
