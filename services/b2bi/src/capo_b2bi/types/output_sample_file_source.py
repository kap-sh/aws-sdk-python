"""Generated from Smithy shape ``com.amazonaws.b2bi#OutputSampleFileSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_b2bi.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_b2bi.types.s3_location


class _OutputSampleFileSource_fileLocation(TypedDict, closed=True):
    fileLocation: "capo_b2bi.types.s3_location.S3Location"


OutputSampleFileSource: TypeAlias = _OutputSampleFileSource_fileLocation


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OutputSampleFileSource) -> dict:
    if "fileLocation" in value:
        import capo_b2bi.types.s3_location

        return {
            "fileLocation": capo_b2bi.types.s3_location.serialize_aws_json_1_0(
                value["fileLocation"]
            )
        }
    else:
        raise SerializationError("OutputSampleFileSource: no variant present")


def deserialize_aws_json_1_0(data: dict) -> OutputSampleFileSource:
    if "fileLocation" in data:
        import capo_b2bi.types.s3_location

        return {
            "fileLocation": capo_b2bi.types.s3_location.deserialize_aws_json_1_0(
                data["fileLocation"]
            )
        }
    else:
        raise DeserializationError("OutputSampleFileSource: no recognized variant key")
