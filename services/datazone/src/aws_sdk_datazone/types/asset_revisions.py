"""Generated from Smithy shape ``com.amazonaws.datazone#AssetRevisions``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_datazone.types.asset_revision

AssetRevisions: TypeAlias = list["aws_sdk_datazone.types.asset_revision.AssetRevision"]


# --- restJson1 ser/de ---
def serialize_json(value: AssetRevisions) -> list:
    import aws_sdk_datazone.types.asset_revision
    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.asset_revision.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssetRevisions:
    import aws_sdk_datazone.types.asset_revision
    out: AssetRevisions = []
    for item in data:
        out.append(aws_sdk_datazone.types.asset_revision.deserialize_json(item))
    return out