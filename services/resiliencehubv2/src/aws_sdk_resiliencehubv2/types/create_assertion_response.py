"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#CreateAssertionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.assertion


class CreateAssertionResponse(TypedDict, closed=True):
    assertion: "aws_sdk_resiliencehubv2.types.assertion.Assertion"
    """<p>The created assertion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssertionResponse) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehubv2.types.assertion

    out["assertion"] = aws_sdk_resiliencehubv2.types.assertion.serialize_json(
        value["assertion"]
    )
    return out


def deserialize_json(data: dict) -> CreateAssertionResponse:
    out: CreateAssertionResponse = {}  # type: ignore[typeddict-item]
    if "assertion" in data:
        import aws_sdk_resiliencehubv2.types.assertion

        out["assertion"] = aws_sdk_resiliencehubv2.types.assertion.deserialize_json(
            data["assertion"]
        )
    else:
        raise DeserializationError("CreateAssertionResponse.assertion required")
    return out
