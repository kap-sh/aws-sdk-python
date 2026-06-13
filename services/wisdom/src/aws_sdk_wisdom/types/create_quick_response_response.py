"""Generated from Smithy shape ``com.amazonaws.wisdom#CreateQuickResponseResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.quick_response_data


class CreateQuickResponseResponse(TypedDict):
    quick_response: NotRequired[
        "aws_sdk_wisdom.types.quick_response_data.QuickResponseData"
    ]
    """<p>The quick response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateQuickResponseResponse) -> dict:
    out: dict = {}
    if "quick_response" in value:
        import aws_sdk_wisdom.types.quick_response_data

        out["quickResponse"] = aws_sdk_wisdom.types.quick_response_data.serialize_json(
            value["quick_response"]
        )
    return out


def deserialize_json(data: dict) -> CreateQuickResponseResponse:
    out: CreateQuickResponseResponse = {}  # type: ignore[typeddict-item]
    if "quickResponse" in data:
        import aws_sdk_wisdom.types.quick_response_data

        out["quick_response"] = (
            aws_sdk_wisdom.types.quick_response_data.deserialize_json(
                data["quickResponse"]
            )
        )
    return out
