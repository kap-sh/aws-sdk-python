"""Generated from Smithy shape ``com.amazonaws.backup#IndexAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.resource_types


class IndexAction(TypedDict, closed=True):
    resource_types: NotRequired["capo_backup.types.resource_types.ResourceTypes"]
    """<p>0 or 1 index action will be accepted for each BackupRule.</p> <p>Valid values:</p> <ul> <li> <p> <code>EBS</code> for Amazon Elastic Block Store</p> </li> <li> <p> <code>S3</code> for Amazon Simple Storage Service (Amazon S3)</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: IndexAction) -> dict:
    out: dict = {}
    if "resource_types" in value:
        import capo_backup.types.resource_types

        out["ResourceTypes"] = capo_backup.types.resource_types.serialize_json(
            value["resource_types"]
        )
    return out


def deserialize_json(data: dict) -> IndexAction:
    out: IndexAction = {}  # type: ignore[typeddict-item]
    if "ResourceTypes" in data:
        import capo_backup.types.resource_types

        out["resource_types"] = capo_backup.types.resource_types.deserialize_json(
            data["ResourceTypes"]
        )
    return out
