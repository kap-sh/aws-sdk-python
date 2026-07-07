"""Generated from Smithy shape ``com.amazonaws.glue#GetMappingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.mapping_list


class GetMappingResponse(TypedDict, closed=True):
    mapping: "aws_sdk_glue.types.mapping_list.MappingList"
    """<p>A list of mappings to the specified targets.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMappingResponse) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.mapping_list

    out["Mapping"] = aws_sdk_glue.types.mapping_list.serialize_aws_json_1_1(
        value["mapping"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMappingResponse:
    out: GetMappingResponse = {}  # type: ignore[typeddict-item]
    if "Mapping" in data:
        import aws_sdk_glue.types.mapping_list

        out["mapping"] = aws_sdk_glue.types.mapping_list.deserialize_aws_json_1_1(
            data["Mapping"]
        )
    else:
        raise DeserializationError("GetMappingResponse.mapping required")
    return out
