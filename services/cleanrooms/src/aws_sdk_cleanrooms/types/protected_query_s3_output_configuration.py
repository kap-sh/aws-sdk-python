"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedQueryS3OutputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.key_prefix
    import aws_sdk_cleanrooms.types.result_format


class ProtectedQueryS3OutputConfiguration(TypedDict, closed=True):
    result_format: "aws_sdk_cleanrooms.types.result_format.ResultFormat"
    """<p>Intended file format of the result.</p>"""
    bucket: "str"
    """<p>The S3 bucket to unload the protected query results.</p>"""
    key_prefix: NotRequired["aws_sdk_cleanrooms.types.key_prefix.KeyPrefix"]
    """<p>The S3 prefix to unload the protected query results.</p>"""
    single_file_output: NotRequired["bool"]
    """<p>Indicates whether files should be output as a single file (<code>TRUE</code>) or output as multiple files (<code>FALSE</code>). This parameter is only supported for analyses with the Spark analytics engine.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedQueryS3OutputConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.result_format

    out["resultFormat"] = aws_sdk_cleanrooms.types.result_format.serialize_json(
        value["result_format"]
    )
    out["bucket"] = value["bucket"]
    if "key_prefix" in value:
        out["keyPrefix"] = value["key_prefix"]
    if "single_file_output" in value:
        out["singleFileOutput"] = value["single_file_output"]
    return out


def deserialize_json(data: dict) -> ProtectedQueryS3OutputConfiguration:
    out: ProtectedQueryS3OutputConfiguration = {}  # type: ignore[typeddict-item]
    if "resultFormat" in data:
        import aws_sdk_cleanrooms.types.result_format

        out["result_format"] = aws_sdk_cleanrooms.types.result_format.deserialize_json(
            data["resultFormat"]
        )
    else:
        raise DeserializationError(
            "ProtectedQueryS3OutputConfiguration.result_format required"
        )
    if "bucket" in data:
        out["bucket"] = data["bucket"]
    else:
        raise DeserializationError(
            "ProtectedQueryS3OutputConfiguration.bucket required"
        )
    if "keyPrefix" in data:
        out["key_prefix"] = data["keyPrefix"]
    if "singleFileOutput" in data:
        out["single_file_output"] = data["singleFileOutput"]
    return out
