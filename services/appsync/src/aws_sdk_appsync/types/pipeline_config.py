"""Generated from Smithy shape ``com.amazonaws.appsync#PipelineConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appsync.types.functions_ids


class PipelineConfig(TypedDict):
    functions: NotRequired["aws_sdk_appsync.types.functions_ids.FunctionsIds"]
    """<p>A list of <code>Function</code> objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipelineConfig) -> dict:
    out: dict = {}
    if "functions" in value:
        import aws_sdk_appsync.types.functions_ids

        out["functions"] = aws_sdk_appsync.types.functions_ids.serialize_json(
            value["functions"]
        )
    return out


def deserialize_json(data: dict) -> PipelineConfig:
    out: PipelineConfig = {}  # type: ignore[typeddict-item]
    if "functions" in data:
        import aws_sdk_appsync.types.functions_ids

        out["functions"] = aws_sdk_appsync.types.functions_ids.deserialize_json(
            data["functions"]
        )
    return out
