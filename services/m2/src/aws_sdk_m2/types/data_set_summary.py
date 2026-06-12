"""Generated from Smithy shape ``com.amazonaws.m2#DataSetSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_m2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.string20
    import aws_sdk_m2.types.string200
    import aws_sdk_m2.types.timestamp


class DataSetSummary(TypedDict):
    data_set_name: "aws_sdk_m2.types.string200.String200"
    """<p>The name of the data set.</p>"""
    data_set_org: NotRequired["aws_sdk_m2.types.string20.String20"]
    """<p>The type of data set. The only supported value is VSAM.</p>"""
    format: NotRequired["aws_sdk_m2.types.string20.String20"]
    """<p>The format of the data set. </p>"""
    creation_time: NotRequired["aws_sdk_m2.types.timestamp.Timestamp"]
    """<p>The timestamp when the data set was created.</p>"""
    last_updated_time: NotRequired["aws_sdk_m2.types.timestamp.Timestamp"]
    """<p>The last time the data set was updated.</p>"""
    last_referenced_time: NotRequired["aws_sdk_m2.types.timestamp.Timestamp"]
    """<p>The last time the data set was referenced.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetSummary) -> dict:
    out: dict = {}
    out["dataSetName"] = value["data_set_name"]
    if "data_set_org" in value:
        out["dataSetOrg"] = value["data_set_org"]
    if "format" in value:
        out["format"] = value["format"]
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
    return out


def deserialize_json(data: dict) -> DataSetSummary:
    out: DataSetSummary = {}  # type: ignore[typeddict-item]
    if "dataSetName" in data:
        out["data_set_name"] = data["dataSetName"]
    else:
        raise DeserializationError("DataSetSummary.data_set_name required")
    if "dataSetOrg" in data:
        out["data_set_org"] = data["dataSetOrg"]
    if "format" in data:
        out["format"] = data["format"]
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
    return out
