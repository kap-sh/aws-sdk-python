"""Generated from Smithy shape ``com.amazonaws.quicksight#DefaultPaginatedLayoutConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.default_section_based_layout_configuration


class DefaultPaginatedLayoutConfiguration(TypedDict, closed=True):
    section_based: NotRequired[
        "capo_quicksight.types.default_section_based_layout_configuration.DefaultSectionBasedLayoutConfiguration"
    ]
    """<p>The options that determine the default settings for a section-based layout configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DefaultPaginatedLayoutConfiguration) -> dict:
    out: dict = {}
    if "section_based" in value:
        import capo_quicksight.types.default_section_based_layout_configuration

        out["SectionBased"] = (
            capo_quicksight.types.default_section_based_layout_configuration.serialize_json(
                value["section_based"]
            )
        )
    return out


def deserialize_json(data: dict) -> DefaultPaginatedLayoutConfiguration:
    out: DefaultPaginatedLayoutConfiguration = {}  # type: ignore[typeddict-item]
    if "SectionBased" in data:
        import capo_quicksight.types.default_section_based_layout_configuration

        out["section_based"] = (
            capo_quicksight.types.default_section_based_layout_configuration.deserialize_json(
                data["SectionBased"]
            )
        )
    return out
