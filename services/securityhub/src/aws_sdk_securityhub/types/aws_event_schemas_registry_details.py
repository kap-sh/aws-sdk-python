"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEventSchemasRegistryDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEventSchemasRegistryDetails(TypedDict):
    description: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> A description of the registry to be created. </p>"""
    registry_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The Amazon Resource Name (ARN) of the registry. </p>"""
    registry_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The name of the schema registry. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEventSchemasRegistryDetails) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "registry_arn" in value:
        out["RegistryArn"] = value["registry_arn"]
    if "registry_name" in value:
        out["RegistryName"] = value["registry_name"]
    return out


def deserialize_json(data: dict) -> AwsEventSchemasRegistryDetails:
    out: AwsEventSchemasRegistryDetails = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "RegistryArn" in data:
        out["registry_arn"] = data["RegistryArn"]
    if "RegistryName" in data:
        out["registry_name"] = data["RegistryName"]
    return out
