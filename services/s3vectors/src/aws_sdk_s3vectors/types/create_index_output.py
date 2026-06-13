"""Generated from Smithy shape ``com.amazonaws.s3vectors#CreateIndexOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.index_arn


class CreateIndexOutput(TypedDict):
    index_arn: NotRequired["aws_sdk_s3vectors.types.index_arn.IndexArn"]
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
