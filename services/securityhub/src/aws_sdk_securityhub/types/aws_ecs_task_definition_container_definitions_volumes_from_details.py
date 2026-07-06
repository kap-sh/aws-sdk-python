"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string


class AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetails(
    TypedDict, closed=True
):
    read_only: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether the container has read-only access to the volume.</p>"""
    source_container: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of another container within the same task definition from which to mount volumes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetails,
) -> dict:
    out: dict = {}
    if "read_only" in value:
        out["ReadOnly"] = value["read_only"]
    if "source_container" in value:
        out["SourceContainer"] = value["source_container"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetails:
    out: AwsEcsTaskDefinitionContainerDefinitionsVolumesFromDetails = {}  # type: ignore[typeddict-item]
    if "ReadOnly" in data:
        out["read_only"] = data["ReadOnly"]
    if "SourceContainer" in data:
        out["source_container"] = data["SourceContainer"]
    return out
