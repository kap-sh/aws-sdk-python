"""Generated from Smithy shape ``com.amazonaws.omics#ReferenceListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_omics.types.md5
    import aws_sdk_omics.types.reference_arn
    import aws_sdk_omics.types.reference_description
    import aws_sdk_omics.types.reference_id
    import aws_sdk_omics.types.reference_name
    import aws_sdk_omics.types.reference_status
    import aws_sdk_omics.types.reference_store_id


class ReferenceListItem(TypedDict, closed=True):
    id: "aws_sdk_omics.types.reference_id.ReferenceId"
    """<p>The reference's ID.</p>"""
    arn: "aws_sdk_omics.types.reference_arn.ReferenceArn"
    """<p>The reference's ARN.</p>"""
    reference_store_id: "aws_sdk_omics.types.reference_store_id.ReferenceStoreId"
    """<p>The reference's store ID.</p>"""
    md5: "aws_sdk_omics.types.md5.Md5"
    """<p>The reference's MD5 checksum.</p>"""
    status: NotRequired["aws_sdk_omics.types.reference_status.ReferenceStatus"]
    """<p>The reference's status.</p>"""
    name: NotRequired["aws_sdk_omics.types.reference_name.ReferenceName"]
    """<p>The reference's name.</p>"""
    description: NotRequired[
        "aws_sdk_omics.types.reference_description.ReferenceDescription"
    ]
    """<p>The reference's description.</p>"""
    creation_time: "datetime.datetime"
    """<p>When the reference was created.</p>"""
    update_time: "datetime.datetime"
    """<p>When the reference was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceListItem) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["referenceStoreId"] = value["reference_store_id"]
    out["md5"] = value["md5"]
    if "status" in value:
        out["status"] = value["status"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_omics.types._prelude.timestamp

    out["creationTime"] = aws_sdk_omics.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    import aws_sdk_omics.types._prelude.timestamp

    out["updateTime"] = aws_sdk_omics.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    return out


def deserialize_json(data: dict) -> ReferenceListItem:
    out: ReferenceListItem = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ReferenceListItem.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("ReferenceListItem.arn required")
    if "referenceStoreId" in data:
        out["reference_store_id"] = data["referenceStoreId"]
    else:
        raise DeserializationError("ReferenceListItem.reference_store_id required")
    if "md5" in data:
        out["md5"] = data["md5"]
    else:
        raise DeserializationError("ReferenceListItem.md5 required")
    if "status" in data:
        out["status"] = data["status"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "creationTime" in data:
        import aws_sdk_omics.types._prelude.timestamp

        out["creation_time"] = aws_sdk_omics.types._prelude.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("ReferenceListItem.creation_time required")
    if "updateTime" in data:
        import aws_sdk_omics.types._prelude.timestamp

        out["update_time"] = aws_sdk_omics.types._prelude.timestamp.deserialize_json(
            data["updateTime"]
        )
    else:
        raise DeserializationError("ReferenceListItem.update_time required")
    return out
