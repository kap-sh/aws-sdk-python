"""Generated from Smithy shape ``com.amazonaws.s3tables#ReplicationInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.table_arn


class ReplicationInformation(TypedDict, closed=True):
    source_table_arn: "aws_sdk_s3tables.types.table_arn.TableARN"
    """<p>The Amazon Resource Name (ARN) of the source table from which this table is replicated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplicationInformation) -> dict:
    out: dict = {}
    out["sourceTableARN"] = value["source_table_arn"]
    return out


def deserialize_json(data: dict) -> ReplicationInformation:
    out: ReplicationInformation = {}  # type: ignore[typeddict-item]
    if "sourceTableARN" in data:
        out["source_table_arn"] = data["sourceTableARN"]
    else:
        raise DeserializationError("ReplicationInformation.source_table_arn required")
    return out
