"""Generated from Smithy shape ``com.amazonaws.schemas#GetCodeBindingSourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_schemas.types.body


class GetCodeBindingSourceResponse(TypedDict, closed=True):
    body: NotRequired["capo_schemas.types.body.Body"]


# --- restJson1 ser/de ---
def serialize_json(value: GetCodeBindingSourceResponse) -> dict:
    out: dict = {}
    if "body" in value:
        import capo_schemas.types.body

        out["Body"] = capo_schemas.types.body.serialize_json(value["body"])
    return out


def deserialize_json(data: dict) -> GetCodeBindingSourceResponse:
    out: GetCodeBindingSourceResponse = {}  # type: ignore[typeddict-item]
    if "Body" in data:
        import capo_schemas.types.body

        out["body"] = capo_schemas.types.body.deserialize_json(data["Body"])
    return out
