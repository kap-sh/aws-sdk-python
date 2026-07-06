"""Generated from Smithy shape ``com.amazonaws.wisdom#GetQuickResponseResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.quick_response_data


class GetQuickResponseResponse(TypedDict, closed=True):
    quick_response: NotRequired[
        "aws_sdk_wisdom.types.quick_response_data.QuickResponseData"
    ]
    """<p>The quick response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQuickResponseResponse) -> dict:
    out: dict = {}
    if "quick_response" in value:
        import aws_sdk_wisdom.types.quick_response_data

        out["quickResponse"] = aws_sdk_wisdom.types.quick_response_data.serialize_json(
            value["quick_response"]
        )
    return out


def deserialize_json(data: dict) -> GetQuickResponseResponse:
    out: GetQuickResponseResponse = {}  # type: ignore[typeddict-item]
    if "quickResponse" in data:
        import aws_sdk_wisdom.types.quick_response_data

        out["quick_response"] = (
            aws_sdk_wisdom.types.quick_response_data.deserialize_json(
                data["quickResponse"]
            )
        )
    return out
