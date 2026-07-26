"""Generated from Smithy shape ``com.amazonaws.qapps#ListCategoriesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.instance_id


class ListCategoriesInput(TypedDict, closed=True):
    instance_id: "capo_qapps.types.instance_id.InstanceId"
    """<p>The unique identifier of the Amazon Q Business application environment instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCategoriesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCategoriesInput:
    out: ListCategoriesInput = {}  # type: ignore[typeddict-item]
    return out
