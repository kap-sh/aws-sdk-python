"""Generated from Smithy shape ``com.amazonaws.neptunedata#ManageSparqlStatisticsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_neptunedata.types.statistics_auto_generation_mode


class ManageSparqlStatisticsInput(TypedDict):
    mode: NotRequired[
        "aws_sdk_neptunedata.types.statistics_auto_generation_mode.StatisticsAutoGenerationMode"
    ]
    """<p>The statistics generation mode. One of: <code>DISABLE_AUTOCOMPUTE</code>, <code>ENABLE_AUTOCOMPUTE</code>, or <code>REFRESH</code>, the last of which manually triggers DFE statistics generation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManageSparqlStatisticsInput) -> dict:
    out: dict = {}
    if "mode" in value:
        import aws_sdk_neptunedata.types.statistics_auto_generation_mode

        out["mode"] = (
            aws_sdk_neptunedata.types.statistics_auto_generation_mode.serialize_json(
                value["mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> ManageSparqlStatisticsInput:
    out: ManageSparqlStatisticsInput = {}  # type: ignore[typeddict-item]
    if "mode" in data:
        import aws_sdk_neptunedata.types.statistics_auto_generation_mode

        out["mode"] = (
            aws_sdk_neptunedata.types.statistics_auto_generation_mode.deserialize_json(
                data["mode"]
            )
        )
    return out
