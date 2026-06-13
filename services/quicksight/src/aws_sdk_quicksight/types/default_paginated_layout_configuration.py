"""Generated from Smithy shape ``com.amazonaws.quicksight#DefaultPaginatedLayoutConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.default_section_based_layout_configuration


class DefaultPaginatedLayoutConfiguration(TypedDict):
    section_based: NotRequired[
        "aws_sdk_quicksight.types.default_section_based_layout_configuration.DefaultSectionBasedLayoutConfiguration"
    ]
    """<p>The options that determine the default settings for a section-based layout configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DefaultPaginatedLayoutConfiguration) -> dict:
    out: dict = {}
    if "section_based" in value:
        import aws_sdk_quicksight.types.default_section_based_layout_configuration

        out["SectionBased"] = (
            aws_sdk_quicksight.types.default_section_based_layout_configuration.serialize_json(
                value["section_based"]
            )
        )
    return out


def deserialize_json(data: dict) -> DefaultPaginatedLayoutConfiguration:
    out: DefaultPaginatedLayoutConfiguration = {}  # type: ignore[typeddict-item]
    if "SectionBased" in data:
        import aws_sdk_quicksight.types.default_section_based_layout_configuration

        out["section_based"] = (
            aws_sdk_quicksight.types.default_section_based_layout_configuration.deserialize_json(
                data["SectionBased"]
            )
        )
    return out
