"""Generated from Smithy shape ``com.amazonaws.sagemaker#S3FileSystem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.s3_schema_uri


class S3FileSystem(TypedDict, closed=True):
    s3_uri: NotRequired["capo_sagemaker.types.s3_schema_uri.S3SchemaUri"]
    """<p>The Amazon S3 URI that specifies the location in S3 where files are stored, which is mounted within the Studio environment. For example: <code>s3://&lt;bucket-name&gt;/&lt;prefix&gt;/</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3FileSystem) -> dict:
    out: dict = {}
    if "s3_uri" in value:
        out["S3Uri"] = value["s3_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3FileSystem:
    out: S3FileSystem = {}  # type: ignore[typeddict-item]
    if "S3Uri" in data:
        out["s3_uri"] = data["S3Uri"]
    return out
