"""Generated from Smithy shape ``com.amazonaws.appflow#SAPODataParallelismConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.sapo_data_max_parallelism


class SAPODataParallelismConfig(TypedDict, closed=True):
    max_parallelism: (
        "aws_sdk_appflow.types.sapo_data_max_parallelism.SAPODataMaxParallelism"
    )
    """<p>The maximum number of processes that Amazon AppFlow runs at the same time when it retrieves your data from your SAP application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SAPODataParallelismConfig) -> dict:
    out: dict = {}
    out["maxParallelism"] = value["max_parallelism"]
    return out


def deserialize_json(data: dict) -> SAPODataParallelismConfig:
    out: SAPODataParallelismConfig = {}  # type: ignore[typeddict-item]
    if "maxParallelism" in data:
        out["max_parallelism"] = data["maxParallelism"]
    else:
        raise DeserializationError("SAPODataParallelismConfig.max_parallelism required")
    return out
