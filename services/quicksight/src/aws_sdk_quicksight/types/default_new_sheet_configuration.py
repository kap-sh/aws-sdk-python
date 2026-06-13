"""Generated from Smithy shape ``com.amazonaws.quicksight#DefaultNewSheetConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.default_interactive_layout_configuration
    import aws_sdk_quicksight.types.default_paginated_layout_configuration
    import aws_sdk_quicksight.types.sheet_content_type


class DefaultNewSheetConfiguration(TypedDict):
    interactive_layout_configuration: NotRequired[
        "aws_sdk_quicksight.types.default_interactive_layout_configuration.DefaultInteractiveLayoutConfiguration"
    ]
    """<p>The options that determine the default settings for interactive layout configuration.</p>"""
    paginated_layout_configuration: NotRequired[
        "aws_sdk_quicksight.types.default_paginated_layout_configuration.DefaultPaginatedLayoutConfiguration"
    ]
    """<p>The options that determine the default settings for a paginated layout configuration.</p>"""
    sheet_content_type: NotRequired[
        "aws_sdk_quicksight.types.sheet_content_type.SheetContentType"
    ]
    """<p>The option that determines the sheet content type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DefaultNewSheetConfiguration) -> dict:
    out: dict = {}
    if "interactive_layout_configuration" in value:
        import aws_sdk_quicksight.types.default_interactive_layout_configuration

        out["InteractiveLayoutConfiguration"] = (
            aws_sdk_quicksight.types.default_interactive_layout_configuration.serialize_json(
                value["interactive_layout_configuration"]
            )
        )
    if "paginated_layout_configuration" in value:
        import aws_sdk_quicksight.types.default_paginated_layout_configuration

        out["PaginatedLayoutConfiguration"] = (
            aws_sdk_quicksight.types.default_paginated_layout_configuration.serialize_json(
                value["paginated_layout_configuration"]
            )
        )
    if "sheet_content_type" in value:
        import aws_sdk_quicksight.types.sheet_content_type

        out["SheetContentType"] = (
            aws_sdk_quicksight.types.sheet_content_type.serialize_json(
                value["sheet_content_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> DefaultNewSheetConfiguration:
    out: DefaultNewSheetConfiguration = {}  # type: ignore[typeddict-item]
    if "InteractiveLayoutConfiguration" in data:
        import aws_sdk_quicksight.types.default_interactive_layout_configuration

        out["interactive_layout_configuration"] = (
            aws_sdk_quicksight.types.default_interactive_layout_configuration.deserialize_json(
                data["InteractiveLayoutConfiguration"]
            )
        )
    if "PaginatedLayoutConfiguration" in data:
        import aws_sdk_quicksight.types.default_paginated_layout_configuration

        out["paginated_layout_configuration"] = (
            aws_sdk_quicksight.types.default_paginated_layout_configuration.deserialize_json(
                data["PaginatedLayoutConfiguration"]
            )
        )
    if "SheetContentType" in data:
        import aws_sdk_quicksight.types.sheet_content_type

        out["sheet_content_type"] = (
            aws_sdk_quicksight.types.sheet_content_type.deserialize_json(
                data["SheetContentType"]
            )
        )
    return out
