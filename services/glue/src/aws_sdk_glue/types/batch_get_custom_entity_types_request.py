"""Generated from Smithy shape ``com.amazonaws.glue#BatchGetCustomEntityTypesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.custom_entity_type_names


class BatchGetCustomEntityTypesRequest(TypedDict):
    names: "aws_sdk_glue.types.custom_entity_type_names.CustomEntityTypeNames"
    """<p>A list of names of the custom patterns that you want to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetCustomEntityTypesRequest) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.custom_entity_type_names

    out["Names"] = aws_sdk_glue.types.custom_entity_type_names.serialize_aws_json_1_1(
        value["names"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetCustomEntityTypesRequest:
    out: BatchGetCustomEntityTypesRequest = {}  # type: ignore[typeddict-item]
    if "Names" in data:
        import aws_sdk_glue.types.custom_entity_type_names

        out["names"] = (
            aws_sdk_glue.types.custom_entity_type_names.deserialize_aws_json_1_1(
                data["Names"]
            )
        )
    else:
        raise DeserializationError("BatchGetCustomEntityTypesRequest.names required")
    return out
