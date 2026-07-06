"""Generated from Smithy shape ``com.amazonaws.glue#DeleteRegistryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.registry_id


class DeleteRegistryInput(TypedDict, closed=True):
    registry_id: "aws_sdk_glue.types.registry_id.RegistryId"
    """<p>This is a wrapper structure that may contain the registry name and Amazon Resource Name (ARN).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRegistryInput) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.registry_id

    out["RegistryId"] = aws_sdk_glue.types.registry_id.serialize_aws_json_1_1(
        value["registry_id"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRegistryInput:
    out: DeleteRegistryInput = {}  # type: ignore[typeddict-item]
    if "RegistryId" in data:
        import aws_sdk_glue.types.registry_id

        out["registry_id"] = aws_sdk_glue.types.registry_id.deserialize_aws_json_1_1(
            data["RegistryId"]
        )
    else:
        raise DeserializationError("DeleteRegistryInput.registry_id required")
    return out
