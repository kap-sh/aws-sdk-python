"""Generated from Smithy shape ``com.amazonaws.neptunedata#ManagePropertygraphStatisticsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptunedata.types.statistics_auto_generation_mode


class ManagePropertygraphStatisticsInput(TypedDict, closed=True):
    mode: NotRequired[
        "capo_neptunedata.types.statistics_auto_generation_mode.StatisticsAutoGenerationMode"
    ]
    """<p>The statistics generation mode. One of: <code>DISABLE_AUTOCOMPUTE</code>, <code>ENABLE_AUTOCOMPUTE</code>, or <code>REFRESH</code>, the last of which manually triggers DFE statistics generation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagePropertygraphStatisticsInput) -> dict:
    out: dict = {}
    if "mode" in value:
        import capo_neptunedata.types.statistics_auto_generation_mode

        out["mode"] = (
            capo_neptunedata.types.statistics_auto_generation_mode.serialize_json(
                value["mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> ManagePropertygraphStatisticsInput:
    out: ManagePropertygraphStatisticsInput = {}  # type: ignore[typeddict-item]
    if "mode" in data:
        import capo_neptunedata.types.statistics_auto_generation_mode

        out["mode"] = (
            capo_neptunedata.types.statistics_auto_generation_mode.deserialize_json(
                data["mode"]
            )
        )
    return out
