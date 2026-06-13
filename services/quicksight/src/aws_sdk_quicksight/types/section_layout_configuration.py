"""Generated from Smithy shape ``com.amazonaws.quicksight#SectionLayoutConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.free_form_section_layout_configuration


class SectionLayoutConfiguration(TypedDict):
    free_form_layout: "aws_sdk_quicksight.types.free_form_section_layout_configuration.FreeFormSectionLayoutConfiguration"
    """<p>The free-form layout configuration of a section.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SectionLayoutConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.free_form_section_layout_configuration

    out["FreeFormLayout"] = (
        aws_sdk_quicksight.types.free_form_section_layout_configuration.serialize_json(
            value["free_form_layout"]
        )
    )
    return out


def deserialize_json(data: dict) -> SectionLayoutConfiguration:
    out: SectionLayoutConfiguration = {}  # type: ignore[typeddict-item]
    if "FreeFormLayout" in data:
        import aws_sdk_quicksight.types.free_form_section_layout_configuration

        out["free_form_layout"] = (
            aws_sdk_quicksight.types.free_form_section_layout_configuration.deserialize_json(
                data["FreeFormLayout"]
            )
        )
    else:
        raise DeserializationError(
            "SectionLayoutConfiguration.free_form_layout required"
        )
    return out
