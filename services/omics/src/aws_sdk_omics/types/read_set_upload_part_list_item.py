"""Generated from Smithy shape ``com.amazonaws.omics#ReadSetUploadPartListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_omics.types.read_set_part_source


class ReadSetUploadPartListItem(TypedDict, closed=True):
    part_number: "int"
    """<p> The number identifying the part in an upload. </p>"""
    part_size: "int"
    """<p> The size of the the part in an upload. </p>"""
    part_source: "aws_sdk_omics.types.read_set_part_source.ReadSetPartSource"
    """<p> The origin of the part being direct uploaded. </p>"""
    checksum: "str"
    """<p> A unique identifier used to confirm that parts are being added to the correct upload. </p>"""
    creation_time: NotRequired["datetime.datetime"]
    """<p> The time stamp for when a direct upload was created. </p>"""
    last_updated_time: NotRequired["datetime.datetime"]
    """<p> The time stamp for the most recent update to an uploaded part. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadSetUploadPartListItem) -> dict:
    out: dict = {}
    out["partNumber"] = value["part_number"]
    out["partSize"] = value["part_size"]
    out["partSource"] = value["part_source"]
    out["checksum"] = value["checksum"]
    if "creation_time" in value:
        import aws_sdk_omics.types._prelude.timestamp

        out["creationTime"] = aws_sdk_omics.types._prelude.timestamp.serialize_json(
            value["creation_time"]
        )
    if "last_updated_time" in value:
        import aws_sdk_omics.types._prelude.timestamp

        out["lastUpdatedTime"] = aws_sdk_omics.types._prelude.timestamp.serialize_json(
            value["last_updated_time"]
        )
    return out


def deserialize_json(data: dict) -> ReadSetUploadPartListItem:
    out: ReadSetUploadPartListItem = {}  # type: ignore[typeddict-item]
    if "partNumber" in data:
        out["part_number"] = data["partNumber"]
    else:
        raise DeserializationError("ReadSetUploadPartListItem.part_number required")
    if "partSize" in data:
        out["part_size"] = data["partSize"]
    else:
        raise DeserializationError("ReadSetUploadPartListItem.part_size required")
    if "partSource" in data:
        out["part_source"] = data["partSource"]
    else:
        raise DeserializationError("ReadSetUploadPartListItem.part_source required")
    if "checksum" in data:
        out["checksum"] = data["checksum"]
    else:
        raise DeserializationError("ReadSetUploadPartListItem.checksum required")
    if "creationTime" in data:
        import aws_sdk_omics.types._prelude.timestamp

        out["creation_time"] = aws_sdk_omics.types._prelude.timestamp.deserialize_json(
            data["creationTime"]
        )
    if "lastUpdatedTime" in data:
        import aws_sdk_omics.types._prelude.timestamp

        out["last_updated_time"] = (
            aws_sdk_omics.types._prelude.timestamp.deserialize_json(
                data["lastUpdatedTime"]
            )
        )
    return out
