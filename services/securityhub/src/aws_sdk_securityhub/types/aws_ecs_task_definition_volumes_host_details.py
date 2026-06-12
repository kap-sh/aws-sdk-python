"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionVolumesHostDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEcsTaskDefinitionVolumesHostDetails(TypedDict):
    source_path: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The path on the host container instance that is presented to the container.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsTaskDefinitionVolumesHostDetails) -> dict:
    out: dict = {}
    if "source_path" in value:
        out["SourcePath"] = value["source_path"]
    return out


def deserialize_json(data: dict) -> AwsEcsTaskDefinitionVolumesHostDetails:
    out: AwsEcsTaskDefinitionVolumesHostDetails = {}  # type: ignore[typeddict-item]
    if "SourcePath" in data:
        out["source_path"] = data["SourcePath"]
    return out
