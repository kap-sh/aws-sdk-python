"""Generated from Smithy shape ``com.amazonaws.keyspaces#RestoreTableResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_keyspaces.types.arn


class RestoreTableResponse(TypedDict, closed=True):
    restored_table_arn: "aws_sdk_keyspaces.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the restored table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RestoreTableResponse) -> dict:
    out: dict = {}
    out["restoredTableARN"] = value["restored_table_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RestoreTableResponse:
    out: RestoreTableResponse = {}  # type: ignore[typeddict-item]
    if "restoredTableARN" in data:
        out["restored_table_arn"] = data["restoredTableARN"]
    else:
        raise DeserializationError("RestoreTableResponse.restored_table_arn required")
    return out
