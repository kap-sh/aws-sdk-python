"""Generated from Smithy shape ``com.amazonaws.quicksight#FreeFormSectionLayoutConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.free_from_layout_element_list


class FreeFormSectionLayoutConfiguration(TypedDict):
    elements: "aws_sdk_quicksight.types.free_from_layout_element_list.FreeFromLayoutElementList"
    """<p>The elements that are included in the free-form layout.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FreeFormSectionLayoutConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.free_from_layout_element_list

    out["Elements"] = (
        aws_sdk_quicksight.types.free_from_layout_element_list.serialize_json(
            value["elements"]
        )
    )
    return out


def deserialize_json(data: dict) -> FreeFormSectionLayoutConfiguration:
    out: FreeFormSectionLayoutConfiguration = {}  # type: ignore[typeddict-item]
    if "Elements" in data:
        import aws_sdk_quicksight.types.free_from_layout_element_list

        out["elements"] = (
            aws_sdk_quicksight.types.free_from_layout_element_list.deserialize_json(
                data["Elements"]
            )
        )
    else:
        raise DeserializationError(
            "FreeFormSectionLayoutConfiguration.elements required"
        )
    return out
