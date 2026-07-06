"""Generated from Smithy shape ``com.amazonaws.glue#UpsertRedshiftTargetOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.enclosed_in_string_properties_min_one
    import aws_sdk_glue.types.enclosed_in_string_property


class UpsertRedshiftTargetOptions(TypedDict, closed=True):
    table_location: NotRequired[
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The physical location of the Redshift table.</p>"""
    connection_name: NotRequired[
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The name of the connection to use to write to Redshift.</p>"""
    upsert_keys: NotRequired[
        "aws_sdk_glue.types.enclosed_in_string_properties_min_one.EnclosedInStringPropertiesMinOne"
    ]
    """<p>The keys used to determine whether to perform an update or insert.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpsertRedshiftTargetOptions) -> dict:
    out: dict = {}
    if "table_location" in value:
        out["TableLocation"] = value["table_location"]
    if "connection_name" in value:
        out["ConnectionName"] = value["connection_name"]
    if "upsert_keys" in value:
        import aws_sdk_glue.types.enclosed_in_string_properties_min_one

        out["UpsertKeys"] = (
            aws_sdk_glue.types.enclosed_in_string_properties_min_one.serialize_aws_json_1_1(
                value["upsert_keys"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpsertRedshiftTargetOptions:
    out: UpsertRedshiftTargetOptions = {}  # type: ignore[typeddict-item]
    if "TableLocation" in data:
        out["table_location"] = data["TableLocation"]
    if "ConnectionName" in data:
        out["connection_name"] = data["ConnectionName"]
    if "UpsertKeys" in data:
        import aws_sdk_glue.types.enclosed_in_string_properties_min_one

        out["upsert_keys"] = (
            aws_sdk_glue.types.enclosed_in_string_properties_min_one.deserialize_aws_json_1_1(
                data["UpsertKeys"]
            )
        )
    return out
