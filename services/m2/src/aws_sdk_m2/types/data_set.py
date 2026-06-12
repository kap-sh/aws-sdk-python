"""Generated from Smithy shape ``com.amazonaws.m2#DataSet``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_m2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.dataset_org_attributes
    import aws_sdk_m2.types.record_length


class DataSet(TypedDict):
    storage_type: NotRequired["str"]
    """<p>The storage type of the data set: database or file system. For Micro Focus, database corresponds to datastore and file system corresponds to EFS/FSX. For Blu Age, there is no support of file system and database corresponds to Blusam. </p>"""
    dataset_name: "str"
    """<p>The logical identifier for a specific data set (in mainframe format).</p>"""
    dataset_org: "aws_sdk_m2.types.dataset_org_attributes.DatasetOrgAttributes"
    """<p>The type of dataset. The only supported value is VSAM.</p>"""
    relative_path: NotRequired["str"]
    """<p>The relative location of the data set in the database or file system. </p>"""
    record_length: "aws_sdk_m2.types.record_length.RecordLength"
    """<p>The length of a record.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSet) -> dict:
    out: dict = {}
    if "storage_type" in value:
        out["storageType"] = value["storage_type"]
    out["datasetName"] = value["dataset_name"]
    import aws_sdk_m2.types.dataset_org_attributes

    out["datasetOrg"] = aws_sdk_m2.types.dataset_org_attributes.serialize_json(
        value["dataset_org"]
    )
    if "relative_path" in value:
        out["relativePath"] = value["relative_path"]
    import aws_sdk_m2.types.record_length

    out["recordLength"] = aws_sdk_m2.types.record_length.serialize_json(
        value["record_length"]
    )
    return out


def deserialize_json(data: dict) -> DataSet:
    out: DataSet = {}  # type: ignore[typeddict-item]
    if "storageType" in data:
        out["storage_type"] = data["storageType"]
    if "datasetName" in data:
        out["dataset_name"] = data["datasetName"]
    else:
        raise DeserializationError("DataSet.dataset_name required")
    if "datasetOrg" in data:
        import aws_sdk_m2.types.dataset_org_attributes

        out["dataset_org"] = aws_sdk_m2.types.dataset_org_attributes.deserialize_json(
            data["datasetOrg"]
        )
    else:
        raise DeserializationError("DataSet.dataset_org required")
    if "relativePath" in data:
        out["relative_path"] = data["relativePath"]
    if "recordLength" in data:
        import aws_sdk_m2.types.record_length

        out["record_length"] = aws_sdk_m2.types.record_length.deserialize_json(
            data["recordLength"]
        )
    else:
        raise DeserializationError("DataSet.record_length required")
    return out
