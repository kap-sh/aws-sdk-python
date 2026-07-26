"""Generated from Smithy shape ``com.amazonaws.appsync#PipelineConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.functions_ids


class PipelineConfig(TypedDict, closed=True):
    functions: NotRequired["capo_appsync.types.functions_ids.FunctionsIds"]
    """<p>A list of <code>Function</code> objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipelineConfig) -> dict:
    out: dict = {}
    if "functions" in value:
        import capo_appsync.types.functions_ids

        out["functions"] = capo_appsync.types.functions_ids.serialize_json(
            value["functions"]
        )
    return out


def deserialize_json(data: dict) -> PipelineConfig:
    out: PipelineConfig = {}  # type: ignore[typeddict-item]
    if "functions" in data:
        import capo_appsync.types.functions_ids

        out["functions"] = capo_appsync.types.functions_ids.deserialize_json(
            data["functions"]
        )
    return out
