"""Generated from Smithy shape ``com.amazonaws.schemas#GetCodeBindingSourceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_schemas.types.body


class GetCodeBindingSourceResponse(TypedDict):
    body: NotRequired["aws_sdk_schemas.types.body.Body"]


# --- restJson1 ser/de ---
def serialize_json(value: GetCodeBindingSourceResponse) -> dict:
    out: dict = {}
    if "body" in value:
        import aws_sdk_schemas.types.body

        out["Body"] = aws_sdk_schemas.types.body.serialize_json(value["body"])
    return out


def deserialize_json(data: dict) -> GetCodeBindingSourceResponse:
    out: GetCodeBindingSourceResponse = {}  # type: ignore[typeddict-item]
    if "Body" in data:
        import aws_sdk_schemas.types.body

        out["body"] = aws_sdk_schemas.types.body.deserialize_json(data["Body"])
    return out
