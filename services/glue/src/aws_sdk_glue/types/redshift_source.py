"""Generated from Smithy shape ``com.amazonaws.glue#RedshiftSource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.enclosed_in_string_property
    import aws_sdk_glue.types.node_name


class RedshiftSource(TypedDict):
    name: "aws_sdk_glue.types.node_name.NodeName"
    """<p>The name of the Amazon Redshift data store.</p>"""
    database: "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The database to read from.</p>"""
    table: "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The database table to read from.</p>"""
    redshift_tmp_dir: NotRequired[
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The Amazon S3 path where temporary data can be staged when copying out of the database.</p>"""
    tmp_dir_iam_role: NotRequired[
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The IAM role with permissions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RedshiftSource) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Database"] = value["database"]
    out["Table"] = value["table"]
    if "redshift_tmp_dir" in value:
        out["RedshiftTmpDir"] = value["redshift_tmp_dir"]
    if "tmp_dir_iam_role" in value:
        out["TmpDirIAMRole"] = value["tmp_dir_iam_role"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RedshiftSource:
    out: RedshiftSource = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("RedshiftSource.name required")
    if "Database" in data:
        out["database"] = data["Database"]
    else:
        raise DeserializationError("RedshiftSource.database required")
    if "Table" in data:
        out["table"] = data["Table"]
    else:
        raise DeserializationError("RedshiftSource.table required")
    if "RedshiftTmpDir" in data:
        out["redshift_tmp_dir"] = data["RedshiftTmpDir"]
    if "TmpDirIAMRole" in data:
        out["tmp_dir_iam_role"] = data["TmpDirIAMRole"]
    return out
