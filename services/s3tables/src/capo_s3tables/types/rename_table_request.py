"""Generated from Smithy shape ``com.amazonaws.s3tables#RenameTableRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.namespace_name
    import capo_s3tables.types.table_bucket_arn
    import capo_s3tables.types.table_name
    import capo_s3tables.types.version_token


class RenameTableRequest(TypedDict, closed=True):
    table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the table bucket. </p>"""
    namespace: "capo_s3tables.types.namespace_name.NamespaceName"
    """<p>The namespace associated with the table. </p>"""
    name: "capo_s3tables.types.table_name.TableName"
    """<p>The current name of the table.</p>"""
    new_namespace_name: NotRequired["capo_s3tables.types.namespace_name.NamespaceName"]
    """<p>The new name for the namespace.</p>"""
    new_name: NotRequired["capo_s3tables.types.table_name.TableName"]
    """<p>The new name for the table.</p>"""
    version_token: NotRequired["capo_s3tables.types.version_token.VersionToken"]
    """<p>The version token of the table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RenameTableRequest) -> dict:
    out: dict = {}
    if "new_namespace_name" in value:
        out["newNamespaceName"] = value["new_namespace_name"]
    if "new_name" in value:
        out["newName"] = value["new_name"]
    if "version_token" in value:
        out["versionToken"] = value["version_token"]
    return out


def deserialize_json(data: dict) -> RenameTableRequest:
    out: RenameTableRequest = {}  # type: ignore[typeddict-item]
    if "newNamespaceName" in data:
        out["new_namespace_name"] = data["newNamespaceName"]
    if "newName" in data:
        out["new_name"] = data["newName"]
    if "versionToken" in data:
        out["version_token"] = data["versionToken"]
    return out
