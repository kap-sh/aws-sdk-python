"""Generated from Smithy shape ``com.amazonaws.glue#JoinColumn``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.enclosed_in_string_property
    import aws_sdk_glue.types.glue_studio_path_list

JoinColumn = TypedDict(
    "JoinColumn",
    {
        "from": "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty",
        "keys": "aws_sdk_glue.types.glue_studio_path_list.GlueStudioPathList",
    },
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JoinColumn) -> dict:
    out: dict = {}
    out["From"] = value["from"]
    import aws_sdk_glue.types.glue_studio_path_list

    out["Keys"] = aws_sdk_glue.types.glue_studio_path_list.serialize_aws_json_1_1(
        value["keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> JoinColumn:
    out: JoinColumn = {}  # type: ignore[typeddict-item]
    if "From" in data:
        out["from"] = data["From"]
    else:
        raise DeserializationError("JoinColumn.from required")
    if "Keys" in data:
        import aws_sdk_glue.types.glue_studio_path_list

        out["keys"] = aws_sdk_glue.types.glue_studio_path_list.deserialize_aws_json_1_1(
            data["Keys"]
        )
    else:
        raise DeserializationError("JoinColumn.keys required")
    return out
