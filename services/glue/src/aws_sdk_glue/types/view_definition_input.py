"""Generated from Smithy shape ``com.amazonaws.glue#ViewDefinitionInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.arn_string
    import aws_sdk_glue.types.last_refresh_type
    import aws_sdk_glue.types.nullable_boolean
    import aws_sdk_glue.types.refresh_seconds
    import aws_sdk_glue.types.table_version_id
    import aws_sdk_glue.types.version_string
    import aws_sdk_glue.types.view_representation_input_list
    import aws_sdk_glue.types.view_sub_object_version_ids_list
    import aws_sdk_glue.types.view_sub_objects_list


class ViewDefinitionInput(TypedDict):
    is_protected: NotRequired["aws_sdk_glue.types.nullable_boolean.NullableBoolean"]
    """<p>You can set this flag as true to instruct the engine not to push user-provided operations into the logical plan of the view during query planning. However, setting this flag does not guarantee that the engine will comply. Refer to the engine's documentation to understand the guarantees provided, if any.</p>"""
    definer: NotRequired["aws_sdk_glue.types.arn_string.ArnString"]
    """<p>The definer of a view in SQL.</p>"""
    representations: NotRequired[
        "aws_sdk_glue.types.view_representation_input_list.ViewRepresentationInputList"
    ]
    """<p>A list of structures that contains the dialect of the view, and the query that defines the view.</p>"""
    view_version_id: "aws_sdk_glue.types.table_version_id.TableVersionId"
    """<p>The ID value that identifies this view's version. For materialized views, the version ID is the Apache Iceberg table's snapshot ID. </p>"""
    view_version_token: NotRequired["aws_sdk_glue.types.version_string.VersionString"]
    """<p>The version ID of the Apache Iceberg table.</p>"""
    refresh_seconds: NotRequired["aws_sdk_glue.types.refresh_seconds.RefreshSeconds"]
    """<p>Auto refresh interval in seconds for the materialized view. If not specified, the view will not automatically refresh.</p>"""
    last_refresh_type: NotRequired[
        "aws_sdk_glue.types.last_refresh_type.LastRefreshType"
    ]
    """<p>The type of the materialized view's last refresh. Valid values: <code>Full</code>, <code>Incremental</code>.</p>"""
    sub_objects: NotRequired[
        "aws_sdk_glue.types.view_sub_objects_list.ViewSubObjectsList"
    ]
    """<p>A list of base table ARNs that make up the view.</p>"""
    sub_object_version_ids: NotRequired[
        "aws_sdk_glue.types.view_sub_object_version_ids_list.ViewSubObjectVersionIdsList"
    ]
    """<p>List of the Apache Iceberg table versions referenced by the materialized view.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ViewDefinitionInput) -> dict:
    out: dict = {}
    if "is_protected" in value:
        out["IsProtected"] = value["is_protected"]
    if "definer" in value:
        out["Definer"] = value["definer"]
    if "representations" in value:
        import aws_sdk_glue.types.view_representation_input_list

        out["Representations"] = (
            aws_sdk_glue.types.view_representation_input_list.serialize_aws_json_1_1(
                value["representations"]
            )
        )
    out["ViewVersionId"] = value.get("view_version_id", 0)
    if "view_version_token" in value:
        out["ViewVersionToken"] = value["view_version_token"]
    if "refresh_seconds" in value:
        out["RefreshSeconds"] = value["refresh_seconds"]
    if "last_refresh_type" in value:
        import aws_sdk_glue.types.last_refresh_type

        out["LastRefreshType"] = (
            aws_sdk_glue.types.last_refresh_type.serialize_aws_json_1_1(
                value["last_refresh_type"]
            )
        )
    if "sub_objects" in value:
        import aws_sdk_glue.types.view_sub_objects_list

        out["SubObjects"] = (
            aws_sdk_glue.types.view_sub_objects_list.serialize_aws_json_1_1(
                value["sub_objects"]
            )
        )
    if "sub_object_version_ids" in value:
        import aws_sdk_glue.types.view_sub_object_version_ids_list

        out["SubObjectVersionIds"] = (
            aws_sdk_glue.types.view_sub_object_version_ids_list.serialize_aws_json_1_1(
                value["sub_object_version_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ViewDefinitionInput:
    out: ViewDefinitionInput = {}  # type: ignore[typeddict-item]
    if "IsProtected" in data:
        out["is_protected"] = data["IsProtected"]
    if "Definer" in data:
        out["definer"] = data["Definer"]
    if "Representations" in data:
        import aws_sdk_glue.types.view_representation_input_list

        out["representations"] = (
            aws_sdk_glue.types.view_representation_input_list.deserialize_aws_json_1_1(
                data["Representations"]
            )
        )
    if "ViewVersionId" in data:
        out["view_version_id"] = data["ViewVersionId"]
    else:
        out["view_version_id"] = 0
    if "ViewVersionToken" in data:
        out["view_version_token"] = data["ViewVersionToken"]
    if "RefreshSeconds" in data:
        out["refresh_seconds"] = data["RefreshSeconds"]
    if "LastRefreshType" in data:
        import aws_sdk_glue.types.last_refresh_type

        out["last_refresh_type"] = (
            aws_sdk_glue.types.last_refresh_type.deserialize_aws_json_1_1(
                data["LastRefreshType"]
            )
        )
    if "SubObjects" in data:
        import aws_sdk_glue.types.view_sub_objects_list

        out["sub_objects"] = (
            aws_sdk_glue.types.view_sub_objects_list.deserialize_aws_json_1_1(
                data["SubObjects"]
            )
        )
    if "SubObjectVersionIds" in data:
        import aws_sdk_glue.types.view_sub_object_version_ids_list

        out["sub_object_version_ids"] = (
            aws_sdk_glue.types.view_sub_object_version_ids_list.deserialize_aws_json_1_1(
                data["SubObjectVersionIds"]
            )
        )
    return out
