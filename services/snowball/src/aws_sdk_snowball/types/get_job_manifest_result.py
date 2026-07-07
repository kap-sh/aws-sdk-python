"""Generated from Smithy shape ``com.amazonaws.snowball#GetJobManifestResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_snowball.types.string


class GetJobManifestResult(TypedDict, closed=True):
    manifest_uri: NotRequired["aws_sdk_snowball.types.string.String"]
    """<p>The Amazon S3 presigned URL for the manifest file associated with the specified <code>JobId</code> value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetJobManifestResult) -> dict:
    out: dict = {}
    if "manifest_uri" in value:
        out["ManifestURI"] = value["manifest_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetJobManifestResult:
    out: GetJobManifestResult = {}  # type: ignore[typeddict-item]
    if "ManifestURI" in data:
        out["manifest_uri"] = data["ManifestURI"]
    return out
