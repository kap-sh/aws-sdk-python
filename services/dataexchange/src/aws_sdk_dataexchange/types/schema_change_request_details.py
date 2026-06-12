"""Generated from Smithy shape ``com.amazonaws.dataexchange#SchemaChangeRequestDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.list_of_schema_change_details
    import aws_sdk_dataexchange.types.timestamp


class SchemaChangeRequestDetails(TypedDict):
    changes: NotRequired[
        "aws_sdk_dataexchange.types.list_of_schema_change_details.ListOfSchemaChangeDetails"
    ]
    """<p>List of schema changes happening in the scope of this notification. This can have up to 100 entries.</p>"""
    schema_change_at: "aws_sdk_dataexchange.types.timestamp.Timestamp"
    """<p>A date in the future when the schema change is taking effect.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SchemaChangeRequestDetails) -> dict:
    out: dict = {}
    if "changes" in value:
        import aws_sdk_dataexchange.types.list_of_schema_change_details

        out["Changes"] = (
            aws_sdk_dataexchange.types.list_of_schema_change_details.serialize_json(
                value["changes"]
            )
        )
    import aws_sdk_dataexchange.types.timestamp

    out["SchemaChangeAt"] = aws_sdk_dataexchange.types.timestamp.serialize_json(
        value["schema_change_at"]
    )
    return out


def deserialize_json(data: dict) -> SchemaChangeRequestDetails:
    out: SchemaChangeRequestDetails = {}  # type: ignore[typeddict-item]
    if "Changes" in data:
        import aws_sdk_dataexchange.types.list_of_schema_change_details

        out["changes"] = (
            aws_sdk_dataexchange.types.list_of_schema_change_details.deserialize_json(
                data["Changes"]
            )
        )
    if "SchemaChangeAt" in data:
        import aws_sdk_dataexchange.types.timestamp

        out["schema_change_at"] = aws_sdk_dataexchange.types.timestamp.deserialize_json(
            data["SchemaChangeAt"]
        )
    else:
        raise DeserializationError(
            "SchemaChangeRequestDetails.schema_change_at required"
        )
    return out
