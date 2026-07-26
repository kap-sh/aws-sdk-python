"""Generated from Smithy shape ``com.amazonaws.firehose#TableCreationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_firehose.errors import DeserializationError

if TYPE_CHECKING:
    import capo_firehose.types.boolean_object


class TableCreationConfiguration(TypedDict, closed=True):
    enabled: "capo_firehose.types.boolean_object.BooleanObject"
    """<p> Specify whether you want to enable automatic table creation. </p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableCreationConfiguration) -> dict:
    out: dict = {}
    out["Enabled"] = value["enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TableCreationConfiguration:
    out: TableCreationConfiguration = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    else:
        raise DeserializationError("TableCreationConfiguration.enabled required")
    return out
