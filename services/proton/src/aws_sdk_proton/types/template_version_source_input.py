"""Generated from Smithy shape ``com.amazonaws.proton#TemplateVersionSourceInput``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_proton.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.s3_object_source


class _TemplateVersionSourceInput_s3(TypedDict):
    s3: "aws_sdk_proton.types.s3_object_source.S3ObjectSource"


TemplateVersionSourceInput: TypeAlias = _TemplateVersionSourceInput_s3


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TemplateVersionSourceInput) -> dict:
    if "s3" in value:
        import aws_sdk_proton.types.s3_object_source

        return {
            "s3": aws_sdk_proton.types.s3_object_source.serialize_aws_json_1_0(
                value["s3"]
            )
        }
    else:
        raise SerializationError("TemplateVersionSourceInput: no variant present")


def deserialize_aws_json_1_0(data: dict) -> TemplateVersionSourceInput:
    if "s3" in data:
        import aws_sdk_proton.types.s3_object_source

        return {
            "s3": aws_sdk_proton.types.s3_object_source.deserialize_aws_json_1_0(
                data["s3"]
            )
        }
    else:
        raise DeserializationError(
            "TemplateVersionSourceInput: no recognized variant key"
        )
