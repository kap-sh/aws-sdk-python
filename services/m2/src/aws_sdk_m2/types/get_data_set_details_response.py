"""Generated from Smithy shape ``com.amazonaws.m2#GetDataSetDetailsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_m2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.dataset_detail_org_attributes
    import aws_sdk_m2.types.integer
    import aws_sdk_m2.types.string200
    import aws_sdk_m2.types.string2000
    import aws_sdk_m2.types.timestamp


class GetDataSetDetailsResponse(TypedDict, closed=True):
    data_set_name: "aws_sdk_m2.types.string200.String200"
    """<p>The name of the data set.</p>"""
    data_set_org: NotRequired[
        "aws_sdk_m2.types.dataset_detail_org_attributes.DatasetDetailOrgAttributes"
    ]
    """<p>The type of data set. The only supported value is VSAM.</p>"""
    record_length: NotRequired["aws_sdk_m2.types.integer.Integer"]
    """<p>The length of records in the data set.</p>"""
    location: NotRequired["aws_sdk_m2.types.string2000.String2000"]
    """<p>The location where the data set is stored.</p>"""
    blocksize: NotRequired["aws_sdk_m2.types.integer.Integer"]
    """<p>The size of the block on disk. </p>"""
    creation_time: NotRequired["aws_sdk_m2.types.timestamp.Timestamp"]
    """<p>The timestamp when the data set was created.</p>"""
    last_updated_time: NotRequired["aws_sdk_m2.types.timestamp.Timestamp"]
    """<p>The last time the data set was updated.</p>"""
    last_referenced_time: NotRequired["aws_sdk_m2.types.timestamp.Timestamp"]
    """<p>The last time the data set was referenced.</p>"""
    file_size: NotRequired["int"]
    """<p>File size of the dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataSetDetailsResponse) -> dict:
    out: dict = {}
    out["dataSetName"] = value["data_set_name"]
    if "data_set_org" in value:
        import aws_sdk_m2.types.dataset_detail_org_attributes

        out["dataSetOrg"] = (
            aws_sdk_m2.types.dataset_detail_org_attributes.serialize_json(
                value["data_set_org"]
            )
        )
    if "record_length" in value:
        out["recordLength"] = value["record_length"]
    if "location" in value:
        out["location"] = value["location"]
    if "blocksize" in value:
        out["blocksize"] = value["blocksize"]
    if "creation_time" in value:
        import aws_sdk_m2.types.timestamp

        out["creationTime"] = aws_sdk_m2.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "last_updated_time" in value:
        import aws_sdk_m2.types.timestamp

        out["lastUpdatedTime"] = aws_sdk_m2.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    if "last_referenced_time" in value:
        import aws_sdk_m2.types.timestamp

        out["lastReferencedTime"] = aws_sdk_m2.types.timestamp.serialize_json(
            value["last_referenced_time"]
        )
    if "file_size" in value:
        out["fileSize"] = value["file_size"]
    return out


def deserialize_json(data: dict) -> GetDataSetDetailsResponse:
    out: GetDataSetDetailsResponse = {}  # type: ignore[typeddict-item]
    if "dataSetName" in data:
        out["data_set_name"] = data["dataSetName"]
    else:
        raise DeserializationError("GetDataSetDetailsResponse.data_set_name required")
    if "dataSetOrg" in data:
        import aws_sdk_m2.types.dataset_detail_org_attributes

        out["data_set_org"] = (
            aws_sdk_m2.types.dataset_detail_org_attributes.deserialize_json(
                data["dataSetOrg"]
            )
        )
    if "recordLength" in data:
        out["record_length"] = data["recordLength"]
    if "location" in data:
        out["location"] = data["location"]
    if "blocksize" in data:
        out["blocksize"] = data["blocksize"]
    if "creationTime" in data:
        import aws_sdk_m2.types.timestamp

        out["creation_time"] = aws_sdk_m2.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    if "lastUpdatedTime" in data:
        import aws_sdk_m2.types.timestamp

        out["last_updated_time"] = aws_sdk_m2.types.timestamp.deserialize_json(
            data["lastUpdatedTime"]
        )
    if "lastReferencedTime" in data:
        import aws_sdk_m2.types.timestamp

        out["last_referenced_time"] = aws_sdk_m2.types.timestamp.deserialize_json(
            data["lastReferencedTime"]
        )
    if "fileSize" in data:
        out["file_size"] = data["fileSize"]
    return out
