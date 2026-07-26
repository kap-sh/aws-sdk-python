"""Generated from Smithy shape ``com.amazonaws.s3vectors#CreateIndexOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3vectors.types.index_arn


class CreateIndexOutput(TypedDict, closed=True):
    index_arn: NotRequired["capo_s3vectors.types.index_arn.IndexArn"]
    """<p>The Amazon Resource Name (ARN) of the newly created vector index.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIndexOutput) -> dict:
    out: dict = {}
    if "index_arn" in value:
        out["indexArn"] = value["index_arn"]
    return out


def deserialize_json(data: dict) -> CreateIndexOutput:
    out: CreateIndexOutput = {}  # type: ignore[typeddict-item]
    if "indexArn" in data:
        out["index_arn"] = data["indexArn"]
    return out
