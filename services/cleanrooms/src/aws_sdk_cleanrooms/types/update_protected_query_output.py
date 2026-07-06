"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdateProtectedQueryOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.protected_query


class UpdateProtectedQueryOutput(TypedDict, closed=True):
    protected_query: "aws_sdk_cleanrooms.types.protected_query.ProtectedQuery"
    """<p>The protected query output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProtectedQueryOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.protected_query

    out["protectedQuery"] = aws_sdk_cleanrooms.types.protected_query.serialize_json(
        value["protected_query"]
    )
    return out


def deserialize_json(data: dict) -> UpdateProtectedQueryOutput:
    out: UpdateProtectedQueryOutput = {}  # type: ignore[typeddict-item]
    if "protectedQuery" in data:
        import aws_sdk_cleanrooms.types.protected_query

        out["protected_query"] = (
            aws_sdk_cleanrooms.types.protected_query.deserialize_json(
                data["protectedQuery"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateProtectedQueryOutput.protected_query required"
        )
    return out
