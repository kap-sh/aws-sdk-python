"""Generated from Smithy shape ``com.amazonaws.quicksight#Layout``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.layout_configuration


class Layout(TypedDict):
    configuration: "aws_sdk_quicksight.types.layout_configuration.LayoutConfiguration"
    """<p>The configuration that determines what the type of layout for a sheet.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Layout) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.layout_configuration

    out["Configuration"] = aws_sdk_quicksight.types.layout_configuration.serialize_json(
        value["configuration"]
    )
    return out


def deserialize_json(data: dict) -> Layout:
    out: Layout = {}  # type: ignore[typeddict-item]
    if "Configuration" in data:
        import aws_sdk_quicksight.types.layout_configuration

        out["configuration"] = (
            aws_sdk_quicksight.types.layout_configuration.deserialize_json(
                data["Configuration"]
            )
        )
    else:
        raise DeserializationError("Layout.configuration required")
    return out
