"""Generated from Smithy shape ``com.amazonaws.glue#UpdateRegistryInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.description_string
    import aws_sdk_glue.types.registry_id


class UpdateRegistryInput(TypedDict):
    registry_id: "aws_sdk_glue.types.registry_id.RegistryId"
    """<p>This is a wrapper structure that may contain the registry name and Amazon Resource Name (ARN).</p>"""
    description: "aws_sdk_glue.types.description_string.DescriptionString"
    """<p>A description of the registry. If description is not provided, this field will not be updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateRegistryInput) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.registry_id

    out["RegistryId"] = aws_sdk_glue.types.registry_id.serialize_aws_json_1_1(
        value["registry_id"]
    )
    out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateRegistryInput:
    out: UpdateRegistryInput = {}  # type: ignore[typeddict-item]
    if "RegistryId" in data:
        import aws_sdk_glue.types.registry_id

        out["registry_id"] = aws_sdk_glue.types.registry_id.deserialize_aws_json_1_1(
            data["RegistryId"]
        )
    else:
        raise DeserializationError("UpdateRegistryInput.registry_id required")
    if "Description" in data:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("UpdateRegistryInput.description required")
    return out
