"""Generated from Smithy shape ``com.amazonaws.glue#RedshiftTarget``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.enclosed_in_string_property
    import aws_sdk_glue.types.node_name
    import aws_sdk_glue.types.one_input
    import aws_sdk_glue.types.upsert_redshift_target_options


class RedshiftTarget(TypedDict):
    name: "aws_sdk_glue.types.node_name.NodeName"
    """<p>The name of the data target.</p>"""
    inputs: "aws_sdk_glue.types.one_input.OneInput"
    """<p>The nodes that are inputs to the data target.</p>"""
    database: "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The name of the database to write to.</p>"""
    table: "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The name of the table in the database to write to.</p>"""
    redshift_tmp_dir: NotRequired[
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The Amazon S3 path where temporary data can be staged when copying out of the database.</p>"""
    tmp_dir_iam_role: NotRequired[
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The IAM role with permissions.</p>"""
    upsert_redshift_options: NotRequired[
        "aws_sdk_glue.types.upsert_redshift_target_options.UpsertRedshiftTargetOptions"
    ]
    """<p>The set of options to configure an upsert operation when writing to a Redshift target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RedshiftTarget) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_glue.types.one_input

    out["Inputs"] = aws_sdk_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    out["Database"] = value["database"]
    out["Table"] = value["table"]
    if "redshift_tmp_dir" in value:
        out["RedshiftTmpDir"] = value["redshift_tmp_dir"]
    if "tmp_dir_iam_role" in value:
        out["TmpDirIAMRole"] = value["tmp_dir_iam_role"]
    if "upsert_redshift_options" in value:
        import aws_sdk_glue.types.upsert_redshift_target_options

        out["UpsertRedshiftOptions"] = (
            aws_sdk_glue.types.upsert_redshift_target_options.serialize_aws_json_1_1(
                value["upsert_redshift_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RedshiftTarget:
    out: RedshiftTarget = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("RedshiftTarget.name required")
    if "Inputs" in data:
        import aws_sdk_glue.types.one_input

        out["inputs"] = aws_sdk_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        raise DeserializationError("RedshiftTarget.inputs required")
    if "Database" in data:
        out["database"] = data["Database"]
    else:
        raise DeserializationError("RedshiftTarget.database required")
    if "Table" in data:
        out["table"] = data["Table"]
    else:
        raise DeserializationError("RedshiftTarget.table required")
    if "RedshiftTmpDir" in data:
        out["redshift_tmp_dir"] = data["RedshiftTmpDir"]
    if "TmpDirIAMRole" in data:
        out["tmp_dir_iam_role"] = data["TmpDirIAMRole"]
    if "UpsertRedshiftOptions" in data:
        import aws_sdk_glue.types.upsert_redshift_target_options

        out["upsert_redshift_options"] = (
            aws_sdk_glue.types.upsert_redshift_target_options.deserialize_aws_json_1_1(
                data["UpsertRedshiftOptions"]
            )
        )
    return out
