"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#UpdateAssertionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.assertion


class UpdateAssertionResponse(TypedDict):
    assertion: "aws_sdk_resiliencehubv2.types.assertion.Assertion"
    """<p>The updated assertion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssertionResponse) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehubv2.types.assertion

    out["assertion"] = aws_sdk_resiliencehubv2.types.assertion.serialize_json(
        value["assertion"]
    )
    return out


def deserialize_json(data: dict) -> UpdateAssertionResponse:
    out: UpdateAssertionResponse = {}  # type: ignore[typeddict-item]
    if "assertion" in data:
        import aws_sdk_resiliencehubv2.types.assertion

        out["assertion"] = aws_sdk_resiliencehubv2.types.assertion.deserialize_json(
            data["assertion"]
        )
    else:
        raise DeserializationError("UpdateAssertionResponse.assertion required")
    return out
