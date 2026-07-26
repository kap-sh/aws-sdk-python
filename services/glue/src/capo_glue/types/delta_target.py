"""Generated from Smithy shape ``com.amazonaws.glue#DeltaTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.connection_name
    import capo_glue.types.nullable_boolean
    import capo_glue.types.path_list


class DeltaTarget(TypedDict, closed=True):
    delta_tables: NotRequired["capo_glue.types.path_list.PathList"]
    """<p>A list of the Amazon S3 paths to the Delta tables.</p>"""
    connection_name: NotRequired["capo_glue.types.connection_name.ConnectionName"]
    """<p>The name of the connection to use to connect to the Delta table target.</p>"""
    write_manifest: NotRequired["capo_glue.types.nullable_boolean.NullableBoolean"]
    """<p>Specifies whether to write the manifest files to the Delta table path.</p>"""
    create_native_delta_table: NotRequired[
        "capo_glue.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Specifies whether the crawler will create native tables, to allow integration with query engines that support querying of the Delta transaction log directly.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeltaTarget) -> dict:
    out: dict = {}
    if "delta_tables" in value:
        import capo_glue.types.path_list

        out["DeltaTables"] = capo_glue.types.path_list.serialize_aws_json_1_1(
            value["delta_tables"]
        )
    if "connection_name" in value:
        out["ConnectionName"] = value["connection_name"]
    if "write_manifest" in value:
        out["WriteManifest"] = value["write_manifest"]
    if "create_native_delta_table" in value:
        out["CreateNativeDeltaTable"] = value["create_native_delta_table"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeltaTarget:
    out: DeltaTarget = {}  # type: ignore[typeddict-item]
    if "DeltaTables" in data:
        import capo_glue.types.path_list

        out["delta_tables"] = capo_glue.types.path_list.deserialize_aws_json_1_1(
            data["DeltaTables"]
        )
    if "ConnectionName" in data:
        out["connection_name"] = data["ConnectionName"]
    if "WriteManifest" in data:
        out["write_manifest"] = data["WriteManifest"]
    if "CreateNativeDeltaTable" in data:
        out["create_native_delta_table"] = data["CreateNativeDeltaTable"]
    return out
