"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedQueryResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.protected_query_output


class ProtectedQueryResult(TypedDict, closed=True):
    output: "capo_cleanrooms.types.protected_query_output.ProtectedQueryOutput"
    """<p>The output of the protected query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedQueryResult) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.protected_query_output

    out["output"] = capo_cleanrooms.types.protected_query_output.serialize_json(
        value["output"]
    )
    return out


def deserialize_json(data: dict) -> ProtectedQueryResult:
    out: ProtectedQueryResult = {}  # type: ignore[typeddict-item]
    if "output" in data:
        import capo_cleanrooms.types.protected_query_output

        out["output"] = capo_cleanrooms.types.protected_query_output.deserialize_json(
            data["output"]
        )
    else:
        raise DeserializationError("ProtectedQueryResult.output required")
    return out
