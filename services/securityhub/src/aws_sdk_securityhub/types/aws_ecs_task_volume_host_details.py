"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskVolumeHostDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEcsTaskVolumeHostDetails(TypedDict):
    source_path: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>When the <code>host</code> parameter is used, specify a <code>sourcePath</code> to declare the path on the host container instance that's presented to the container. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsTaskVolumeHostDetails) -> dict:
    out: dict = {}
    if "source_path" in value:
        out["SourcePath"] = value["source_path"]
    return out


def deserialize_json(data: dict) -> AwsEcsTaskVolumeHostDetails:
    out: AwsEcsTaskVolumeHostDetails = {}  # type: ignore[typeddict-item]
    if "SourcePath" in data:
        out["source_path"] = data["SourcePath"]
    return out
