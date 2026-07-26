"""Generated from Smithy shape ``com.amazonaws.quicksight#KPIVisualLayoutOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.kpi_visual_standard_layout


class KPIVisualLayoutOptions(TypedDict, closed=True):
    standard_layout: NotRequired[
        "capo_quicksight.types.kpi_visual_standard_layout.KPIVisualStandardLayout"
    ]
    """<p>The standard layout of the KPI visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KPIVisualLayoutOptions) -> dict:
    out: dict = {}
    if "standard_layout" in value:
        import capo_quicksight.types.kpi_visual_standard_layout

        out["StandardLayout"] = (
            capo_quicksight.types.kpi_visual_standard_layout.serialize_json(
                value["standard_layout"]
            )
        )
    return out


def deserialize_json(data: dict) -> KPIVisualLayoutOptions:
    out: KPIVisualLayoutOptions = {}  # type: ignore[typeddict-item]
    if "StandardLayout" in data:
        import capo_quicksight.types.kpi_visual_standard_layout

        out["standard_layout"] = (
            capo_quicksight.types.kpi_visual_standard_layout.deserialize_json(
                data["StandardLayout"]
            )
        )
    return out
