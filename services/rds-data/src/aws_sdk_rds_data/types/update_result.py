"""Generated from Smithy shape ``com.amazonaws.rdsdata#UpdateResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rds_data.types.field_list


class UpdateResult(TypedDict):
    generated_fields: NotRequired["aws_sdk_rds_data.types.field_list.FieldList"]
    """<p>Values for fields generated during the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResult) -> dict:
    out: dict = {}
    if "generated_fields" in value:
        import aws_sdk_rds_data.types.field_list

        out["generatedFields"] = aws_sdk_rds_data.types.field_list.serialize_json(
            value["generated_fields"]
        )
    return out


def deserialize_json(data: dict) -> UpdateResult:
    out: UpdateResult = {}  # type: ignore[typeddict-item]
    if "generatedFields" in data:
        import aws_sdk_rds_data.types.field_list

        out["generated_fields"] = aws_sdk_rds_data.types.field_list.deserialize_json(
            data["generatedFields"]
        )
    return out
