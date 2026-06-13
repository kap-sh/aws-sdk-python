"""Generated from Smithy shape ``com.amazonaws.quicksight#KPIVisualLayoutOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.kpi_visual_standard_layout


class KPIVisualLayoutOptions(TypedDict):
    standard_layout: NotRequired[
        "aws_sdk_quicksight.types.kpi_visual_standard_layout.KPIVisualStandardLayout"
    ]
    """<p>The standard layout of the KPI visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KPIVisualLayoutOptions) -> dict:
    out: dict = {}
    if "standard_layout" in value:
        import aws_sdk_quicksight.types.kpi_visual_standard_layout

        out["StandardLayout"] = (
            aws_sdk_quicksight.types.kpi_visual_standard_layout.serialize_json(
                value["standard_layout"]
            )
        )
    return out


def deserialize_json(data: dict) -> KPIVisualLayoutOptions:
    out: KPIVisualLayoutOptions = {}  # type: ignore[typeddict-item]
    if "StandardLayout" in data:
        import aws_sdk_quicksight.types.kpi_visual_standard_layout

        out["standard_layout"] = (
            aws_sdk_quicksight.types.kpi_visual_standard_layout.deserialize_json(
                data["StandardLayout"]
            )
        )
    return out
